"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 002.py
@Author : hongbo.zhang
@Time : 2023/7/17 16:51
"""

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return factorial(num-1)*num

if __name__ == '__main__':
    n = input("please input a positive integer: ")
    result = [str(factorial(i)) for i in range(1,n+1)]
    print(",".join(result))


