"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : gendata.py
@Author : hongbo.zhang
@Time : 2023/7/19 15:53
"""


from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime


tlds = ('com', 'edu', 'net', 'org', 'gov')
# 打开文件，以写入模式清空文件内容
with open('redata.txt', 'w', encoding='utf-8') as log:
    log.write('')  # 清空文件内容

for i in range(randrange(5, 11)):
    dtint = randrange(maxsize)
    dtstr = ctime(maxsize % 1000000000)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))

    """
    # 打开log.txt文件，文件存在则打开，不存在则创建后再打开，默认将log.txt文件创建在与py文件同一个目录下
    # 设置mode='a'是将log.txt文件权限设置为可读写
    # 设置encoding='utf-8'是为了正常显示中文
    log = open('redata.txt', mode='a',  )
    """

    # 打开文件，以追加模式写入新的输出
    with open('redata.txt', 'a', encoding='utf-8') as log:
        # 将print输出写入文件
        # 将需要打印到log.txt文件中的print后面设置file=log,自动换行
        print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen), file=log)
