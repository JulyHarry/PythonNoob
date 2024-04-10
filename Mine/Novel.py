# -*- coding: utf-8 -*-
from lxml import etree


def aggregation():
    with open('/Users/hang/Downloads/frxxz.txt', 'w') as g:
        for i in range(1, 2456):
            with open(f'/Users/hang/Downloads/frxxz/OPS/chapter{i}.html') as f:
                m = f.read().replace("<br />", "").replace('    ', '').replace('手机小说大全', '').replace(
                    ' , 更多电子书下载 ', '')
                e = etree.HTML(m, etree.HTMLParser())
                title = e.xpath('//title/text()')
                content = e.xpath('//div/text()')
                g.write(''.join(title))
                g.write('\n')
                g.write(''.join(content))


def aggregation2():
    with open('/Users/hang/Downloads/frxxzxjp.txt', 'w') as g:
        for i in range(1, 2):
            with open(f'/Users/hang/Downloads/frxxz/OPS/chapter{i}.html') as f:
                m = f.read().replace("<br />", "").replace('    ', '').replace('手机小说大全', '').replace(
                    ' , 更多电子书下载 ', '')
                e = etree.HTML(m, etree.HTMLParser())
                title = e.xpath('//title/text()')
                content = e.xpath('//div/text()')
                g.write(''.join(title))
                g.write('\n')
                g.write(''.join(content))


if __name__ == '__main__':
    aggregation2()
