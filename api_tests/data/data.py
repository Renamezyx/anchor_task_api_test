from api_tests.data.data_awards import DataAwards
from api_tests.data.data_tasks import DataTasks


def get_data():
    cases = []
    data_tasks = DataTasks()
    data_awards = DataAwards()
    task_list = data_tasks.get_task_detail()
    for task in task_list:
        case = task
        case["award_value"] = data_awards.get_awards(case["task_type"], case["anchor_level"], case["anchor_task_level"])
        cases.append(case)
    for case in cases:
        print(case)
    print(len(cases))
    return cases


if __name__ == "__main__":
    get_data()
