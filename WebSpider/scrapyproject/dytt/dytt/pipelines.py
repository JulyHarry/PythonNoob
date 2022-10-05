# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import requests


class DyttPipeline:
    def open_spider(self, item):
        self.f = open('movie.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        name = item.get('name')
        img_url = item.get('img_url')
        # 目录位置相对于 /spiders 文件夹
        self.f.write(str(item))
        with open(f'./images/{name}.jpg', 'wb') as f:
            response = requests.get(img_url)
            f.write(response.content)
        return item

    def close_spider(self, item):
        self.f.close()
