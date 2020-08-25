#_*_ coding:utf-8_*_
"""

@Time:2020/8/25 19:44
@Author:Power5Bin
@File:002.py
@IDE:PyCharm
@Email:75806318@qq.com

"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
url = 'http://www.pythonscraping.com/pages/warandpeace.html'
html = urlopen(url)
bs = BeautifulSoup(html.read(),'html.parser')
namelist = bs.findAll('span',{'class':'green'})
for name in namelist:
    print(name.get_text())