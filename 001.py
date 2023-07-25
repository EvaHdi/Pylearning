"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 001.py
@Author : hongbo.zhang
@Time : 2023/7/24 10:16

利用random 库实现如下功能
a) 有一个字符串  testStr = 'AaBbCcDdEeFfGgHhIiJjKkLlMmnOoPpQqRrSsTtUuVvWwXxYyZz'，实现一个函数 randpick：
使用random随机库里的函数，生成一个由任意6个字符组成子字符串，并显示在屏幕上；
要求randpick 每被调用五次生成相同字符串，即第1次随机产生，
第5,10.次调用生成相同字符串（不能用保存第一次结果赋值的方式实现），其他情况随机生成字符串内容
b) 生成一个[10, 100]之间以3为步长的随机整数列表
c) 将上述序列随机打乱，生成一个随机列表

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