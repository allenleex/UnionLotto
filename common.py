# -*- coding: UTF-8 -*-
import csv
import random

# 全局变量
CSV_IN = "data/data.csv"
MIN_RED_NUM = 1
MAX_RED_NUM = 33
MIN_BLUE_NUM = 1
MAX_BLUE_NUM = 16
RED_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
               12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
               23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
COL_NAME_RED = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
                "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22",
                "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33"]
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
    print("")
    print("=== " + msg + " ===")
    print("")


def print_r(a, b, c, d, e, f):
    print("{:0>2d}".format(a), "{:0>2d}".format(b), "{:0>2d}".format(c),
          "{:0>2d}".format(d), "{:0>2d}".format(e), "{:0>2d}".format(f))


class Node:
    def __init__(self, key, val, prev=None, succ=None):
        self.key = key
        self.val = val
        # 前驱
        self.prev = prev
        # 后继
        self.succ = succ

    def __repr__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head = Node(None, 'header')
        self.tail = Node(None, 'tail')
        self.head.succ = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.str = ""

    def append(self, node):
        # 将node节点添加在链表尾部
        prev = self.tail.prev
        node.prev = prev
        node.succ = prev.succ
        prev.succ = node
        node.succ.prev = node
        self.size += 1

    def delete(self, node):
        # 删除节点
        prev = node.prev
        succ = node.succ
        succ.prev, prev.succ = prev, succ
        self.size -= 1

    def get_list(self):
        # 返回一个包含所有节点的list，方便上游遍历
        ret = []
        cur = self.head.succ
        while cur != self.tail:
            ret.append(cur)
            cur = cur.succ
        return ret

    def get_by_key(self, key):
        cur = self.head.succ
        while cur != self.tail:
            if cur.key == key:
                return cur
            cur = cur.succ
        return None

    # def to_string(self):
    #     for node in self.get_list():
    #         self.str += str(node.key) + '\t'
    #     self.str += "\n"
    #     for node in self.get_list():
    #         self.str += str(node.val) + '\n'
    #
    #     return self.str


class HashMap:
    def __init__(self, capacity=1, load_factor=1):
        self.capacity = capacity
        self.load_factor = load_factor
        self.headers = [LinkedList() for _ in range(capacity)]
        self.str = ""

    def get_hash_key(self, key):
        return hash(key) & (self.capacity - 1)

    def put(self, key, val):
        hash_key = self.get_hash_key(key)
        linked_list = self.headers[hash_key]
        if linked_list.size >= self.load_factor * self.capacity:
            self.reset()
            hash_key = self.get_hash_key(key)
            linked_list = self.headers[hash_key]
        node = linked_list.get_by_key(key)
        if node is not None:
            node.val = val
        else:
            node = Node(key, val)
            linked_list.append(node)

    def get(self, key):
        hash_key = self.get_hash_key(key)
        linked_list = self.headers[hash_key]
        node = linked_list.get_by_key(key)
        return node.val if node is not None else None

    def delete(self, key):
        node = self.get(key)
        if node is None:
            return False
        hash_key = self.get_hash_key(key)
        linked_list = self.headers[hash_key]
        linked_list.delete(node)
        return True

    def reset(self):
        headers = [LinkedList() for _ in range(self.capacity * 2)]
        cap = self.capacity
        self.capacity = self.capacity * 2
        for i in range(cap):
            linked_list = self.headers[i]
            nodes = linked_list.get_list()
            for u in nodes:
                hash_key = self.get_hash_key(u.key)
                head = headers[hash_key]
                head.append(u)
        self.headers = headers
        self.str = ""

    def to_string(self):
        for list in self.headers:
            for node in list.get_list():
                self.str += str(node.key) + ":" + str(node.val) + "  "

        return self.str

    def sort(self):

        pass
