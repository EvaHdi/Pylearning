"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 004.py
@Author : hongbo.zhang
@Time : 2023/7/27 13:32

移除无效的括号
给你一个由 '('、')' 和小写字母组成的字符串 s。
你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。
请返回任意一个合法字符串。
有效「括号字符串」应当符合以下 任意一条 要求：
空字符串或只包含小写字母的字符串
可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」

示例 1：
输入：s = "a)b(c)d"
输出："ab(c)d"
示例 2：
输入：s = "))(("
输出：""
解释：空字符串也是有效的
"""


def remove(s):
    stack = []
    indices_to_remove = []

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                indices_to_remove.append(i)

    # 合并需要删除的左右括号的索引
    indices_to_remove += stack

    # 构造新字符串
    res = ""
    for i in range(len(s)):
        if i not in indices_to_remove:
            res += s[i]

    return res


if __name__ == '__main__':

    s = "a)b(c)d"

    print('"' + remove(s) + '"')

    s = "))(("
    print('"' + remove(s) + '"')
