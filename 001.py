"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 001.py
@Author : hongbo.zhang
@Time : 2023/7/24 10:16
"""

import random

counter = 1
def randpick():
    testStr = 'AaBbCcDdEeFfGgHhIiJjKkLlMmnOoPpQqRrSsTtUuVvWwXxYyZz'
    global counter
    if counter % 5 == 0 or counter == 1:
        random.seed(10)
    else:
        random.seed()

    res = ''.join(random.choices(testStr, k=6))

    counter += 1
    print(res)

def randnum():
    start = 10
    end = 100
    step = 3
    # 计算可能的元素数量
    num_elements = (end - start) // step + 1

    # 使用 random.sample 函数生成随机数组
    random_list = random.sample(list(range(10, 101, 3)), num_elements)
    return random_list

def randlist(random_list):
    random.shuffle(random_list)
    print(random_list)

if __name__ == '__main__':

    # (a)
    """for _ in range(10):
        randpick()"""

    # (b)
    random_list = randnum()
    print(random_list)

    # (c)
    randlist(random_list)