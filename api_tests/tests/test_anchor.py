import os

import pytest

from api_tests.api.http.anchor_task import ApiAnchorTask
from api_tests.utils.json_tools import JSONFileHandler
from common.logger_base import logger
from config import get_project_root


class TestAnchor:
    cases = JSONFileHandler(os.path.join(get_project_root(), "api_tests", "data", "data.json")).read("cases")
    cases = [cases[0]]

    @pytest.mark.parametrize("case", cases, ids=[i["case_no"] for i in cases])
    def test_fetch_task_info(self, case):
        logger.info(f"获取case: {case}")
        # 设置主播数据 pass
        anchor_task = ApiAnchorTask()
        res = anchor_task.fetch_task_info("3,4,7,8")
        assert all([res.status_code == 200, res.json()["status_code"] == 0])

        detail_info_map = res.json()["data"]["detail_info_map"]["7"] if case["task_case"]["task_type"] == "weekly" else \
            res.json()["data"]["detail_info_map"]["3"]
        assert detail_info_map["task_group_progress_list"]
        logger.info(detail_info_map["task_group_progress_list"])
        assert_task = [task for task in detail_info_map["task_group_progress_list"][0]["sub_task_progress_list"] if
                       task["sub_task_name_tag"] == case["task_case"]["task_key"]]
        logger.info(assert_task)
        # assert assert_task

