import unittest

import requests

import config
from common.request_base import request


class ApiAnchorTask(object):
    def __init__(self, env=None):
        self.headers = {
            "Host": "webcast.tiktok.com",
            "Accept": "*/*",
            "Accept-Language": "zh-CN",
            "Cookie": ""
        }
        if env:
            self.headers["x-use-ppe"] = "1"
            self.headers["x-tt-env"] = env

    def fetch_task_info(self, session: str, scene_list: str = "3,4,6,7,8") -> requests.Response:
        """
        :param scene_list: "3,4,7,8"
        :return:Response
        """
        url = "https://webcast.tiktok.com/webcast/game/studio/anchor_task/fetch_task_info/"
        self.headers["Cookie"] = f"sessionid={session}"
        params = {
            "scene_list": scene_list,
        }
        response = request("GET", url=url, headers=self.headers, params=params)
        return response


if __name__ == '__main__':
    api = ApiAnchorTask(env="ppe_ls_task_qa_auto_test")
    print(api.fetch_task_info(scene_list="3,4,7,8", session="06b47b4259afa6ad7511d320926dd7f8"))
