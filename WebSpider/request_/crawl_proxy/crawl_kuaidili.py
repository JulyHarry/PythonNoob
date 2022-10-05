# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# 爬取快代理ip
def crawl_kuaidaili(start, end, sleep_time=1.5):
    ua = UserAgent()
    ua.update()

    if start > end:
        print('起始数必须小于结束数')
        return
    with open(f'./data/kdl_ip_{time.strftime("%y%m%d", time.localtime())}.log', 'w', encoding='utf-8') as g:
        with open(f'./data/kdl_ip_{time.strftime("%y%m%d", time.localtime())}.txt', 'w', encoding='utf-8') as f:
            for page in range(start, end + 1):
                if page == 1:
                    url = 'https://www.kuaidaili.com/free/'
                else:
                    url = f'https://www.kuaidaili.com/free/inha/{str(page)}'

                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Pragma': 'no-cache',
                    'Cache-Control': 'no-cache',
                    'Host': 'www.kuaidaili.com',
                    'User-Agent': ua.random,
                    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
                    'Connection': 'keep-alive'
                }

                response = requests.post(url=url, headers=headers)
                soup = BeautifulSoup(response.text, 'lxml')
                ip_list = [s.get_text() for s in soup.select('table > tbody > tr > td[data-title="IP"]')]
                port_list = [s.get_text() for s in soup.select('table > tbody > tr > td[data-title="PORT"]')]
                type_list = [s.get_text() for s in soup.select('table > tbody > tr > td[data-title="类型"]')]

                if len(ip_list) == 0:
                    print(f'页面{page}爬取失败')
                    g.write(f'页面{page}爬取失败, 内容为: \n')
                    g.write(f'爬取时间: {time.strftime("%y-%m-%d %H:%M:%S", time.localtime())}\n')
                    g.write(response.text + '\n')
                else:
                    for i in zip(type_list, ip_list, port_list):
                        f.write(f'{i[0]} {i[1]} {i[2]}\n')
                    print(f'页面{page}已成功爬取数据, 数据有{len(ip_list)}条')
                    g.write(f'页面{page}已成功爬取数据, 数据有{len(ip_list)}条\n')
                time.sleep(sleep_time)


if __name__ == '__main__':
    start = 1  # 起始数
    end = 20  # 结束数
    crawl_kuaidaili(start, end, 1)
