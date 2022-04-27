# -*- coding: UTF-8 -*-
import pandas as pd
import common as m
from common import HashMap, LinkedList, Node
import numpy as np
import common as m
from sklearn.datasets import load_iris

CACHE = {}
COL_SORT = "OCCURRENCE"

# 数据文件
CSV_4_0 = "data/statistics_4_red.csv"
CSV_3_1 = "data/statistics_3_red_1_blue.csv"
CSV_4_1 = "data/statistics_4_red_1_blue.csv"
CSV_5_0 = "data/statistics_5_red.csv"
MAX_SIZE = 20

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
    # load_old_data(CSV_5_1)
    pass


# 四等奖
def fourth_prize():
    m.log("5个红球")
    load_old_data(CSV_5_0)
    m.log("4个红球 + 1个蓝球")
    load_old_data(CSV_4_1)


# 五等奖
def fifth_prize():
    m.log("4个红球")
    load_old_data(CSV_4_0)
    m.log("3个红球 + 1个蓝球")
    load_old_data(CSV_3_1)


# 打印曾经中奖的组合数据
def load_old_data(csv):
    data = pd.read_csv(csv, encoding='utf-8', engine='python')
    data = data.sort_values(by=COL_SORT, ascending=False).head(MAX_SIZE)
    print(data.to_string())
    # 写入缓存用于后续分析
    CACHE[csv] = data
    return data


# 第1步：找出概率最高的中奖组合
def step_1():
    data_4_0 = load_old_data(CSV_4_0)
    data_3_1 = load_old_data(CSV_3_1)
    m.log("推荐组合如下")

    for line in data_4_0.itertuples():
        a = line[1]
        b = line[2]
        c = line[3]
        d = line[4]
        x, y = last_2_numbers(data_4_0, line[0], a, b, c, d)
        m.print_r(a, b, c, d, x, y)

    for line in data_3_1.itertuples():
        a = line[1]
        b = line[2]
        c = line[3]
        d = line[4]
        x, y, z = last_3_numbers(data_3_1, line[0], a, b, c)
        m.print_r(a, b, c, x, y, z)


# 推荐2个红球
def last_2_numbers(data, idx, a, b, c, d):
    x = 0
    buf = np.zeros(m.MAX_RED_NUM - m.MIN_RED_NUM + 1, dtype=int, order='C')
    for line in data.itertuples():
        if line.Index != idx:
            arr = [line.RED1, line.RED2, line.RED3, line.RED4]
            i = 0
            while i <= m.MAX_RED_NUM - m.MIN_RED_NUM:
                if i != a and i != b and i != c and i != d and i in arr:
                    buf[i] = int(buf[i] + 1)
                i += 1
    x = np.argmax(buf)

    y = 0
    buf = np.zeros(m.MAX_RED_NUM - m.MIN_RED_NUM + 1, dtype=int, order='C')
    for line in data.itertuples():
        if line.Index != idx:
            arr = [line.RED1, line.RED2, line.RED3, line.RED4]
            i = 0
            while i <= m.MAX_RED_NUM - m.MIN_RED_NUM:
                if i != a and i != b and i != c and i != d and i != x and i in arr:
                    buf[i] = int(buf[i] + 1)
                i += 1
    y = np.argmax(buf)

    return x, y


def last_3_numbers(data, idx, a, b, c):
    x = 0
    buf = np.zeros(m.MAX_RED_NUM - m.MIN_RED_NUM + 1, dtype=int, order='C')
    for line in data.itertuples():
        if line.Index != idx:
            arr = [line.RED1, line.RED2, line.RED3]
            i = 0
            while i <= m.MAX_RED_NUM - m.MIN_RED_NUM:
                if i != a and i != b and i != c and i in arr:
                    buf[i] = int(buf[i] + 1)
                i += 1
    x = np.argmax(buf)

    y = 0
    buf = np.zeros(m.MAX_RED_NUM - m.MIN_RED_NUM + 1, dtype=int, order='C')
    for line in data.itertuples():
        if line.Index != idx:
            arr = [line.RED1, line.RED2, line.RED3]
            i = 0
            while i <= m.MAX_RED_NUM - m.MIN_RED_NUM:
                if i != a and i != b and i != c and i != x and i in arr:
                    buf[i] = int(buf[i] + 1)
                i += 1
    y = np.argmax(buf)

    z = 0
    buf = np.zeros(m.MAX_RED_NUM - m.MIN_RED_NUM + 1, dtype=int, order='C')
    for line in data.itertuples():
        if line.Index != idx:
            arr = [line.RED1, line.RED2, line.RED3]
            i = 0
            while i <= m.MAX_RED_NUM - m.MIN_RED_NUM:
                if i != a and i != b and i != c and i != x and i in arr:
                    buf[i] = int(buf[i] + 1)
                i += 1
    z = np.argmax(buf)

    return x, y, z


def blue_ball():

    pass


if __name__ == '__main__':
    m.log("彩票有风险 投资请谨慎")

    try:
        step_1()
    except Exception as ex:
        print(ex)

    m.log("推荐完毕 谋事在人 成事在天 一切随缘")
