#_*_ coding:utf-8_*_
"""

@Time:2020/8/25 17:52
@Author:Power5Bin
@File:001.py
@IDE:PyCharm
@Email:75806318@qq.com

"""
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('title not be found')
else:
    print(title)