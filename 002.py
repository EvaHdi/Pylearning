"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 002.py
@Author : hongbo.zhang
@Time : 2023/7/17 16:51

对存储设备的读写分为两种：顺序和随机。如果下一笔写的起始地址和上一笔写的结束地址是连续的，则该笔操作是顺序的，否则为随机的。现在要求如下，对100MB范围内地址空间，每笔写4KB大小，实现顺序写和随机写（覆盖所有地址空间）
a. “写”函数可以自定义，输出打印即可
b. 主要考察列表、列表生成式、循环、随机函数
def write4K(start):
    print('Write to {}'.format(start))
...
print('Sequential Write')
...
print('Random Write')
"""
import random


def write4k(start):
    print('Write to {}'.format(start))


def sequential_write(start_address, end_address):
    print('Sequential Write')
    while start_address <= end_address:
        write4k(start_address)
        start_address += 4096


def random_write(mb, speed):
    print('Random Write')
    addresses = list(range(0, mb, speed))
    addresses.pop(len(addresses)-1)  # 弹出列表最后一个地址，因为会越界
    while len(addresses)>0:
        num = random.randint(0,len(addresses)-1)
        write4k(addresses.pop(num))



if __name__ == '__main__':
    start_address = 0
    # 最大地址为 100 * 1024 * 1024 - 1，即100MB范围内的最大地址，所以最后一次写操作无法进行，必须减去4096。
    end_address = 100 * 1024 * 1024 - 4096  # 首先全部转换为大B，100MB 范围内地址空间，每个写操作4KB
    ssd = 100 * 1024 * 1024
    speed = 4096
    sequential_write(start_address, end_address)
    random_write(ssd, speed)

