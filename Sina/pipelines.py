# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class SinaPipeline(object):

    def open_spider(self, spider):
        self.f = open('sina.json', 'w')

    def process_item(self, item, spider):

        json_str = json.dumps(dict(item)) + ",\n"

        self.f.write(json_str)
        return item

    def close_spider(self, spider):
        self.f.close()

