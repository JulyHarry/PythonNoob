# -*- coding: utf-8 -*-

import time
import requests
from fake_useragent import UserAgent
import telnetlib


def check_effect_proxy(file='', url='https://www.baidu.com/s'):
    # tn = telnetlib.Telnet(p[0], port=p[1][:1], timeout=2)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'httpbin.org',
        'User-Agent': UserAgent().random,
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Connection': 'keep-alive'
    }
    proxies = {'HTTP': '147.106.105.236:80'}
    content = requests.get(url, proxies=proxies)
    print(content)
    print(content.content.decode('utf-8'))
    # content = requests.get(url, headers=headers)


if __name__ == '__main__':
    check_effect_proxy()
