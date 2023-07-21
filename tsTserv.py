"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : tsTserv.py
@Author : hongbo.zhang
@Time : 2023/7/21 10:25
"""

# 基于TCP的本地客户端构建
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connection")
    tcpCliSock, addr = tcpSerSock.accept()
    print("...connected from:", addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(('[%s] %s' % (bytes(ctime(), 'utf-8'), data)).encode())
        # tcpCliSock.send() 方法需要接收字节型数据作为参数，而不是字符串,使用encode()编码为字节型数据

    tcpCliSock.close()
tcpSerSock.close()