"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 多线程.py
@Author : hongbo.zhang
@Time : 2023/7/25 20:19
"""

import threading
from time import sleep, ctime


def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())


def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())


def main():
    print('starting ar: ', ctime())
    threading.stack_size(loop0(), ())
    threading.stack_size(loop1(), ())
    sleep(6)
    print("all DONE at:", ctime())



if __name__ == '__main__':
    main()
