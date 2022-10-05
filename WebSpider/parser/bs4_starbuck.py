# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import request

url = 'https://www.starbucks.com.cn/menu/'

resp = request.urlopen(url)

content = resp.read().decode('utf-8')

soup = BeautifulSoup(content, 'lxml')

urls = soup.select("div[class='preview circle']")

for u in urls:
    print(u.get('style'))
