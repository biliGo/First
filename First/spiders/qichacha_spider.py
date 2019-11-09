# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午3:18
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : qichacha_spider.py
# @Software: PyCharm

import scrapy
from First.items import QichachaItem


class Qichacha_spider(scrapy.Spider):
    name = 'qichacha'

    urls = 'https://www.qichacha.com/search?key=%E8%8B%97%E6%9C%A8'

    search_url = 'https://www.qichacha.com'

    cookies = {
        "PHPSESSID": "3l8k0tubad8uq4s6hte2jtc9a2",
        "UM_distinctid": "164ea02c28c98-0c280099a46ab5-16386953-13c680-164ea02c2916aa",
        "CNZZDATA1254842228": "438378475-1532930676-https%253A%252F%252Fwww.baidu.com%252F%7C1532930676",
        "zg_did": "%7B%22did%22%3A%20%22164ea02c2ea736-0ac7316f91bc49-16386953-13c680-164ea02c2eb350%22%7D",
        "hasShow": "1",
        "_uab_collina": "153293440762931594640848",
        "acw_tc": "AQAAAFjuqQVHiQYACawhfXYzEwhkNaUN",
        "Hm_lvt_3456bee468c83cc63fb5147f119f1075": "1532934413",
        "_umdata": "55F3A8BFC9C50DDAD664C8F78A0F6157C5BC785BA2673A6B42DE3F9F53E900853251E9C855793ECBCD43AD3E795C914C8DE22270132F2F7AD437EC193219E2EB",
        "zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f": "%7B%22sid%22%3A%201532934406894%2C%22updated%22%3A%201532935896844%2C%22info%22%3A%201532934406897%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%22e38e7c0195865c127e66b19d7e5fdc31%22%7D",
        "Hm_lpvt_3456bee468c83cc63fb5147f119f1075": "1532935897"
    }

    def start_requests(self):
        for num in range(10):
            ul = self.urls + '#p:' + str(num + 1) + '&'
            yield scrapy.Request(url=ul, dont_filter=True, cookies=self.cookies, callback=self.parse)


    def parse(self, response):

        for item in response.xpath('//*[@id="searchlist"]/table/tbody/tr/td[2]/a'):
            # '//*[@id="searchlist"]/table/tbody/tr[8]/td[2]/a'
            # print('----------------',item.xpath('text()'))
            url = item.xpath('@href').extract_first()

            yield scrapy.Request(url=self.search_url + url, cookies=self.cookies, callback=self.parse_item)

    def parse_item(self, response):

        title = response.xpath('//*[@id="company-top"]/div[1]/div[2]/div[1]/h1/text()').extract_first()
        phone = response.xpath('//*[@id="company-top"]/div[1]/div[2]/div[2]/span[1]/span[2]/span/text()').extract_first()
        url = response.xpath('//*[@id="company-top"]/div[1]/div[2]/div[2]/span[3]/a[1]/text()').extract_first()
        email = response.xpath('//*[@id="company-top"]/div[1]/div[2]/div[3]/span[1]/span[2]/a/text()').extract_first()
        address = response.xpath('//*[@id="company-top"]/div[1]/div[2]/div[3]/span[3]/a[1]/text()').extract_first()
        sobus = response.xpath('//*[@id="company-top"]/div[1]/div[2]/div[4]/span[2]/text()').extract_first()

        item = QichachaItem()
        item['title'] = title
        item['phone'] = phone
        item['url'] = url
        item['email'] = email
        item['address'] = address
        item['sobus'] = sobus

        yield item


