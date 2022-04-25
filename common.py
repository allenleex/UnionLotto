# -*- coding: UTF-8 -*-
import csv


# 全局变量
CSV_IN = "data/data.csv"
MIN_RED_NUM = 1
MAX_RED_NUM = 33
MIN_BLUE_NUM = 1
MAX_BLUE_NUM = 16
RED_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
               12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
               23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
BLUE_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# 写入csv文件
def write_csv(fp, arr, header):
    f = open(fp, 'w', encoding='utf-8', newline='')
    cw = csv.writer(f)
    cw.writerow(header)

    for row in arr:
        cw.writerow(row)

    f.close()
    log("写入CSV完成")


# 打印日志
def log(msg):
    print("=== " + msg + " ===")


def print_arr(arr):
    for row in arr:
        pass
