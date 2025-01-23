
from enum import IntEnum, auto, unique


class Province(IntEnum):
    """以汉字为name，auto()为value"""
    UNKNOWN = auto()
    北京 = auto()
    上海 = auto()
    广东 = auto()
    江苏 = auto()
    浙江 = auto()
    山东 = auto()
    河南 = auto()
    河北 = auto()
    四川 = auto()
    湖北 = auto()
    湖南 = auto()
    重庆 = auto()
    天津 = auto()
    安徽 = auto()
    福建 = auto()
    辽宁 = auto()
    吉林 = auto()
    黑龙江 = auto()
    山西 = auto()
    陕西 = auto()
    云南 = auto()
    贵州 = auto()
    甘肃 = auto()
    青海 = auto()
    广西 = auto()
    西藏 = auto()
    新疆 = auto()
    海南 = auto()
    宁夏 = auto()

class Year(IntEnum):
    UNKNOWN = auto()
    year_2017 = auto()
    year_2018 = auto()
    year_2019 = auto()
    year_2020 = auto()
    year_2021 = auto()
    year_2022 = auto()
    year_2023 = auto()
    year_2024 = auto()

class LevelType(IntEnum):
    "以汉字为name，auto()为value"
    国考 = auto()
    省考 = auto()
    选调 = auto()
    事业编综合应用 = auto()

class SubLevelType(IntEnum):
    副省级 = auto()
    地市级 = auto()
    行政执法 = auto()
    政法干警 = auto()
    公安 = auto()
    乡镇 = auto()
    县级 = auto()
    市级 = auto()
    甲卷 = auto()
    乙卷 = auto()
    丙卷 = auto()
    省级 = auto()
    市县级 = auto()
    A卷 = auto()
    B卷 = auto()
    C卷 = auto()
    D卷 = auto()

class QuestionOrder(IntEnum):
    UNKNOWN = -1
    order_1 = 0
    order_2 = 1
    order_3 = 2
    order_4 = 3
    order_5 = 4

class QuestionType(IntEnum):
    单一题 = auto()
    综合题 = auto()
    公文题 = auto()
    大作文 = auto()

class QuestionSubType(IntEnum):
    做法 = auto()
    影响 = auto()
    问题 = auto()
    分析 = auto()
    措施启示 = auto()
    解释 = auto()
    提纲题 = auto()
    其他题型_公文题 = auto()
    策论文_县级 = auto()
    议论文_县级 = auto()
    提出建议_乡镇 = auto()

class QuestionLabel(IntEnum):
    行政执法 = auto()
    基层治理 = auto()
    乡村振兴 = auto()
    消费 = auto()
    经济 = auto()
    城市治理 = auto()
    文化建设 = auto()
    生态环境 = auto()
    科技创新 = auto()
    新质生产力 = auto()
    人才 = auto()
    就业创业 = auto()
    数字经济 = auto()
    实体经济 = auto()
    民生 = auto()
    教育 = auto()
    健康健身 = auto()
    营商环境 = auto()
    网络治理 = auto()
    政府建设 = auto()
    调研 = auto()
    基层减负 = auto()

if __name__=="__main__":
    pass

