# -*- coding: UTF-8 -*-
import pandas as pd
import common as m
import numpy
import common as m
from sklearn.datasets import load_iris

COL_SORT = "OCCURRENCE"
# 数据文件
# 五等奖
CSV_4_0 = "data/statistics_4_red.csv"
CSV_3_1 = "data/statistics_3_red_1_blue.csv"
# 四等奖
CSV_4_1 = "data/statistics_4_red_1_blue.csv"
CSV_5_0 = "data/statistics_5_red.csv"
MAX_SIZE = 10


# 一等奖
def first_prize():
    pass


# 二等奖
def second_prize():
    pass


# 三等奖
def third_prize():
    pass


# 四等奖
def fourth_prize():
    m.log("四等奖 推荐组合")

    m.log("5个红球")
    data = pd.read_csv(CSV_5_0, encoding='utf-8', engine='python')
    data = data.sort_values(by=COL_SORT, ascending=False).head(MAX_SIZE)
    print(data.to_string())

    m.log("4个红球 + 1个蓝球")
    data = pd.read_csv(CSV_4_1, encoding='utf-8', engine='python')
    data = data.sort_values(by=COL_SORT, ascending=False).head(MAX_SIZE)
    print(data.to_string())


# 五等奖
def fifth_prize():
    m.log("五等奖 推荐组合")

    m.log("4个红球")
    data = pd.read_csv(CSV_4_0, encoding='utf-8', engine='python')
    data = data.sort_values(by=COL_SORT, ascending=False).head(MAX_SIZE)
    print(data.to_string())

    m.log("3个红球 + 1个蓝球")
    data = pd.read_csv(CSV_3_1, encoding='utf-8', engine='python')
    data = data.sort_values(by=COL_SORT, ascending=False).head(MAX_SIZE)
    print(data.to_string())


if __name__ == '__main__':
    m.log("彩票有风险 投资请谨慎")

    try:
        fifth_prize()
        fourth_prize()
    except Exception as ex:
        print(ex)

    m.log("推荐完毕")
