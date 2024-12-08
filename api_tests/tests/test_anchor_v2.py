import json
import os
import time
from unittest import case

import pytest
import allure

from api_tests.api.http.https_anchor_task import ApiAnchorTask
from api_tests.api.rpc.rpc_task_center import RPCTaskCenter
from config import get_project_root

rpc_task_center = RPCTaskCenter(env="ppe_ls_task_qa_auto_test")
api_anchor_task = ApiAnchorTask(env="ppe_ls_task_qa_auto_test")
cases_weekly_file = os.path.join(get_project_root(), "api_tests", "data", "cases_weekly_default.json")
cases_daily_file = os.path.join(get_project_root(), "api_tests", "data", "cases_daily_default.json")
cases_clockIn_file = os.path.join(get_project_root(), "api_tests", "data", "cases_clockIn_default.json")
with open(cases_weekly_file, mode="r") as f:
    weekly_data = f.read()
    cases_weekly = json.loads(weekly_data)["cases"]
with open(cases_daily_file, mode="r") as f:
    daily_data = f.read()
    cases_daily = json.loads(daily_data)["cases"]
with open(cases_clockIn_file, mode="r") as f:
    clockIn_data = f.read()
    cases_clockIn = json.loads(clockIn_data)["cases"]

if len(cases_weekly) > len(cases_daily):
    cases_daily += [None] * (len(cases_weekly) - len(cases_daily))
else:
    cases_weekly += [None] * (len(cases_daily) - len(cases_weekly))


def clean_cache(user, case):
    if case is None:
        return None
    res = rpc_task_center.clean_cache(user["user_id"], case["anchor"]["mock_scene"])
    assert res.status_code == 200
    allure.attach(f'{res.json()["data"]["resp_body"]}')
    assert res.json()['error_code'] == 0


def mock_anchor(case):
    if case is None:
        return None
    stats = {}
    for key in case["anchor"]:
        stats[key] = case["anchor"][key]
        if stats[key] and any([f in key for f in ["go_live_duration", "total_watch_duration", "link_micro_duration",
                                                  "co_host_duration"]]):
            stats[key] = case["anchor"][key] * 60
    res = rpc_task_center.mock_stats_for_DW(case["anchor"])
    assert res.status_code == 200
    allure.attach(f'{res.json()["data"]["resp_body"]}')
    assert res.json()['error_code'] == 0


def generate_custom_ids(weekly_case, daily_case):
    return f"weekly_{weekly_case["info"]["case_id"] if weekly_case else 0}_daily_{daily_case["info"]["case_id"] if daily_case else 0}"


@pytest.mark.parametrize("get_user", [{"tag_list": ["liveStudio_anchor"]}], indirect=True)
@allure.feature("AnchorTask")
class TestAnchor:
    @pytest.mark.parametrize("case_weekly, case_daily", zip(cases_weekly, cases_daily))
    def test_fetch_task_info_WD(self, get_user, case_weekly, case_daily):
        with allure.step(f"当前weekly_case:{case_weekly}"):
            time.sleep(0)
        with allure.step(f"当前daily_case:{case_daily}"):
            time.sleep(0)
        with allure.step(f"当前账号: {get_user['user_id']}"):
            time.sleep(0)
