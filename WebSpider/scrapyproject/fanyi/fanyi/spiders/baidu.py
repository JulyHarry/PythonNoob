import scrapy
import json


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['fanyi.baidu.com']

    # start_urls = ['http://fanyi.baidu.com/sug']

    def start_requests(self):
        url = 'http://fanyi.baidu.com/sug'

        data = {
            'kw': 'test'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)

    def parse(self, response):
        content = json.loads(response.text)
        print(content)
