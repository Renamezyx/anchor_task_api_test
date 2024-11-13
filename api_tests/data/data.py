import random
from enum import Enum

from api_tests.data.data_anchor_level_require import generate_boundary_values
from api_tests.data.data_awards import DataAwards
from api_tests.data.data_tasks import DataTasks


class AnchorWeeklyData:
    def __init__(self, data=None):
        data = data or {}
        self.level_1 = data.get("1", 0)
        self.level_2 = data.get("2", 0)
        self.level_3 = data.get("3", 0)
        self.level_4 = data.get("4", 0)
        self.level_5 = data.get("5", 0)
        self.mock_scene = data.get("mock_scene", 0)
        self.go_live_duration = data.get("go_live_duration", 0)
        self.total_watch_duration = data.get("total_watch_duration", 0)
        self.gain_diamond_count = data.get("gain_diamond_count", 0)
        self.increase_fans_count = data.get("increase_fans_count", 0)
        self.go_live_valid_day = data.get("go_live_valid_day", 0)

        self.increase_subscription_count = data.get("increase_subscription_count", 0)
        self.live_like_count = data.get("live_like_count", 0)

        self.live_room_acu = data.get("live_room_acu", 0)
        self.link_micro_duration = data.get("link_micro_duration", 0)
        self.increase_video_item_publish_count = data.get("increase_video_item_publish_count", 0)
        self.co_host_duration = data.get("co_host_duration", 0)
        self.pk_victory = data.get("pk_victory", 0)

        self.live_comment_count = data.get("live_comment_count", 0)

    def to_dict(self):
        anchor_dict = self.__dict__
        anchor_dict["1"] = anchor_dict.pop("level_1")
        anchor_dict["2"] = anchor_dict.pop("level_2")
        anchor_dict["3"] = anchor_dict.pop("level_3")
        anchor_dict["4"] = anchor_dict.pop("level_4")
        anchor_dict["5"] = anchor_dict.pop("level_5")
        return anchor_dict


def get_data(scene):
    cases = []
    data_tasks = DataTasks()
    data_awards = DataAwards()

    task_cases = []
    for task in data_tasks.task_details:
        for task_case in data_tasks.generate_boundary_values(task):
            task_case["award_value"] = data_awards.get_award_value(task_type=task_case["task_type"],
                                                                   task_level=task_case["anchor_task_level"],
                                                                   anchor_level=task_case["anchor_level"])

            task_cases.append(task_case)

    anchor_level_cases = []
    if scene == 4:

        for i in range(1, 7):
            level_cases = generate_boundary_values(i) + generate_boundary_values(i, "US") + generate_boundary_values(i,
                                                                                                                     "JP")
            level_case = level_cases[random.randint(0, len(level_cases) - 1)]
            anchor_data = AnchorWeeklyData()
            anchor_data.level_1 = level_case["Last7DayAvgAcu"]
            anchor_data.level_2 = level_case["Last1DayFansCnt"]
            anchor_data.level_3 = level_case["Last7DayWatchTotalDuration"]
            anchor_data.level_4 = level_case["Last30DayIncome"]
            anchor_data.level_5 = level_case["Last7DayIncome"]
            anchor_data.mock_scene = scene
            anchor_level_cases.append(anchor_data.to_dict())

        for anchor_level_case in anchor_level_cases:
            for task_case in task_cases:
                case = task_case
                if task_case["task_type"] == "weekly":
                    if anchor_level_case["level"] == task_case["anchor_level"]:
                        anchor_level_case[task_case["task_key"]] = task_case["value"]
                        cases.append(case)
    return cases


if __name__ == "__main__":
    cases = get_data(4)
    for i in cases:
        print(i)
