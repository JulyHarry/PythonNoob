import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dushu.items import DushuItem


class DushucomSpider(CrawlSpider):
    name = 'dushucom'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1617_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        parser = response.xpath("//div[@class='bookslist']//img")
        for p in parser:
            name = p.xpath("./@alt").extract_first()
            img_url = p.xpath("./@data-original").extract_first()
            print(name, img_url)
            book = DushuItem(name=name, img_url=img_url)
            yield book
