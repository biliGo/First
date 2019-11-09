# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 下午3:29
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : douban.py
# @Software: PyCharm
import time

import scrapy
from First.items import GetDoubanItem

class DouBan(scrapy.Spider):
    name = 'douban'

    start_urls = [
        'https://movie.douban.com/top250?start=0&filter='
    ]

    url = 'https://movie.douban.com/top250'



    def parse(self, response):

        sites = response.xpath('//ol[@class="grid_view"]/li')

        print('----------------------------------------------')

        for sel in sites:
            item = GetDoubanItem()
            item['num'] = sel.xpath('div/div/em/text()').extract_first()
            title = sel.xpath('div/div/div/a/span/text()').extract()
            item['title'] = title[0]
            item['score'] = sel.xpath('div/div/div/div/span[2]/text()').extract_first()

            yield item

        urls = response.xpath('//*[@id="content"]/div/div[1]/div[2]/a/@href').extract()


        for ll in urls:
            try:

                # time.sleep(3)
                if ll != '?start=0&filter=':
                    yield scrapy.Request(url=self.url + ll, callback=self.parse)
            except:
                pass


