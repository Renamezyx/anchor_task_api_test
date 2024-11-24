import json
import random

from api_tests.data.data import AnchorWeeklyData
from api_tests.data.data_anchor_level_require import generate_data_for_level
from api_tests.data.data_awards import DataAwards
from api_tests.data.data_tasks import DataTasks


def get_tasks_details_for_class():
    data_tasks = DataTasks()
    data_awards = DataAwards()

    task_cases = []

    for task_detail in data_tasks.task_details:
        for t in data_tasks.generate_boundary_values(task_detail):
            t["assert_awards"] = data_awards.get_award_value(task_type=t["task_type"],
                                                             anchor_level=t["anchor_level"],
                                                             task_level=t["anchor_task_level"])
            task_cases.append(t)

    task_type = set([i["task_type"] for i in task_cases])
    task_key = set([i["task_key"] for i in task_cases])
    anchorLevel = set([i["anchor_level"] for i in task_cases])
    taskAnchorLevel = set([i["anchor_task_level"] for i in task_cases])

    tasks_for_t_k_al_tal = {
        t_type: {
            a_level:
                {
                    t_a_level:
                        {
                            t_key: [] for t_key in task_key
                        }
                    for t_a_level in taskAnchorLevel
                }
            for a_level in anchorLevel
        }
        for t_type in task_type
    }

    for task in task_cases:
        curr_tasks = tasks_for_t_k_al_tal[task["task_type"]][task["anchor_level"]][task["anchor_task_level"]][
            task["task_key"]]
        if task not in curr_tasks:
            tasks_for_t_k_al_tal[task["task_type"]][task["anchor_level"]][task["anchor_task_level"]][
                task["task_key"]].append(task)
    return tasks_for_t_k_al_tal


def get_anchor_level_case(level, regin=""):
    level_cases = generate_data_for_level(str(level), regin=regin)

    level_case = level_cases[random.randint(0, len(level_cases) - 1)]
    anchor_data = AnchorWeeklyData()
    anchor_data.i1 = level_case["Last7DayAvgAcu"]
    anchor_data.i2 = level_case["Last1DayFansCnt"]
    anchor_data.i3 = level_case["Last7DayWatchTotalDuration"]
    anchor_data.i4 = level_case["Last30DayIncome"]
    anchor_data.i5 = level_case["Last7DayIncome"]
    return anchor_data.to_dict()


if __name__ == '__main__':
    cases = []
    tasks_details_for_class = get_tasks_details_for_class()
    with open('task.json', 'w', encoding='utf-8') as f:
        json.dump({"cases": tasks_details_for_class}, f, ensure_ascii=False, indent=4)
    tasks_details_for_class_weekly = tasks_details_for_class["weekly"]
    tasks_details_for_class_daily = tasks_details_for_class["daily"]
    for anchorLevel in tasks_details_for_class_weekly:
        for taskALevel in tasks_details_for_class_weekly[anchorLevel]:
            info = {"ATALevel": f"{anchorLevel}_{taskALevel}","assert_value":{},"assert_awards":{}}
            flag = [True]
            index = 0
            while any(flag):
                flag = []
                anchor = get_anchor_level_case(anchorLevel)
                anchor["mock_scene"] = 3
                for taskKey in tasks_details_for_class_weekly[anchorLevel][taskALevel]:
                    if tasks_details_for_class_weekly[anchorLevel][taskALevel][taskKey]:
                        anchor[taskKey] = tasks_details_for_class_weekly[anchorLevel][taskALevel][taskKey].pop()
                        info["assert_value"][taskKey] = anchor[taskKey]["assert_value"]
                        info["assert_awards"][taskKey] = anchor[taskKey]["assert_awards"]
                        anchor[taskKey] = anchor[taskKey]["value"]
                        flag.append(tasks_details_for_class_weekly[anchorLevel][taskALevel][taskKey])
                    else:
                        anchor[taskKey] = 0
                        info["assert_value"][taskKey] = None
                        info["assert_awards"][taskKey] = None
                index += 1
                cases.append({"info": info, "anchor": anchor})

            print(index)

    print(len(cases))
    with open('cases.json', 'w', encoding='utf-8') as f:
        json.dump({"cases": cases}, f, ensure_ascii=False, indent=4)

    #
    # for key in anchor:
    #         if key in tasks_details_for_class_weekly["anchorLevel"]:
    #             anchor[key] = tasks_details_for_class_weekly["anchorLevel"][key].pop() if len(
    #                 tasks_details_for_class_weekly["anchorLevel"][key]) > 0 else 0

    # for l in tasks_details_for_class:
    #     for anchor_level in tasks_details_for_class[l]:
    #         for task_keys in tasks_details_for_class[l][anchor_level]:
    #             print(l, task_keys, len(tasks_details_for_class[l][anchor_level][task_keys]))
