# -*- coding: utf-8 -*-
import json
import logging
import time
from typing import Dict

import requests

from Mine.mysql_client import myslq_cursor

logging.basicConfig(format='%(asctime)s  %(levelname)s  %(message)s', level=logging.DEBUG,
                    filename=f'./log/request_{time.strftime("%y%m%d")}.log', filemode='a')


def post(url: str, data: Dict, source: str, keyword: str, session=None, headers=''):
    if session:
        r = session.post(url=url, data=data)
        print('session')
    else:
        r = requests.post(url=url, data=data)
        print('request')
    keyword = keyword if len(keyword) < 100 else keyword[:100]
    log(source, r.status_code, str(data), str(r.text), keyword,
        json.dumps(headers))
    return r


def log(source: str, code: int, reqmsg: str, rspmsg: str, keyword: str, headers=''):
    logging.debug(str({'source': source, 'status_code': code, 'data': reqmsg, 'response': rspmsg, 'query': keyword,
                       'headers': headers}))


def mylog(source: str, code: int, reqmsg: str, rspmsg: str, keyword: str, headers=''):
    cursor = myslq_cursor()
    cursor.execute(
        'insert into trans_log (source, status, keyword, reqmsg, rspmsg, logtime, headers) '
        'values (%s, %s, %s, %s, %s, %s, %s)',
        [source, code, keyword, reqmsg, rspmsg, time.localtime(), headers])
    cursor.close()
