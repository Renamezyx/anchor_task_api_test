import json

from api_tests.data.data_awards import DataAwards
from api_tests.utils.xls_tools import XlsTools


class DataAwardsClockIn:
    def __init__(self, path_award_datas="./meta/award_clockIn.xlsx"):
        self.path_award_datas = path_award_datas
        self.awards_to_task_datas = None
        self.title = None
        self.get_awards_to_task_datas()
        self.award_detail = self.get_award_detail()

    def get_awards_to_task_datas(self):
        awards = []
        xls = XlsTools(self.path_award_datas)
        all_rows = xls.read_all_rows()  # 只读取一次所有行
        keys = all_rows[0]  # 第一行作为键
        values = all_rows[1:]  # 后续行作为值

        for row in values:
            item = {}
            for idx, v in enumerate(row):
                key = keys[idx]
                item[key] = v
            awards.append(item)
        self.awards_to_task_datas = awards
        self.title = keys

    def get_award_detail(self):
        task_levels = [i for i in self.title if "task_level_" in i]
        award_detail = []
        for data in self.awards_to_task_datas:
            for i in data:
                if i in task_levels:
                    award_detail.append({'regin': data["regin"] or "",
                                         'anchor_level': data["anchor_level"],
                                         'task_level': i.replace("task_level_", ""),
                                         'value': eval(data[i])})
        return award_detail

    def get_award_value(self, regin, anchor_level, task_level):
        award_detail = self.award_detail
        for award in award_detail:
            if (award['regin'].lower(), award["anchor_level"], award["task_level"]) == (
                    regin.lower(), anchor_level, task_level):
                return award["value"]
        raise Exception("NONE")


if __name__ == "__main__":
    datas = DataAwardsClockIn().award_detail
    for i in datas:
        print(i)
