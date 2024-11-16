import datetime
import os.path

from api_tests.utils.json_tools import JSONFileHandler
from common.logger_base import logger

import pytest

from config import get_project_root


@pytest.fixture()
def load_test_cases():
    logger.info("Loading test cases...")


report_json_tool = None


@pytest.fixture(scope="session", autouse=True)
def report_create(request):
    report_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "_report.json"
    report_path = os.path.join(get_project_root(), report_name)
    os.makedirs(report_path, exist_ok=True)
    # shutil.copy(os.path.join(get_project_root(), "api_tests", "data", "data.json"),
    #             report_path)
    request.session.report_json_tool = JSONFileHandler  # 存储工具实例
    print(f"Report created at: {report_path}")
    print(f"Using report tool: {request.session.report_json_tool}")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    """
    捕获测试用例的执行结果。
    """
    test_results = {}

    if report.when == "call":  # 只记录测试执行阶段的结果
        test_results[report.nodeid] = {
            "outcome": report.outcome,  # 可能的值: "passed", "failed", "skipped"
            "duration": report.duration,  # 测试用例执行时间
            "longrepr": "failed" if report.failed else None,  # 失败详情
        }
        if hasattr(report.config, 'report_json_tool'):
            report_json_tool = report.config.report_json_tool
            print(f"Using report tool: {report_json_tool}")
            # 你可以在这里使用 report_json_tool 来记录测试结果
        else:
            print("No report_json_tool found.")
