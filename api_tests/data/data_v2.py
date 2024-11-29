import json
import random

from api_tests.data.data import AnchorWeeklyData, AnchorDailyData, AnchorClockInData
from api_tests.data.data_anchor_level_require import generate_data_for_level
from api_tests.data.data_awards import DataAwards
from api_tests.data.data_awards_clockIn import DataAwardsClockIn
from api_tests.data.data_tasks import DataTasks
from api_tests.data.data_tasks_clockIn import DataTasksClockIn


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


def get_anchor_level_case(scene, level, regin=""):
    level_cases = generate_data_for_level(str(level), regin=regin)
    level_case = level_cases[random.randint(0, len(level_cases) - 1)]
    match scene:
        case 3:
            anchor_data = AnchorWeeklyData()
        case 7:
            anchor_data = AnchorDailyData()
        case 8:
            anchor_data = AnchorClockInData()
        case _:
            raise Exception("scene 参数未定义")
    anchor_data.i1 = level_case["Last7DayAvgAcu"]
    anchor_data.i2 = level_case["Last1DayFansCnt"]
    anchor_data.i3 = level_case["Last7DayWatchTotalDuration"]
    anchor_data.i4 = level_case["Last30DayIncome"]
    anchor_data.i5 = level_case["Last7DayIncome"]
    if scene == 8:
        return anchor_data
    return anchor_data.to_dict()


def gene_cases_for_type(task_details_for_class, scene):
    res = []
    for anchorLevel in task_details_for_class:
        for taskALevel in task_details_for_class[anchorLevel]:
            info = {"ATALevel": f"{anchorLevel}_{taskALevel}", "assert_value": {}, "assert_awards": {}}
            flag = [True]
            index = 0
            while any(flag):
                flag = []
                anchor = get_anchor_level_case(scene=scene, level=anchorLevel)
                # anchor["mock_scene"] = scene
                for taskKey in task_details_for_class[anchorLevel][taskALevel]:
                    if taskKey in anchor:
                        if task_details_for_class[anchorLevel][taskALevel][taskKey]:
                            anchor[taskKey] = task_details_for_class[anchorLevel][taskALevel][taskKey].pop()
                            info["assert_value"][taskKey] = anchor[taskKey]["assert_value"]
                            info["assert_awards"][taskKey] = anchor[taskKey]["assert_awards"]
                            anchor[taskKey] = anchor[taskKey]["value"]
                            # if taskKey in ["go_live_duration", "total_watch_duration", "link_micro_duration",
                            #                        "co_host_duration"]:
                            #     anchor[taskKey] *= 60
                            flag.append(task_details_for_class[anchorLevel][taskALevel][taskKey])
                        else:
                            anchor[taskKey] = 0
                            info["assert_value"][taskKey] = None
                            info["assert_awards"][taskKey] = None
                index += 1
                res.append({"info": info, "anchor": anchor})

                print(index)

    return res


if __name__ == '__main__':
    """
    周日任务case生成
    """
    cases_weekly = None
    cases_daily = None

    tasks_details_for_class = get_tasks_details_for_class()
    with open('task.json', 'w', encoding='utf-8') as f:
        json.dump({"cases": tasks_details_for_class}, f, ensure_ascii=False, indent=4)
    tasks_details_for_class_weekly = tasks_details_for_class["weekly"]
    tasks_details_for_class_daily = tasks_details_for_class["daily"]
    cases_weekly = gene_cases_for_type(tasks_details_for_class_weekly, 3)
    cases_daily = gene_cases_for_type(tasks_details_for_class_daily, 7)
    print("cases_weekly:", len(cases_weekly))
    print("cases_daily:", len(cases_daily))

    with open('cases_weekly.json', 'w', encoding='utf-8') as f:
        json.dump({"cases": cases_weekly}, f, ensure_ascii=False, indent=4)
    with open('cases_daily.json', 'w', encoding='utf-8') as f:
        json.dump({"cases": cases_daily}, f, ensure_ascii=False, indent=4)


    """
    打卡任务生成
    """
    cases_clockIn = []
    data_tasks_clockIn = DataTasksClockIn()
    data_awards_clockIn = DataAwardsClockIn()
    tasks_details_clockIn = data_tasks_clockIn.task_details
    tasks_clockIn_taskKey = set([i["task_key"] for i in tasks_details_clockIn])
    cases_clockIn = {key: [] for key in tasks_clockIn_taskKey}
    for task_detail in tasks_details_clockIn:
        tasks = data_tasks_clockIn.generate_boundary_values(task_detail)
        tasks = list({json.dumps(task, sort_keys=True) for task in tasks})
        tasks = [json.loads(task) for task in tasks]
        for task in tasks:
            anchor = get_anchor_level_case(8, task["anchor_level"])
            assert_awards = data_awards_clockIn.get_award_value(task["regin"], task["anchor_level"],
                                                                task["anchor_task_level"])
            exec(f"anchor.{task["task_key"]} = {task["value"]}")
            cases_clockIn[task["task_key"]].append({"anchor": anchor.to_dict(),
                                                    "info": {"assert_value": task["assert_value"],
                                                             "assert_awards": assert_awards}})

    with open('cases_clockIn.json', 'w', encoding='utf-8') as f:
        json.dump({"cases": cases_clockIn}, f, ensure_ascii=False, indent=4)

    print("cases_clockIn:", sum(len(value) for value in cases_clockIn.values()))