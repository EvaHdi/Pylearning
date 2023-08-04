"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 010.py
@Author : hongbo.zhang
@Time : 2023/8/4 11:38

异常处理
按照如下要求实现一段代码：
a.定义了一个CmdSend类：包含send方法，方法参数其中之一名为lba
b.自定义一个异常类OutOfRange，如果参数 lba 大于100 就抛出该异常
c.实现一个主程序：实例化一个CmdSend类，并把lba=0，50，102分别作为参数给send 方法；
d.捕获程序中OutOfRange 的异常，然后在异常处理中 打印“customized message”，然后重新抛出该异常
e.无论程序是否发生异常，最后都需要打印“Practice Makes Perfect”
"""


class OutOfRange(Exception):  # 继承异常类
    pass


class CmdSend:
    def send(self,lba):
        if lba > 100:
            raise OutOfRange("LBA out of range")
        else:
            print("success!")


if __name__ == '__main__':
    try:
        send = CmdSend()
        send.send(0)
        send.send(50)
        send.send(102)
    except OutOfRange as e:
        print("customized message",e)  # 重复抛出e会有bug，所以不用raise而使用print
    finally:
        print("Practice Makes Perfect")