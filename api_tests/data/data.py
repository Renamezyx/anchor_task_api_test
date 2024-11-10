from api_tests.utils.xls_tools import XlsTools


class Data:
    def __init__(self, path_task_to_anchor_datas="../data/data.xlsx"):
        self.path_task_to_anchor_datas = path_task_to_anchor_datas
        self.task_to_anchor_datas = None
        self.title = None
        self.get_task_to_anchor_datas()

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


if __name__ == "__main__":
    o_datas = Data()
    datas = o_datas.task_to_anchor_datas
    anchor_task_for_levels = {}
    task_levels = [i for i in o_datas.title if "anchor_task_level_" in i]
    for i in datas:
        print(i)
    tasks_detail = []
    for task_level in task_levels:
        for data in datas:
            for i in data:
                if i in task_levels:
                    tasks_detail.append({'anchor_level': data["anchor_level"],
                                         'task_name': data["task_name"],
                                         'task_key': data["task_key"],
                                         'anchor_task_level': i.replace("anchor_task_level_", ""),
                                         'value': data[i]})
    for i in tasks_detail:
        print(i)
    print(len(tasks_detail),len(datas))