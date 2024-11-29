import datetime
import json
import random

from api_tests.data.data_anchor_level_require import generate_data_for_level
from api_tests.data.data_awards import DataAwards
from api_tests.data.data_tasks import DataTasks


class AnchorData:
    def __init__(self, data=None):
        data = data or {}
        self.i1 = data.get("1", 0)
        self.i2 = data.get("2", 0)
        self.i3 = data.get("3", 0)
        self.i4 = data.get("4", 0)
        self.i5 = data.get("5", 0)

    def to_dict(self):
        anchor_dict = self.__dict__.copy()
        anchor_dict["1"] = anchor_dict.pop("i1")
        anchor_dict["2"] = anchor_dict.pop("i2")
        anchor_dict["3"] = anchor_dict.pop("i3")
        anchor_dict["4"] = anchor_dict.pop("i4")
        anchor_dict["5"] = anchor_dict.pop("i5")

        return anchor_dict


class AnchorWeeklyData(AnchorData):
    def __init__(self, data=None):
        super().__init__(data)
        data = data or {}
        self.mock_scene = 3
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


class AnchorDailyData(AnchorData):
    def __init__(self, data=None):
        super().__init__(data)
        data = data or {}
        self.mock_scene = 7
        self.go_live_duration = data.get("go_live_duration", 0)
        self.total_watch_duration = data.get("total_watch_duration", 0)
        self.gain_diamond_count = data.get("gain_diamond_count", 0)
        self.increase_fans_count = data.get("increase_fans_count", 0)
        self.increase_subscription_count = data.get("increase_subscription_count", 0)
        self.live_like_count = data.get("live_like_count", 0)
        self.live_comment_count = data.get("live_comment_count", 0)


class AnchorClockInData(AnchorData):
    def __init__(self, data=None):
        super().__init__(data)
        data = data or {}
        self.mock_scene = 8
        self.clock_in_task_go_live_duration = data.get("clock_in_task_go_live_duration", (0, 0))
        self.clock_in_task_total_watch_duration = data.get("clock_in_task_total_watch_duration", (0, 0))
        self.clock_in_task_gain_diamond_count = data.get("clock_in_task_gain_diamond_count", (0, 0))

    def to_dict(self):
        anchor_dict = super().to_dict()

        anchor_dict[f"clock_in_task:go_live_duration:{self.clock_in_task_go_live_duration[1]}"] = \
            self.clock_in_task_go_live_duration[0]
        anchor_dict[f"clock_in_task:total_watch_duration:{self.clock_in_task_total_watch_duration[1]}"] = \
            self.clock_in_task_total_watch_duration[0]
        anchor_dict[f"clock_in_task:gain_diamond_count:{self.clock_in_task_gain_diamond_count[1]}"] = \
            self.clock_in_task_gain_diamond_count[0]
        anchor_dict.pop("clock_in_task_go_live_duration")
        anchor_dict.pop("clock_in_task_total_watch_duration")
        anchor_dict.pop("clock_in_task_gain_diamond_count")

        return anchor_dict


def get_data(scene):
    case_no_1 = str(int(datetime.datetime.now().timestamp()))
    case_no_2 = 0
    cases = []
    data_tasks = DataTasks()
    data_awards = DataAwards()

    task_cases = []
    for task in data_tasks.task_details:
        for task_case in data_tasks.generate_boundary_values(task):
            task_case["award_value"] = data_awards.get_award_value(task_type=task_case["task_type"],
                                                                   task_level=task_case["anchor_task_level"],
                                                                   anchor_level=task_case["anchor_level"])
            if task_case["task_key"] in ["go_live_duration", "total_watch_duration", "link_micro_duration",
                                         "co_host_duration"]:
                task_case["value_format"] = task_case["value"] * 60
                task_case["assert_value_format"] = task_case["assert_value"] * 60
            task_cases.append(task_case)
    print(len(task_cases))

    def get_anchor_level_case(level, regin=""):

        level_cases = generate_data_for_level(str(level), regin=regin)

        level_case = level_cases[random.randint(0, len(level_cases) - 1)]
        anchor_data = AnchorWeeklyData()
        anchor_data.i1 = level_case["Last7DayAvgAcu"]
        anchor_data.i2 = level_case["Last1DayFansCnt"]
        anchor_data.i3 = level_case["Last7DayWatchTotalDuration"]
        anchor_data.i4 = level_case["Last30DayIncome"]
        anchor_data.i5 = level_case["Last7DayIncome"]
        anchor_data.mock_scene = scene
        return {"level_case": level_case, "anchor_case": anchor_data.to_dict()}

    if scene == 3:
        for task_case in task_cases:
            if task_case["task_type"] == "weekly":
                case_no_2 += 1
                anchor_level_case = get_anchor_level_case(task_case["anchor_level"])
                task_case_value = task_case["value"]
                if task_case["task_key"] in ["go_live_duration", "total_watch_duration", "link_micro_duration",
                                             "co_host_duration"]:
                    task_case_value *= 60
                anchor_level_case["anchor_case"][task_case["task_key"]] = task_case_value
                cases.append({"case_no": f"{case_no_1}_{case_no_2:04d}", "task_case": task_case,
                              "anchor_case": anchor_level_case})
    return cases


if __name__ == "__main__":
    cases = get_data(3)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump({"cases": cases}, f, ensure_ascii=False, indent=4)
