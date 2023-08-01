"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 006.py
@Author : hongbo.zhang
@Time : 2023/7/31 14:15

装饰器
实现一个retry 装饰器：函数运行异常时，每5秒进行一次retry，共重复三次，三次都失败后，自动捕获，根据判断返回值，决定成功或失败
"""
import time


def decorator(func):
    def retry(*args, **kwargs):
        max_attempts = 3
        delay = 5
        attempts = 0
        result = None
        while attempts < max_attempts:
            try:
                result = func(args[0],args[1])
                break
            except Exception as e:
                print(f"Attempt {attempts + 1} failed: {e}")
                attempts += 1
                time.sleep(delay)
        return result
    return retry


@decorator
def division(num1, num2):
    r = num1 / num2
    return r


if __name__ == '__main__':
    n = input("请输入num1: ")
    m = input("请输入num2(不可为0)：")
    print(division(int(n), int(m)))