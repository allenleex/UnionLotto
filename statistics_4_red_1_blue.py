# -*- coding: UTF-8 -*-
import pandas as pd
import common as m

# 全局变量
CSV_OUT = "data/statistics_4_red_1_blue.csv"
ONLY_OCCURRENCE = True


# 统计4个RED在红球区出现的次数
# x 代表蓝球号码
def count_4_1_in_csv(data, a, b, c, d, x):
    # 判断RED是否在红区
    if a not in m.RED_NUMBERS or b not in m.RED_NUMBERS or c not in m.RED_NUMBERS or d not in m.RED_NUMBERS:
        return 0

    # 遍历数据集
    count = 0
    ids = []
    for line in data.itertuples():
        # 取出一行数据形成数组
        arr = [
            line[2], line[3], line[4], line[5], line[6], line[7]
        ]
        # print(arr)
        # 如果数字都在数组里，计数器+1
        if a in arr and b in arr and c in arr and d in arr and x == line[8]:
            ids.append("{:0>5d}".format(line[1]))
            count += 1

    return count, ids


# 遍历所有数据，统计组合出现次数
def count_all(data):
    a = m.MIN_RED_NUM
    arr = []

    # 嵌套循环
    while a <= m.MAX_RED_NUM:
        b = a + 1
        while b <= m.MAX_RED_NUM:
            c = b + 1
            while c <= m.MAX_RED_NUM:
                d = c + 1
                while d <= m.MAX_RED_NUM:
                    x = m.MIN_BLUE_NUM
                    while x <= m.MAX_BLUE_NUM:
                        count, ids = count_4_1_in_csv(data, a, b, c, d, x)

                        # 如果选择不显示没出现过的组合则跳过
                        if count == 0 and ONLY_OCCURRENCE:
                            x += 1
                            continue

                        ids_str = ""
                        for id in ids:
                            id = "{:0>5d}".format(int(id))
                            ids_str += id + " "
                        print_result(a, b, c, d, x, count, ids_str)
                        row = [a, b, c, d, x, count, ids_str]
                        arr.append(row)

                        x += 1
                    d += 1
                c += 1
            b += 1
        a += 1

    return arr


# 打印结果
def print_result(a, b, c, d, x, count, ids):
    print("[" + str(a) + "][" + str(b) + "][" + str(c) + "][" + str(d) + "]+[" + str(x) + "]: " + str(count) + " : " + ids)


if __name__ == '__main__':
    data = pd.read_csv(m.CSV_IN, encoding='utf-8', engine='python')
    arr = count_all(data)
    m.write_csv(CSV_OUT, arr, ["RED1", "RED2", "RED3", "RED4", "BLUE", "OCCURRENCE", "ISSUE"])
