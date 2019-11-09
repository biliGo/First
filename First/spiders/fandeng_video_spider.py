# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 3:33 下午
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : fandeng_audio_spider.py
# @Software: PyCharm

import scrapy
import json
from First.items import FandengItem


class FandengSpiderSpider(scrapy.Spider):
    name = 'fandeng_video'
    urls = 'https://api.dushu.io'
    token = 'KEJRkP7WBuWFXrxnsPj'

    def start_requests(self):
        # print('xxx')
        for i in range(50):
            yield scrapy.FormRequest(
                url=self.urls + '/books',
                formdata={
                    "bookReadStatus": '-1',
                    "order": '-1',
                    "pageSize": '10',
                    "token": self.token,
                    "page": str(i + 1)
                },
                callback=self.content_pare
            )

    def content_pare(self, response):
        resp = json.loads(response.body)
        books = resp['books']
        # print('qqqq')
        for item in books:
            contents = item['contents']
            for i in contents:
                if i['type'] == 3:
                    yield scrapy.FormRequest(
                        url=self.urls + '/fragment/content',
                        headers={
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Accept': '',
                            'x-dushu-app-ver': '3.9.49'
                        },
                        formdata={
                            "fragmentId": str(i['fragmentId']),
                            # "fragmentId": str(200003085),
                            "albumId": '-8888888',
                            "token": self.token,
                            "programId": '-8888888'
                        },
                        callback=self.parse
                    )

    def parse(self, response):
        # print('ttt')
        resp = json.loads(response.body)
        # print('oooooo', resp)
        title = resp['title']
        summary = resp['summary']
        mediaUrls = resp['mediaUrls']

        item = FandengItem()
        item['title'] = title
        item['summary'] = summary
        item['mediaUrls'] = mediaUrls
        yield item
