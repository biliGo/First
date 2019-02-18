# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 上午10:52
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : tianyan_spider.py
# @Software: PyCharm
import scrapy
from First.items import TianyanItem
from scrapy.http import Response
import time


class TianyanSpider(scrapy.Spider):
    name = 'tianyan'

    # start_urls = [
    #     'https://www.tianyancha.com/search?key=%E8%8A%B1%E5%8D%89'
    # ]




    urls = 'https://www.tianyancha.com/search/p'

    search = '%E8%8B%97%E6%9C%A8'

    cookies = {"aliyungf_tc": "AQAAAPgh/gPeuQEA9gRgynuRg445ErPn",
               "csrfToken": "BrtK5fH6xiKlRo0uV0IGrxIt",
               "jsid": "SEM-BAIDU-PP-SY-000257",
               "TYCID": "bc6c81003ad611e8bbdd01273378855d",
               "undefined": "bc6c81003ad611e8bbdd01273378855d",
               "ssuid": "6270414301",
               "bannerFlag": "true",
               "RTYCID": "deca25149c0f4411a6377f104f28b271",
               "token": "f2b1f71a533d420aa8b36b176968e172",
               "_utm": "acaab8fd0fc24baa91e2cc67af641a36",
               "tyc-user-info": "%257B%2522new%2522%253A%25221%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzM0NjU3MzQwMyIsImlhdCI6MTUyMzE3MDk1MCwiZXhwIjoxNTM4NzIyOTUwfQ.ngl8euZ-LiOrzQTe5uvxY3cq7P9JqluWHH1ZVjW4E_54VMSJjqubA7CtGMsciZ8KJBMzP8BA3DaCBv8657Slmg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252217346573403%2522%257D",
               "auth_token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzM0NjU3MzQwMyIsImlhdCI6MTUyMzE3MDk1MCwiZXhwIjoxNTM4NzIyOTUwfQ.ngl8euZ-LiOrzQTe5uvxY3cq7P9JqluWHH1ZVjW4E_54VMSJjqubA7CtGMsciZ8KJBMzP8BA3DaCBv8657Slmg",
               "Hm_lvt_e92c8d65d92d534b0fc290df538b4758": "1523172532,1523173783,1523173804,1523173865",
               "Hm_lpvt_e92c8d65d92d534b0fc290df538b4758": "1523175263"}

    def start_requests(self):
        for num in range(10):
            ul = self.urls + str(num + 1) + '?key=' + self.search
            yield scrapy.Request(url=ul, cookies=self.cookies, callback=self.parse)

    def parse(self, response):

        for item in response.xpath('//*[@id="web-content"]/div/div/div/div[1]/div[4]/div/div[2]/div[1]/a'):
            '//*[@id="web-content"]/div/div/div/div[1]/div[4]/div/div[2]/div[1]/a'
            '//*[@id="web-content"]/div/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/a' \
            '//*[@id="web-content"]/div/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/a'
            url = item.xpath('@href').extract_first()
            yield scrapy.Request(url=url, cookies=self.cookies, callback=self.parse_item)

    def parse_item(self, response):
        title = response.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[1]/h1/text()').extract_first()
        phone = response.xpath(
            '//*[@id="company_web_top"]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]/text()').extract_first()
        email = response.xpath(
            '//*[@id="company_web_top"]/div[2]/div[2]/div[2]/div[2]/div[2]/span[2]/text()').extract_first()
        url = response.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[2]/div[3]/div[1]/a/text()').extract_first()
        address = response.xpath(
            '//*[@id="company_web_top"]/div[2]/div[2]/div[2]/div[3]/div[2]/span[2]/text()').extract_first()
        sobus = response.xpath(
            '//*[@id="_container_baseInfo"]/div/div[3]/table/tbody/tr[7]/td[2]/span/span/span[2]/text()').extract_first()

        item = TianyanItem()
        item['title'] = title
        item['phone'] = phone
        item['email'] = email
        item['url'] = url
        item['address'] = address
        item['sobus'] = sobus

        yield item
