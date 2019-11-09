# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 下午6:54
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : quhuanqian.py
# @Software: PyCharm

import scrapy
from scrapy.http import Request
from First.items import QhqItem

class Quhuanqian(scrapy.Spider):
    name = 'qhq'

    # start_urls = [
    #     'http://api.quhuanqian.cn'
    # ]
    url = 'http://api.stg.quhuanqian.cn/discovery/article/list/1?pageSize=10&pageIndex=1'

    headers = {
        'token': '4a6a6b567b8146e1882b8cc58192be8d'
    }

    def start_requests(self):
        yield Request(url=self.url, headers={'token': self.headers['token']}, callback=self.parse)
    def parse(self, response):
        body = str(response.body,'utf-8')
        item = QhqItem()
        item['body'] = body
        yield item