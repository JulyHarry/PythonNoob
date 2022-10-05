# -*- coding: utf-8 -*-
from urllib import request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1664774491753_52&jsoncallback=jsonp53&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    # 'accept-encoding': 'gzip, deflate, br',  这个一般不加
    'bx-v': '2.2.3',
    'cookie': 't=519f99d832667cf07465018d212e1095; cookie2=1f9440ada2d3c9c93793c1bd1b354cdc; v=0; _tb_token_=33db53387763e; cna=P1/BG0DrA3kCAT2quMzK1xR8; xlly_s=1; tfstk=c9tcB3gUI_NBlXn9NIsjb4J1aT0RZhNOtF8k4xnHwyMVJstPis4z8LjtZsGIgP1..; l=eBMJQp2gTIllXWAwBOfwlurza77tJIRAguPzaNbMiOCPOhCp593PW6uasL89CnGNh6WkR3o34xxwBeYBcC2sjqj27iJvyBHmn; isg=BCIim1f7tUd5vKmb7Wu3l-Gwc66EcyaNij4aeGy7dhVAP8K5VAJvnfmxb3PDL54l',
    'referer': 'https://dianying.taobao.com/showList.htm?spm=a1z21.3046609.header.4.32c0112aG8ujW6&n_s=new',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

req = request.Request(url=url, headers=headers)

response = request.urlopen(req)

content = response.read().decode('utf-8')
content = content.split('(')[1].split(')')[0]

with open('../downloads/taopiaopiao_city.json', 'w', encoding='utf-8') as f:
    f.write(content)

with open('../downloads/taopiaopiao_city.json', 'r', encoding='utf-8') as f:
    jsonobj = json.load(f)
    parser = jsonpath.jsonpath(jsonobj, '$.returnValue.A')
    print(parser)
