"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 009.py
@Author : hongbo.zhang
@Time : 2023/8/3 9:50

最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：
对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：
输入：s = "a", t = "a"
输出："a"
示例 3:
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
"""
import collections


def strmatch(s, t) -> str:
    i = 0  # 采用滑动窗口的方法
    res = (0, float('inf'))  # float('inf')表示正无穷大
    need = collections.defaultdict(int)  # 在访问一个不存在的键时会返回默认值0,同时自动将不存在的键创建进字典
    for c in t:
        need[c] += 1
    needcnt = len(t)  # 维护一个所需元素
    for j, c in enumerate(s):
        if need[c] > 0:
            needcnt -= 1
        need[c] -= 1
        if needcnt == 0:
            while True:
                c = s[i]  # 从头开始找匹配子串内容的字符，找到就弹出去
                if need[c] == 0:
                    break
                i += 1
                need[c] += 1
            if j - i < res[1] - res[0]:  # 记录结果
                res = (i, j)
            need[s[i]] += 1  # 步骤三：寻找新的满足条件滑动窗口，最先找到的那个子串字符要记录，所以在need里必须更新+1
            i += 1
            needcnt += 1

    return "''" if res[1] > len(s) else s[res[0]:res[1] + 1]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(strmatch(s, t))

    s = "a"
    t = "a"
    print(strmatch(s, t))

    s = "a"
    t = "aa"
    print(strmatch(s, t))