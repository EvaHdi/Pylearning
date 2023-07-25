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


def write4K(start):
    print('Write to {}'.format(start))


print('Sequential Write')
start_address = 0
# 最大地址为 100 * 1024 * 1024 - 1，即100MB范围内的最大地址，所以最后一次写操作无法进行，必须减去4096。
end_address = 100 * 1024 * 1024 - 4096  # 首先全部转换为大B，100MB 范围内地址空间，每个写操作4KB
while start_address <= end_address:
    write4K(start_address)
    start_address += 4096

print('Random Write')
addresses = list(range(0, 100 * 1024 * 1024, 4096))
random.shuffle(addresses)
for address in addresses:
    write4K(address)


