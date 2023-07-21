"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : tsTcInt.py
@Author : hongbo.zhang
@Time : 2023/7/21 10:51
"""

# 基于TCP的简易本地T服务端构建
from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 分配套接字
tcpCliSock.connect(ADDR)  # 建立连接

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    # 在Python 中，socket 发送数据时需要使用encode()方法将字符串类型的数据转换为字节型数据。
    data = tcpCliSock.recv(BUFSIZ)  # 使用recv方法接受服务端返回的值。
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()