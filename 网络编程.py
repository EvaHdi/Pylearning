"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 网络编程.py
@Author : hongbo.zhang
@Time : 2023/7/20 19:50
"""

from socket import *
# 创建套接字，必须使用socket.socket()函数


tcpSock = socket(AF_INET, SOCK_STREAM)
