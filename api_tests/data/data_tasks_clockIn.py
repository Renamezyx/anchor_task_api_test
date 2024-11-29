import copy
import json

from api_tests.data.data_awards_clockIn import DataAwardsClockIn
from api_tests.utils.xls_tools import XlsTools


class DataTasksClockIn:
    def __init__(self, path_tasks_data_file="./meta/tasks_clockIn.xlsx"):
        self.task_to_anchor_datas = []
        self.title = None
        self.path_tasks_data_file = path_tasks_data_file
        self.get_task_to_anchor_datas()
        self.task_details = self.get_task_details()

    def get_task_to_anchor_datas(self):
        xls = XlsTools(self.path_tasks_data_file)
        all_rows = xls.read_all_rows()  # 只读取一次所有行
        keys = all_rows[0]  # 第一行作为键
        values = all_rows[1:]  # 后续行作为值
        for row in values:
            item = {}
            for idx, v in enumerate(row):
                key = keys[idx]
                item[key] = v
            self.task_to_anchor_datas.append(item)
        self.title = keys

    def get_task_details(self):
        task_levels = [i for i in self.title if "anchor_task_level_" in i]
        tasks_detail = []
        for data in self.task_to_anchor_datas:
            for item in data:
                if item in task_levels:
                    tasks_detail.append({'anchor_level': data["anchor_level"],
                                         'regin': data["regin"] or "",
                                         'task_name': data["task_name"],
                                         'task_key': data["task_key"],
                                         'anchor_task_level': item.replace("anchor_task_level_", ""),
                                         'value': eval(data[item])})
        return tasks_detail

    def generate_boundary_values(self, task_detail):
        res = []
        task = copy.copy(task_detail)
        task = self.compute_task_level(task)
        res.append(task)
        if task_detail["anchor_task_level"] == '10':
            task = copy.copy(task_detail)
            task["value"] = 0, 0
            task = self.compute_task_level(task)
            res.append(task)
        if task_detail["value"][0] > 1:
            task = copy.copy(task_detail)
            task["value"] = task["value"][0] - 1, task["value"][1]
            task = self.compute_task_level(task)
            res.append(task)
        if task_detail["value"][1] > 1:
            task = copy.copy(task_detail)
            task["value"] = task["value"][0], task["value"][1] - 1
            task = self.compute_task_level(task)
            res.append(task)
        if task_detail["value"][1] < 7:
            task = copy.copy(task_detail)
            task["value"] = task["value"][0], task["value"][1] + 1
            task = self.compute_task_level(task)
            res.append(task)
        task = copy.copy(task_detail)
        task["value"] = task["value"][0] + 1, task["value"][1]
        task = self.compute_task_level(task)
        res.append(task)
        return res

    def compute_task_level(self, task_detail):
        same_tasks = [i for i in self.task_details
                      if i["anchor_level"] == task_detail["anchor_level"]
                      and i["task_name"] == task_detail["task_name"]
                      and i["task_key"] == task_detail["task_key"]
                      and i["regin"] == task_detail["regin"]]
        same_tasks = sorted(same_tasks,
                            key=lambda x: int(x["anchor_task_level"]))
        anchor_task_level = None
        anchor_task_assert_value = None
        for index, task in enumerate(same_tasks):
            if task_detail["value"][0] >= task["value"][0] and task_detail["value"][1] >= task["value"][1]:
                if index == len(same_tasks) - 1:
                    anchor_task_level = same_tasks[-1]["anchor_task_level"]
                    anchor_task_assert_value = same_tasks[-1]["value"]
                else:
                    anchor_task_level = same_tasks[index + 1]["anchor_task_level"]
                    anchor_task_assert_value = same_tasks[index + 1]["value"][0], same_tasks[index + 1]["value"][1]
        if anchor_task_level is None:
            anchor_task_level = same_tasks[0]["anchor_task_level"]
            anchor_task_assert_value = same_tasks[0]["value"][0], same_tasks[0]["value"][1]
        task_detail["anchor_task_level"] = anchor_task_level
        task_detail["assert_value"] = anchor_task_assert_value
        return task_detail


if __name__ == '__main__':
    data_tasks = DataTasksClockIn()
    data_awards = DataAwardsClockIn()
    tasks = []
    for i in data_tasks.task_details:
        for t in data_tasks.generate_boundary_values(i):
            tasks.append(t)
    print(len(tasks))
    tasks = list({json.dumps(d, sort_keys=True) for d in tasks})
    tasks = [json.loads(u) for u in tasks]
    print(len(tasks))
    for i in tasks:
        print(i)
        print(data_awards.get_award_value(i["regin"], i["anchor_level"], i["anchor_task_level"]))
