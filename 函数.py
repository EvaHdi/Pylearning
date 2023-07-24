"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 函数.py
@Author : hongbo.zhang
@Time : 2023/7/21 16:38
"""
# git pull --rebase origin main 从远程仓库拉下代码和本地合并
# git rebase --continue 完成合并，即可正常提交。


def pratice01(list_name):
    list_name[0] = 'you'
    print(list_name)


def pratice02(*args):  #*args接受任意数量的实参
    for i in args:
        print(i)

if __name__ == '__main__':
    """
    # 01
    list_name = ['I', 'am', 'hongbo', 'zhang']
    pratice01(list_name[:]) #通过这种方式，传入的是副本，修改列表也不会影响原来的列表
    print(list_name)
    """

    """
    # 02
    pratice02('chicken', 'beef', 'pig')
    pratice02('person')
    """


    