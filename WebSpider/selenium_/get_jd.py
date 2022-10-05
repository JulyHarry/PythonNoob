# -*- coding: utf-8 -*-

import requests
from selenium import webdriver

url = 'https://www.jd.com'

# 这里没有"京东秒杀"
# rsp = requests.get(url=url)
# print(rsp.text)

browser = webdriver.Chrome('../downloads/chromedriver')
browser.get(url)
content = browser.page_source
print(content)
