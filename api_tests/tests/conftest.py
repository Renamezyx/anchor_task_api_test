import datetime
import os.path
from api_tests.utils.json_tools import JSONFileHandler
from common.logger_base import logger
import pytest
from config import get_project_root


@pytest.fixture()
def load_test_cases():
    logger.info("Loading test cases...")


test_results = {}


def write_report(test_results):
    report_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "_report.json"
    report_path = os.path.join(get_project_root(), "reports", report_name)
    report_json_tool = JSONFileHandler(report_path)
    for k, v in test_results.items():
        report_json_tool.write(k, v)


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    write_report(test_results)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.when == "call":
        test_results[report.nodeid] = {
            "outcome": report.outcome,  # "passed", "failed", "skipped"
            "duration": report.duration
        }
