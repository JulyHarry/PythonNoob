# -*- coding: utf-8 -*-

import requests

url = 'https://www.baidu.com/'
headers = {
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Host': ' www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15',
    'Referer': 'https://www.baidu.com/'
}
data = {'wd': 'sugar'}

response = requests.post(url, headers, data).text
print(response)
