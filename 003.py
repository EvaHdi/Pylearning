
"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 003.py
@Author : hongbo.zhang
@Time : 2023/7/26 10:48

复原 IP 地址
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。
你不能重新排序或删除 s 中的任何数字。你可以按任何顺序返回答案。

示例 1：
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：
输入：s = "0000"
输出：["0.0.0.0"]
示例 3：
输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

"""
res = []

def restore_ip(s):
    global res  # 代表引用全局变量
    res = []
    try:
        backtrack(s, [], 0)
    except ValueError:
        print("无效的IP地址")
    return res


def backtrack(s, path, segments):
    # 如果字符串s已经为空且segments为4，表示已经找到一个有效的IP地址
    if not s and segments == 4:
        res.append('.'.join(path))
    # 剩余的字符数不足以形成有效的IP地址，或者剩余的字符数过多不能凑齐4个段
    elif len(s) > (4 - segments) * 3 or len(s) < 4 - segments:
        return
        #raise ValueError  # 主动引发异常，而不是return一个空的列表
    else:
        # 每个段最多有三个数字
        for i in range(min(3, len(s))):
            segment = s[:i + 1]
            # 剪枝操作，排除掉前导零和大于255的数字
            if segment[0] == '0' and len(segment) > 1 or int(segment) > 255:
                continue
            backtrack(s[i + 1:], path + [segment], segments + 1)


if __name__ == '__main__':

    # 测试样例
    s = "25525511135"
    print(restore_ip(s))  # Output: ["255.255.11.135", "255.255.111.35"]

    s = "0000"
    print(restore_ip(s))  # Output: ["0.0.0.0"]

    s = "101023"
    print(restore_ip(s))  # Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]


