import copy

from api_tests.utils.xls_tools import XlsTools


class DataTasks:
    def __init__(self, path_task_to_anchor_datas="../data/tasks.xlsx"):
        self.task_to_anchor_datas = None
        self.title = None
        self.path_task_to_anchor_datas = path_task_to_anchor_datas
        self.get_task_to_anchor_datas()
        self.task_details = self.get_task_details()

    def get_task_to_anchor_datas(self):
        task_to_anchor_datas = []
        xls = XlsTools(self.path_task_to_anchor_datas)
        all_rows = xls.read_all_rows()  # 只读取一次所有行
        keys = all_rows[0]  # 第一行作为键
        values = all_rows[1:]  # 后续行作为值

        for row in values:
            item = {}
            for idx, v in enumerate(row):
                key = keys[idx]
                item[key] = v
            task_to_anchor_datas.append(item)
        self.task_to_anchor_datas = task_to_anchor_datas
        self.title = keys

    def get_task_details(self):
        task_levels = [i for i in self.title if "anchor_task_level_" in i]
        tasks_detail = []
        # for task_level in task_levels:
        for data in self.task_to_anchor_datas:
            for i in data:
                if i in task_levels:
                    tasks_detail.append({'anchor_level': data["anchor_level"],
                                         'task_type': data["task_type"],
                                         'task_name': data["task_name"],
                                         'task_key': data["task_key"],
                                         'anchor_task_level': i.replace("anchor_task_level_", ""),
                                         'value': data[i]})
        return tasks_detail

    def generate_boundary_values(self, task_detail):
        res = []
        task = copy.copy(task_detail)
        task = self.compute_task_level(task)
        res.append(task)

        if task_detail["anchor_task_level"] == '10':
            task1 = copy.copy(task_detail)
            task1["value"] = 0
            task1 = self.compute_task_level(task1)
            res.append(task1)
        elif task_detail["value"] > 1:
            task2 = copy.copy(task_detail)
            task2["value"] = task_detail["value"] - 1
            task2 = self.compute_task_level(task2)
            res.append(task2)
        task3 = copy.copy(task_detail)
        task3["value"] = task_detail["value"] + 1
        task3 = self.compute_task_level(task3)
        res.append(task3)
        return res

    def compute_task_level(self, task_detail):
        same_task_level_tasks = [i for i in self.task_details
                                 if i["anchor_level"] == task_detail["anchor_level"]
                                 and i["task_type"] == task_detail["task_type"]
                                 and i["task_name"] == task_detail["task_name"]
                                 and i["task_key"] == task_detail["task_key"]]
        same_task_level_tasks = sorted(same_task_level_tasks, key=lambda x: int(x["anchor_task_level"]), reverse=True)

        anchor_task_level = same_task_level_tasks[-1]["anchor_task_level"]

        for task in same_task_level_tasks:
            if task["value"] <= task_detail["value"]:
                anchor_task_level = task["anchor_task_level"]
                break
        task_detail["anchor_task_level"] = anchor_task_level
        return task_detail


if __name__ == "__main__":
    datas = DataTasks()
    a = []
    for task in datas.task_details:
        for t in datas.generate_boundary_values(task):
            a.append(t)
    for i in a:
        print(i)
