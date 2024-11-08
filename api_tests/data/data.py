from api_tests.utils.xls_tools import XlsTools


class Data:
    def __init__(self, path_task_to_anchor_datas="../data/data.xlsx"):
        self.task_to_anchor_datas = Data.get_task_to_anchor_datas(path_task_to_anchor_datas)
    @staticmethod
    def get_task_to_anchor_datas(path_task_to_anchor_datas):
        task_to_anchor_datas = []
        xls = XlsTools(path_task_to_anchor_datas)
        all_rows = xls.read_all_rows()  # 只读取一次所有行
        keys = all_rows[0]  # 第一行作为键
        values = all_rows[1:]  # 后续行作为值

        for row in values:
            item = {}
            for idx, v in enumerate(row):
                key = keys[idx]
                item[key] = v
            task_to_anchor_datas.append(item)


        return task_to_anchor_datas


if __name__ == "__main__":
    o_datas = Data()
    datas = o_datas.task_to_anchor_datas
    anchor_task_for_levels = {}
    for data in datas:

