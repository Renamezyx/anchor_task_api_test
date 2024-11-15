import json

import requests

import config
from common.request_base import request


class TaskCenter(object):
    def __init__(self, env):
        self.url = "https://explorer.tiktok-row.org/explorer/v5/rpc_request"
        self.headers = config.rpc_headers
        self.env = env
        self.json_data = {
            'serialization': 'json',
            'psm': 'tikcast.game.task_center',
            'func_name': None,
            'idl_source': 1,
            'idl_version': 'master',
            'env': self.env,
            'test_plane': 1,
            'zone': 'SGALI',
            'idc': 'my',
            'cluster': 'default',
            'http_req_headers': [],
            'http_cookies': [],
            'http_query': [],
            'req_body': None,
            'form_req_body': [],
            'rpc_context': [],
            'request_timeout': 60000,
            'connect_timeout': 60000,
            'source': 1,
            'protocol': 'thrift',
            'online': True,
            'request_id': 97057,
        }

    def fetch_task_info(self, user_id: int, scene: int) -> requests.Response:
        func_name = "FetchTaskInfo"
        req_body_temp = {
            "UserID": 7416313210217710597,
            "Query": {
                "Scene": 7,
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
            "Base": {
                "LogID": "",
                "Caller": "",
                "Addr": "",
                "Client": "",
                "TrafficEnv": {
                    "Open": False,
                    "Env": ""
                },
                "Extra": {
                    "": "",
                    "env": "ppe_ls_task_v3"
                }
            }
        }
        req_body_temp["UserID"] = user_id
        req_body_temp["Scene"] = scene
        req_body_temp["Base"]["Extra"]["env"] = self.env
        self.json_data["func_name"] = func_name
        self.json_data["req_body"] = str(json.dumps(req_body_temp))
        res = request(method="POST", url=self.url, headers=self.headers, json=self.json_data)
        return res


if __name__ == "__main__":
    t = TaskCenter("ppe_ls_level_task")
    res = t.fetch_task_info(7416313210217710597, 7)
    print(res.json()["data"]["resp_body"])
