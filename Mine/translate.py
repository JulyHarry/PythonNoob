# -*- coding: utf-8 -*-
import json
import re

import execjs
import requests
from fake_useragent import UserAgent

from Mine.kit import post

baidu_translate_base_url = 'https://fanyi.baidu.com/'
baidu_translate_api_url = 'https://fanyi.baidu.com/v2transapi'
baidu_translate_single_url = 'https://fanyi.baidu.com/sug'
baidu_lang_detect_url = 'https://fanyi.baidu.com/langdetect'

JS_CODE = """
function a(r, o) {
    for (var t = 0; t < o.length - 2; t += 3) {
        var a = o.charAt(t + 2);
        a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
        a = "+" === o.charAt(t + 1) ? r >>> a: r << a,
        r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
    }
    return r
}
var C = null;
var token = function(r, _gtk) {
    var o = r.length;
    o > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(o / 2) - 5, 10) + r.substring(r.length, r.length - 10));
    var t = void 0,
    t = null !== C ? C: (C = _gtk || "") || "";
    for (var e = t.split("."), h = Number(e[0]) || 0, i = Number(e[1]) || 0, d = [], f = 0, g = 0; g < r.length; g++) {
        var m = r.charCodeAt(g);
        128 > m ? d[f++] = m: (2048 > m ? d[f++] = m >> 6 | 192 : (55296 === (64512 & m) && g + 1 < r.length && 56320 === (64512 & r.charCodeAt(g + 1)) ? (m = 65536 + ((1023 & m) << 10) + (1023 & r.charCodeAt(++g)), d[f++] = m >> 18 | 240, d[f++] = m >> 12 & 63 | 128) : d[f++] = m >> 12 | 224, d[f++] = m >> 6 & 63 | 128), d[f++] = 63 & m | 128)
    }
    for (var S = h,
    u = "+-a^+6",
    l = "+-3^+b+-f",
    s = 0; s < d.length; s++) S += d[s],
    S = a(S, u);
    return S = a(S, l),
    S ^= i,
    0 > S && (S = (2147483647 & S) + 2147483648),
    S %= 1e6,
    S.toString() + "." + (S ^ h)
}
"""


class BaiduTranslate:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {'User-Agent': UserAgent().random}
        self.javascript = execjs.compile(JS_CODE)
        self.token = ''
        self.gtk = ''
        self.get_session()
        self.get_session()

    def get_session(self):
        try:
            rsp = self.session.get(url=baidu_translate_base_url, headers=self.headers)
            self.token = re.findall(r"token: '(.*?)'", rsp.text)[0]
            self.gtk = re.findall(r'window.gtk = "(.*?)";', rsp.text)[0]
            print(self.token, self.gtk)
        except Exception as e:
            raise e

    def lang_detect(self, query: str):
        data = {
            'query': query
        }
        r = post(url=baidu_lang_detect_url, data=data, source='baidu_langdetect', keyword=query, session=self.session)
        j = json.loads(r.text)
        print(j['lan'])
        return j['lan']

    def translate(self, query, dst='zh', src=None):
        sign = self.javascript.call('token', query, self.gtk)

        if not src:
            src = self.lang_detect(query)

        data = {
            'from': src,
            'to': dst,
            'query': query,
            'simple_means_flag': 3,
            'sign': sign,
            'token': self.token
        }

        print(data)
        print(query)

        r = post(url=baidu_translate_api_url, data=data, source='baidu_translate_api', keyword=query,
                 session=self.session)
        print(eval(r.text))


# def baidu_translate(query: str):
#     data = {
#         'kw': query,
#     }
#     r = post(url=baidu_translate_single_url, data=data, source='baidu_translate', keyword=query)
#     print(eval(r.text))


if __name__ == '__main__':
    content = 'meat'
    # baidu_translate(content)
    # baidu_langdetect(content)
    # logging('baidulang', 200, '{key:potato}', '{error:3306}')
    bt = BaiduTranslate()
    bt.translate("the tomato tree is dying, please water it.")
    # d = Dict()
    # print(d.dictionary('milk'))
