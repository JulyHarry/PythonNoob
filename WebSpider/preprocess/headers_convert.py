# -*- coding: utf-8 -*-

"""
将浏览器中的headers字段转化为python的字典对
"""

import re

cpl = re.compile('(.*): (.*)')
with open('headers_process/headers_before') as f:
    with open('headers_process/headers_after', 'w') as g:
        content = f.read()
        res = cpl.sub(r"'\1': '\2',", content)
        res = res[:-1]
        g.write(res)
