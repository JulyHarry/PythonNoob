import scrapy

from dytt.items import DyttItem


class Dytt8Spider(scrapy.Spider):
    name = 'dytt8'
    allowed_domains = ['m.dytt8.net', 'www.dytt8.net', 'img9.doubanio.com/view/photo/l_ratio_poster/public/']
    start_urls = ['https://m.dytt8.net/']

    def parse(self, response):
        parser = response.xpath('//div[@class="co_area2"]/div[@class="co_content8"]//td[1]/a[2]')
        for p in parser:
            name = p.xpath('./text()').extract_first()
            detail_url = 'https://www.dytt8.net' + p.xpath('./@href').extract_first()
            yield scrapy.Request(url=detail_url, callback=self.parse_img, meta={'name': name})

    def parse_img(self, response):
        # 如果拿不到数据，首先查看xpath解析是否正确，再确定解析的网址是否在allowed_domains内
        img_url = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        name = response.meta['name']
        movie = DyttItem(name=name, img_url=img_url)
        yield movie
