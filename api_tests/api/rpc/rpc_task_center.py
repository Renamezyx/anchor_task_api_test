import json

import requests

import config
from api_tests.api.rpc.rpc_base import RPCBase
from common.request_base import request


class RPCTaskCenter(RPCBase):
    def __init__(self, env):
        super(RPCTaskCenter, self).__init__(psm="tikcast.game.task_center", env=env)
        self.url = "https://cloud-sg.tiktok-row.net/api/v1/explorer/explorer/v5/rpc_request"
        self.headers = config.rpc_headers
        self.env = env
        self.base = {
            "LogID": "",
            "Caller": "",
            "Addr": "",
            "Client": "",
            "TrafficEnv": {
                "Open": False,
                "Env": env
            },
            "Extra": {
                "": "",
                "env": ""
            }
        }

    def fetch_task_info(self, user_id: int, scene: int) -> requests.Response:
        func_name = "FetchTaskInfo"
        req_body = {
            "UserID": user_id,
            "Query": {
                "Scene": scene,
                "TaskPhaseList": [
                    0
                ],
                "Timing": 0
            },
            "Language": "",
            "RoomID": 0,
            "Timezone": "UTC",
            "Country": "",
            "Region": "",
            "DeviceID": 0,

        }
        req_body["Base"] = self.base
        self.json_data["func_name"] = func_name
        self.json_data["req_body"] = str(json.dumps(req_body))
        res = request(method="POST", url=self.url, headers=self.headers, json=self.json_data)
        return res

    def mock_stats_for_DW(self, stats: dict) -> requests.Response:
        func_name = "MockStats"
        req_body = {}
        req_body["Base"] = self.base
        req_body["Stats"] = stats
        self.json_data["func_name"] = func_name
        self.json_data["req_body"] = str(json.dumps(req_body))
        res = request(method="POST", url=self.url, headers=self.headers, json=self.json_data)
        return res

    def clean_cache(self, user_id: int, scene: int) -> requests.Response:
        func_name = "CleanCache"
        req_body = {}
        req_body["UserID"] = [user_id]
        req_body["Scene"] = scene
        req_body["Base"] = self.base
        self.json_data["func_name"] = func_name
        self.json_data["req_body"] = str(json.dumps(req_body))
        res = request(method="POST", url=self.url, headers=self.headers, json=self.json_data)
        return res


if __name__ == "__main__":
    t = TaskCenter("ppe_ls_task_qa_auto_test")
    # res = t.fetch_task_info(7443692687897183287, 7)
    # res = t.mock_stats_for_DW({
    #             "mock_scene": 3,
    #             "go_live_duration": 79,
    #             "total_watch_duration": 49,
    #             "gain_diamond_count": 0,
    #             "increase_fans_count": 0,
    #             "go_live_valid_day": 0,
    #             "increase_subscription_count": 0,
    #             "live_like_count": 279,
    #             "live_room_acu": 0,
    #             "link_micro_duration": 0,
    #             "increase_video_item_publish_count": 0,
    #             "co_host_duration": 0,
    #             "pk_victory": 0,
    #             "live_comment_count": 4,
    #             "1": 0,
    #             "2": 2999,
    #             "3": 0,
    #             "4": 0,
    #             "5": 0
    #         })
    res = t.clean_cache(7443692687897183287, 7)
    print(res.status_code)
    if res.status_code == 200:
        res = res.json()
        if res['error_code'] == 0:
            res = res["data"]["resp_body"]
            print(json.loads(res))
