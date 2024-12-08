import datetime
import os
from config import threading_num
import pytest

from config import get_project_root

if __name__ == '__main__':

    allure_report_path = os.path.join(get_project_root(), "allure_report",
                                      f"{datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}")
    if threading_num:
        code = pytest.main(["-q", "-s", "-n", str(threading_num), f"--alluredir={allure_report_path}"])
    else:
        code = pytest.main(["-q", "-s", f"--alluredir={allure_report_path}"])
    # if code == 0:
    #     os.system(f"allure serve {allure_report_path}")

    os.system(f"allure serve {allure_report_path}")
