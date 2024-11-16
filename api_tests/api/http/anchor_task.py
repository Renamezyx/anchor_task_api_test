import unittest

import requests

import config
from common.request_base import request


class ApiAnchorTask(object):
    def __init__(self, headers=config.webcast_headers):
        self.headers = headers

    def fetch_task_info(self, scene_list: str) -> requests.Response:
        """
        :param scene_list: "3,4,7,8"
        :return:Response
        """
        url = "https://webcast.tiktok.com/webcast/game/studio/anchor_task/fetch_task_info/"
        params = {
            "scene_list": scene_list,
        }
        response = request("GET", url=url, headers=self.headers, params=params)
        return response


if __name__ == '__main__':
    api = ApiAnchorTask()
    print(api.fetch_task_info("3,4,7,8"))
