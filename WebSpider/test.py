# -*- coding: utf-8 -*-

import requests

url = 'https://www.dytt8.net/html/newgame/20180125/56185.html'

response = requests.get(url)

# print(response.content.decode('gbk'))

content = response.content.decode('gbk').encode('utf-8')

with open('', 'wb') as f:
    f.write(content)
