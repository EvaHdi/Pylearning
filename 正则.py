"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 正则.py
@Author : hongbo.zhang
@Time : 2023/7/18 17:56
"""
import re


def repractice01():
    str1 = "food on the table"
    m = re.match('on', str1)  # match只能从字符串开头开始匹配
    if m is not None:  # 最好不要省去，以免出现Attribute异常
        print(m.group())


def repractice02():
    m = re.search('foo', 'seafoodfool')  # search可以匹配中间的字符串，严格从左到右搜索，只记录第一次出现的位置
    if m is not None:
        print(m.group())


def repractice03():
    bt = 'bat|bit|bet'  # 择一匹配符|
    m = re.search(bt, 'he bit bat bet me')
    if m is not None:
        print(m.group())


def repractice04():
    m = re.match('[cr][23][dp][o2]', 'c3po')  # 字符集匹配，限制没有择一匹配符严格
    if m is not None:
        print(m.group())


def repractice05():
    # 匹配网址模板 '\w+@(\w+\.)+\.com'
    patt = r'\w+@(\w+\.)?\w+\.com'  # ?表示出现0或者1次
    patt1 = r'\w+@(\w+\.)*\w+\.com'  # *表示允许任意数量的中间子域名
    print(re.match(patt, 'nobody@xxx.com').group())
    print(re.match(patt, 'nobody@www.xxx.com').group())
    print(re.match(patt1, 'nobody@www.xxx.yyy.zzz.com').group())


def repractice06():
    m = re.search('^The', 'The end.')  # ^表示从The开始的位置匹配
    if m is not None:
        print(m.group())
    n = re.search(r'\bthe', 'bite the dog')  # \b表示有边界，同理\B表示没有边界
    if n is not None:
        print(n.group())


def repractice07():
    print(re.findall('car', 'carry the barcardi to the car'))
    # findall总是返回一个列表，这是和search和match的区别
    # finditer有什么区别暂时没看懂


def repractice08():
    print(re.sub('[ae]', 'X', 'abcdef'))
    print(re.subn('[ae]', 'X', 'abcdef'))
    # sub会替换，subn在替换的同时会返回替换了几处


def test01():
    strs = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']
    patt = '[bh][aiu]t'
    for i in strs:
        print(re.match(patt, i).group())


def test02():
    str2 = ['Lebron James', 'Steven Curry', 'Russel Westbrook', 'Kevin Durant']
    patt = r'\w+ \w+'
    for i in str2:
        print(re.search(patt, i).group())


def test03():
    str3 = 'this is my job, I will work hard'
    patt = r'\w+, \w+'
    print(re.search(patt, str3).group())


def test04():
    str4 = 'das sadwdd s dsad  s'
    patt = '[a-zA-Z_]+[\w_]+'
    print(re.search(patt, str4).group())


if __name__ == '__main__':
    # repractice01()
    # repractice02()
    # repractice03()
    # repractice04()
    # repractice05()
    # repractice06()
    # repractice07()
    # repractice08()
    # test01()
    # test02()
    # test03()
    test04()
