import datetime
import os.path
from multiprocessing import Manager

from account_manager import AccountManager
from utils.json_tools import JSONFileHandler
from common.logger_base import logger
import pytest
from config import get_project_root

account_manager = AccountManager()
manager = Manager()
test_results = manager.dict()


@pytest.fixture()
def load_test_cases():
    logger.info("Loading test cases...")


test_results = {}
test_parameters = {}


@pytest.fixture(scope='class')
def get_user(**kwargs):
    user = account_manager.get_account(**kwargs)
    yield user
    account_manager.release_account(user["user_id"])


def write_report(test_results, suffix=""):
    report_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + f"_report_{suffix}.json"
    report_path = os.path.join(get_project_root(), "reports", report_name)
    report_json_tool = JSONFileHandler(report_path)
    for k, v in test_results.items():
        report_json_tool.write(k, v)


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """主进程合并所有子进程的测试结果并写报告"""
    if hasattr(session.config, "workerinput"):  # 子进程行为
        suffix = f"_{os.getpid()}"
        write_report(test_results, suffix)
    else:  # 主进程行为
        write_report(test_results)


@pytest.hookimpl
def pytest_configure_node(node):
    """在每个子进程初始化测试结果字典"""
    node.workerinput["test_results"] = test_results


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_setup(item):
    # 获取当前测试用例的参数
    if hasattr(item, "callspec"):
        params = item.callspec.params
        test_parameters[item.nodeid] = params
    yield


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.when == "call":
        params = test_parameters[report.nodeid]
        test_results[
            f"({params['case_weekly']['info']['case_id'] if params.get('case_weekly') else 0},"
            f"{params['case_daily']['info']['case_id'] if params.get('case_daily') else 0})"
        ] = {
            "outcome": report.outcome,  # "passed", "failed", "skipped"
            "duration": report.duration
        }

# 动态修改 ids
