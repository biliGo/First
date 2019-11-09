# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 下午2:35
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : pua_spider.py
# @Software: PyCharm

import scrapy
from First.items import PubItem


class PuaSpider(scrapy.Spider):
    name = 'pua'

    start_urls = [
        'http://www.meixueyuan.com/pua-252-1.html'
    ]

    url = 'http://www.meixueyuan.com/'

    cookie = {
        "8oGs_2132_saltkey": "xfCU30sK",
        "8oGs_2132_lastvisit": "1519867793",
        "__cfduid": "ded90d95fbd067631aa9b63fe9bbe98e31520912706",
        "8oGs_2132_forum_lastvisit": "D_191_1520912734D_254_1520912760D_252_1520922724",
        "8oGs_2132_visitedfid": "252D254D191D245",
        "8oGs_2132_sid": "xDkEZ1",
        "8oGs_2132_lastact": "1520924731%09index.php%09"
    }

    def parse(self, response):

        a_href = response.xpath('//*[@id="fd_page_top"]/div/a/@href').extract()
        for ll in a_href:
            try:
                if ll != 'forum.php?mod=forumdisplay&fid=252&page=1':
                    yield scrapy.Request(url=self.url + ll, callback=self.parse)
            except:
                pass


        pua = response.xpath('//*[@id="nv_forum"]/div[5]/div/a')
        for item in pua:
            ur = item.xpath('@href').extract_first()
            urls = self.url + ur
            yield scrapy.Request(url=urls, cookies=self.cookie, callback=self.parse_pua)

    def parse_pua(self, response):
        title = response.xpath('//*[@id="nv_forum"]/div[4]/div/div[2]/div[3]/h1/text()').extract_first()

        content = response.xpath('//*[@id="nv_forum"]/div[4]/div/div[2]/div[3]/div[2]/text()').extract()

        img = response.xpath('//*[@id="nv_forum"]/div[4]/div/div[2]/div[3]/div[2]/div/ignore_js_op/img/@src').extract_first()


        item = PubItem()
        item['title'] = title
        item['content'] = content
        item['img'] = img

        yield item
