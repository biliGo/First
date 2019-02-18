# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 下午3:39
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : pandeng_spider.py
# @Software: PyCharm

import scrapy
from First.items import PandengItem
import json
import time


class PandengSpider(scrapy.Spider):
    name = 'pandeng'

    # start_urls = [
    #     'http://api.dushu.io/fragment/content'
    # ]
    ll = [5639,5579,5496,5430,5366,5300,5241,5191,5155,5122,5025,5019,4991,4947,4901,4841,4766,4728,4656,4604,4516,4480,4426,4334,4305,4266,4226,4194,4177,4158,4123,4083,4075,3948,3839,3797,3717,3542,3377,3344,3308,3276,3245,3219,3189,3166,3137,3096,3058,3016,2982,2945,2903,2866,2828,2779,2737,2706,2675,2644,2607,2572,2539,2504,2467,2437,2374,2352,2330,2304,2274,2246,2211,2182,2148,2123,2093,2064,2040,2041,1982,1956,1934,1907,1888,1846,1829,1808,1786,1757,1734,1704,1686,1655,1625,1590,1571,1521,1489,1453,1414,1386,1359,1310,1285,1255,1223,1189,1167,1141,1124,1076,1060,1031,1013,987,968,942,901,881,850,344,789,773,743,728,709,687,664,649,619,604,595,519,501,549,441,405,369,350,423,286,267,249,316,187,145,124,217,230,123,142,86,83,170,75,140,171,66,174,59,172,166,36,33,173,28,24,167,385,16,3,6,9,13]

    url = 'http://api.dushu.io/fragment/content'

    def start_requests(self):

        for line in self.ll:
            yield scrapy.FormRequest(
                url=self.url,
                headers={'Content-Type': 'application/x-www-form-urlencoded',
                         'Accept': ''},
                formdata={
                    'token': 'c14195c832aa40df9168f980d117166b',
                    'fragmentId': str(line)
                },
                callback=self.parse
            )




    def parse(self, response):

        jsobj = json.loads(response.body)
        title = jsobj['title']
        summary = jsobj['summary']
        mediaUrls = jsobj['mediaUrls']

        item = PandengItem()
        item['title'] = title
        item['summary'] = summary
        item['mediaUrls'] = mediaUrls
        yield item