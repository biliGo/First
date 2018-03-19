# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import json


class FirstPipeline(object):

    # def __init__(self):
    #     self.filename = open("douban.json", "wb", encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     jsontext = json.dumps(dict(item), ensure_ascii=False) + "\n"
    #     self.filename.write(jsontext.encode("utf-8"))
    #     return item
    #
    # def close_spider(self, spider):
    #     self.filename.close()

    def process_item(self, item, spider):

        return item
