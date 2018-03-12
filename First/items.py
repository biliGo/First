# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jname = scrapy.Field()
    jmoney = scrapy.Field()

    jcompany = scrapy.Field()
    jneed = scrapy.Field()
    jaddress = scrapy.Field()
    pass

class GetDoubanItem(scrapy.Item):
    num = scrapy.Field()
    title = scrapy.Field()
    score = scrapy.Field()
