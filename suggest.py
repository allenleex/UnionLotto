# -*- coding: UTF-8 -*-
import pandas as pd
import common as m
import numpy
import common as m

COL_RANK = "OCCURRENCE_RANK"
# 数据文件
# 五等奖
CSV_4_0 = "data/statistics_4_red.csv"
CSV_3_1 = "data/statistics_3_red_1_blue.csv"


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
    pass


# 五等奖
def fifth_prize():
    m.log("五等奖 推荐组合")

    # data = pd.read_csv(CSV_4_0, encoding='utf-8', engine='python')
    # data[COL_RANK] = data['OCCURRENCE'].rank(method='first', ascending=False)
    # data.sort_values(COL_RANK, inplace=True)
    # print(data)

    pass


if __name__ == '__main__':
    m.log("彩票有风险 投资请谨慎")

    try:
        fifth_prize()
    except Exception as ex:
        print(ex)

    m.log("推荐完毕")
