"""
# -*- coding:utf-8 -*-
@Project : learning
@File : practice01.py
@Author : EvaHdi
@Time : 2023/7/18 20:17
"""
def is_little_endian():
    num = 0x0102  # 创建一个16位整数

    # 将整数转换为字节数组并检查第一个字节的值
    byte_array = bytearray(num.to_bytes(2, 'big'))
    if byte_array[0] == 0x01:
        return False  # 大端序列
    else:
        return True  # 小端序列

if is_little_endian():
    print("CPU采用小端格式")
else:
    print("CPU采用大端格式")