# -*- coding: UTF-8 -*-
import pandas as pd
import csv

# 全局变量
CSV_IN = "data.csv"
CSV_OUT = "statistics_6_red.csv"
MIN_RED_NUM = 1
MAX_RED_NUM = 33
MIN_BLUE_NUM = 1
MAX_BLUE_NUM = 16
RED_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
               12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
               23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
BLUE_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
ONLY_OCCURRENCE = True


# 统计4个RED在红球区出现的次数
def count_6_in_csv(data, a, b, c, d, e, f):
    # 判断RED是否在红区
    if a not in RED_NUMBERS or b not in RED_NUMBERS or c not in RED_NUMBERS \
            or d not in RED_NUMBERS or e not in RED_NUMBERS or f not in RED_NUMBERS:
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
        if a in arr and b in arr and c in arr and d in arr and e in arr and f in arr:
            ids.append("{:0>5d}".format(line[1]))
            count += 1

    return count, ids


# 遍历所有数据，统计组合出现次数
def count_all(data):
    a = MIN_RED_NUM
    b = MIN_RED_NUM
    c = MIN_RED_NUM
    d = MIN_RED_NUM
    e = MIN_RED_NUM
    f = MIN_RED_NUM
    arr = []

    # 嵌套循环
    while a <= MAX_RED_NUM:
        b = a + 1
        while b <= MAX_RED_NUM:
            c = b + 1
            while c <= MAX_RED_NUM:
                d = c + 1
                while d <= MAX_RED_NUM:
                    e = d + 1
                    while e <= MAX_RED_NUM:
                        f = e + 1
                        while f <= MAX_RED_NUM:
                            count, ids = count_6_in_csv(data, a, b, c, d, e, f)

                            # 如果选择不显示没出现过的组合则跳过
                            if count == 0 and ONLY_OCCURRENCE:
                                f += 1
                                continue

                            ids_str = ""
                            for id in ids:
                                id = "{:0>5d}".format(int(id))
                                ids_str += id + " "
                            print_result(a, b, c, d, e, f, count, ids_str)
                            row = [a, b, c, d, e, f, count, ids_str]
                            arr.append(row)

                            f += 1
                        e += 1
                    d += 1
                c += 1
            b += 1
        a += 1

    return arr


# 打印结果
def print_result(a, b, c, d, e, f, count, ids):
    print(
        "[" + str(a) + "][" + str(b) + "][" + str(c) + "]["
        + str(d) + "][" + str(e) + "][" + str(f) + "]: "
        + str(count) + " : " + ids)


# 写入csv文件
def write_csv(arr):
    f = open(CSV_OUT, 'w', encoding='utf-8', newline='')
    cw = csv.writer(f)
    cw.writerow(["RED1", "RED2", "RED3", "RED4", "RED5", "RED6", "OCCURRENCE", "ISSUE"])

    for row in arr:
        cw.writerow(row)

    f.close()
    log("写入CSV完成")


# 打印日志
def log(msg):
    print("=== " + msg + " ===")


if __name__ == '__main__':
    data = pd.read_csv(CSV_IN, encoding='utf-8', engine='python')
    arr = count_all(data)
    write_csv(arr)
