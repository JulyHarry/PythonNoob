# -*- coding: utf-8 -*-

import time
import requests
from fake_useragent import UserAgent
import telnetlib


def check_effect_proxy(file='', url='https://www.baidu.com/s'):
    if not file:
        file = f'./data/kdl_ip_{time.strftime("%y%m%d", time.localtime())}.txt'
    with open(file, 'r', encoding='utf-8') as f:
        with open(f'./data/effective_ip_{time.strftime("%y%m%d", time.localtime())}.txt', 'w', encoding='utf-8') as g:
            for line in f.readlines():
                p = line.strip().split(' ')[1].split(':')
                try:
                    tn = telnetlib.Telnet(p[0], port=p[1], timeout=2)
                except:
                    print(f'{p[0]}:{p[1]} 无效')
                else:
                    g.write(line)


if __name__ == '__main__':
    check_effect_proxy()
