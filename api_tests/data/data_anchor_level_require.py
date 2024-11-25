import copy
import random

anchor_level_requires = {
    "1": [
        {
            "level": 1,
            'regin': '',
            'Last7DayAvgAcu': [0, 0],
            'Last1DayFansCnt': [0, 3000 - 1],
            'Last7DayWatchTotalDuration': [0, 20 * 60 - 1],
            'Last30DayIncome': [0, 0],
            'Last7DayIncome': [0, 0],
            'condition': 'and'
        }
    ],
    "2": [
        {
            "level": 2,
            'regin': '',
            'Last7DayAvgAcu': [0, 1],
            'Last1DayFansCnt': [3 * 1000, 10 * 1000 - 1],
            'Last7DayWatchTotalDuration': [20 * 60, 999999999],
            'Last30DayIncome': [1, 3000 - 1],
            'Last7DayIncome': [1, 1000 - 1],
            'condition': 'or'
        }
    ],
    "3": [
        {
            "level": 3,
            'regin': 'US',
            'Last7DayAvgAcu': [2, 2],
            'Last1DayFansCnt': [5 * 1000, 10 * 1000 - 1],
            'Last7DayWatchTotalDuration': [0],
            'Last30DayIncome': [3 * 1000, 20 * 1000 - 1],
            'Last7DayIncome': [1 * 1000, 5 * 1000 - 1],
            'condition': 'or'
        },
        {
            "level": 3,
            'regin': 'JP',
            'Last7DayAvgAcu': [2, 2],
            'Last1DayFansCnt': [5 * 1000, 10 * 1000 - 1],
            'Last7DayWatchTotalDuration': [0],
            'Last30DayIncome': [3 * 1000, 20 * 1000 - 1],
            'Last7DayIncome': [1 * 1000, 5 * 1000 - 1],
            'condition': 'or'
        },
        {
            "level": 3,
            'regin': '',
            'Last7DayAvgAcu': [2, 2],
            'Last1DayFansCnt': [5 * 1000, 10 * 1000 - 1],
            'Last7DayWatchTotalDuration': [0],
            'Last30DayIncome': [3 * 1000, int(7.5 * 1000 - 1)],
            'Last7DayIncome': [1 * 1000, 2 * 1000 - 1],
            'condition': 'or'
        }
    ],
    "4": [
        {
            "level": 4,
            'regin': 'US',
            'Last7DayAvgAcu': [3, 4],
            'Last1DayFansCnt': [10 * 1000, 15 * 1000 - 1],
            'Last7DayWatchTotalDuration': [0],
            'Last30DayIncome': [20 * 1000, 40 * 1000 - 1],
            'Last7DayIncome': [5 * 1000, 10 * 1000 - 1],
            'condition': 'or'
        },
        {
            "level": 4,
            'regin': 'JP',
            'Last7DayAvgAcu': [3, 4],
            'Last1DayFansCnt': [10 * 1000, 15 * 1000 - 1],
            'Last7DayWatchTotalDuration': [0],
            'Last30DayIncome': [20 * 1000, 40 * 1000 - 1],
            'Last7DayIncome': [5 * 1000, 10 * 1000 - 1],
            'condition': 'or'
        },
        {
            "level": 4,
            'regin': '',
            'Last7DayAvgAcu': [3, 4],
            'Last1DayFansCnt': [10 * 1000, 15 * 1000 - 1],
            'Last7DayWatchTotalDuration': [0],
            'Last30DayIncome': [int(7.5 * 1000), 15 * 1000 - 1],
            'Last7DayIncome': [2 * 1000, 4 * 1000 - 1],
            'condition': 'or'
        }
    ],
    "5": [
        {
            "level": 5,
            'regin': 'US',
            'Last7DayAvgAcu': [5, 29],
            'Last1DayFansCnt': [15 * 1000, 35 * 1000 - 1],
            'Last7DayWatchTotalDuration': [0],
            'Last30DayIncome': [40 * 1000, 600 * 1000 - 1],
            'Last7DayIncome': [10 * 1000, 150 * 1000 - 1],
            'condition': 'or'
        },
        {
            "level": 5,
            'regin': 'JP',
            'Last7DayAvgAcu': [5, 29],
            'Last1DayFansCnt': [15 * 1000, 35 * 1000 - 1],
            'Last7DayWatchTotalDuration': [20 * 60, 999999999],
            'Last30DayIncome': [40 * 1000, 200 * 1000 - 1],
            'Last7DayIncome': [10 * 1000, 50 * 1000 - 1],
            'condition': 'or'
        },
        {
            "level": 5,
            'regin': '',
            'Last7DayAvgAcu': [5, 29],
            'Last1DayFansCnt': [15 * 1000, 35 * 1000 - 1],
            'Last7DayWatchTotalDuration': [0],
            'Last30DayIncome': [15 * 1000, 150 * 1000 - 1],
            'Last7DayIncome': [4 * 1000, 40 * 1000 - 1],
            'condition': 'or'
        }
    ],
    "6": [
        {
            "level": 6,
            'regin': 'US',
            'Last7DayAvgAcu': [30, 999999999],
            'Last1DayFansCnt': [35 * 1000, 999999999],
            'Last7DayWatchTotalDuration': [0],
            'Last30DayIncome': [600 * 1000, 999999999],
            'Last7DayIncome': [150 * 1000, 999999999],
            'condition': 'or'
        },
        {
            "level": 6,
            'regin': 'JP',
            'Last7DayAvgAcu': [30, 999999999],
            'Last1DayFansCnt': [35 * 1000, 999999999],
            'Last7DayWatchTotalDuration': [0],
            'Last30DayIncome': [200 * 1000, 999999999],
            'Last7DayIncome': [50 * 1000, 999999999],
            'condition': 'or'
        },
        {
            "level": 6,
            'regin': '',
            'Last7DayAvgAcu': [30, 999999999],
            'Last1DayFansCnt': [35 * 1000, 999999999],
            'Last7DayWatchTotalDuration': [0],
            'Last30DayIncome': [150 * 1000, 999999999],
            'Last7DayIncome': [40 * 1000, 999999999],
            'condition': 'or'
        }
    ]
}
indicator = ["Last7DayAvgAcu", "Last1DayFansCnt", "Last7DayWatchTotalDuration", "Last30DayIncome",
             "Last7DayIncome"]


def get_level_for_data(data):
    level = 0
    regin = data['regin']
    for anchor_level_require in anchor_level_requires.values():
        flag = []

        require = [i for i in anchor_level_require if i['regin'] == regin]
        if len(require) == 0:
            regin = ""
            require = [i for i in anchor_level_require if i['regin'] == regin][0]
        else:
            require = require[0]
        condition = all if require["condition"] == "and" else any
        # print(f"---------{require["level"]}---------")
        for k, v in require.items():
            if k in indicator:
                if len(v) <= 1:
                    pass
                else:
                    flag.append(all([data[k] >= v[0], data[k] <= v[1]]))
                    # print(f"{data[k]} >= {v[0]}, {data[k]} <= {v[1]}, {flag}")
        if condition == all:
            if condition(flag):
                level = require["level"]
                return level
        else:
            if condition(flag):
                level = require["level"]
                # print(f"{condition(flag), flag}")
    return level


def generate_boundary_values(level: str, regin: str = ""):
    boundary_value = []

    def set_boundary_value(item):
        value_template = {}
        values = []
        for k, v in item.items():
            if k in indicator:
                value_template[k] = v[0]
            else:
                value_template[k] = v

        def do_set(key, value):
            t = copy.copy(value_template)
            t[key] = value
            values.append(t)

        for k, v in item.items():
            if k in indicator:
                vl = v[0]
                do_set(k, vl)
                vl = v[1] if len(v) > 1 else v[0]
                do_set(k, vl)
                vl = v[0] - 1 if v[0] > 0 else 0
                do_set(k, vl)
                vl = v[1] + 1 if len(v) > 1 else v[0]
                do_set(k, vl)

                if len(v) == 1 and v == 0:
                    # 任意
                    vl = random.randint(0, 1000000)
                    do_set(k, vl)

        return [dict(t) for t in {tuple(d.items()) for d in values}]


    for item in [i for i in anchor_level_requires[level] if i["regin"] == regin]:
        if regin.lower() == item['regin'].lower():
            boundary_value += set_boundary_value(item)
    if not boundary_value:
        boundary_value += set_boundary_value([i for i in anchor_level_requires[level] if i["regin"] == ""][0])
    res = []
    for i in boundary_value:
        i["level"] = get_level_for_data(i)
        res.append(i)
    return res


def generate_data_for_level(level: str, regin=""):
    datas = []
    for i in range(1, len(anchor_level_requires) + 1):
        datas += [data for data in generate_boundary_values(str(i)) if data["level"] == int(level)]
    return datas


if __name__ == '__main__':
        # t = generate_data_for_level(str(5))
        t = get_level_for_data({'level': 5, 'regin': '', 'Last7DayAvgAcu': 3, 'Last1DayFansCnt': 5000, 'Last7DayWatchTotalDuration': 0, 'Last30DayIncome': 3000, 'Last7DayIncome': 1000, 'condition': 'or'})
        print(t)

