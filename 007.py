"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 007.py
@Author : hongbo.zhang
@Time : 2023/8/1 10:09

轮转数组
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
"""
from collections import deque


def rotation(list, k):
    list = deque(list)  # 使用双向队列，先得到真实的轮换值，再将右侧弹出的数从左侧添加即可
    for i in range(k % len(list)):
        list.appendleft(list.pop())
    return list

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotation(nums, k))

    nums = [-1, -100, 3, 99]
    k = 2
    print(rotation(nums, k))