# -*- coding: UTF-8 -*-
import pandas as pd
import common as m
import numpy
import common as m
from sklearn.datasets import load_iris

CACHE = {}
COL_SORT = "OCCURRENCE"

# 数据文件
CSV_4_0 = "data/statistics_4_red.csv"
CSV_3_1 = "data/statistics_3_red_1_blue.csv"
CSV_4_1 = "data/statistics_4_red_1_blue.csv"
CSV_5_0 = "data/statistics_5_red.csv"
MAX_SIZE = 30

#

# 五等奖
# 四等奖


# 一等奖
def first_prize():
    pass


# 二等奖
def second_prize():
    pass


# 三等奖
def third_prize():
    m.log("5个红球 + 1个蓝球")
    # print_old_data(CSV_5_1)
    pass


# 四等奖
def fourth_prize():
    m.log("5个红球")
    print_old_data(CSV_5_0)
    m.log("4个红球 + 1个蓝球")
    print_old_data(CSV_4_1)


# 五等奖
def fifth_prize():
    m.log("4个红球")
    print_old_data(CSV_4_0)
    m.log("3个红球 + 1个蓝球")
    print_old_data(CSV_3_1)


# 打印曾经中奖的组合数据
def print_old_data(csv):
    data = pd.read_csv(csv, encoding='utf-8', engine='python')
    data = data.sort_values(by=COL_SORT, ascending=False).head(MAX_SIZE)
    print(data.to_string())
    # 写入缓存用于后续分析
    CACHE[csv] = data


# 第1步：找出概率最高的中奖组合
def step_1():
    fifth_prize()
    fourth_prize()


# 第2步：
def step_2():
    pass


if __name__ == '__main__':
    m.log("彩票有风险 投资请谨慎")

    try:
        step_1()
    except Exception as ex:
        print(ex)

    m.log("推荐完毕 谋事在人 成事在天 一切随缘")
