# -*- coding: utf-8 -*-
import scrapy
import json
from First.items import ShukeItem


class YishuyikeSpiderSpider(scrapy.Spider):
    name = 'yishuyike'
    urls = 'https://api.chiyue365.com'

    headers = {
        'token': 'fd6ec68392f14c3db72ec12402702f70'
    }

    course_number = ''

    def start_requests(self):
        for num in range(3):
            url = self.urls + '/v6/packs/119/packcontent?pageNum=' + str(num+1) + '&pageSize=20'
            yield scrapy.Request(url=url,headers=self.headers, dont_filter=True, callback=self.cont_parse)

    def cont_parse(self, response):
        resp = json.loads(response.body)
        contents = resp['data']['contents']
        for num in  contents:
            contentId = num['contentId']
            url = self.urls + '/v6/contents/' + str(contentId)
            yield scrapy.Request(url=url,headers=self.headers, dont_filter=True,callback=self.parse)


    def parse(self, response):
        resp = json.loads(response.body)
        content = resp['data']['content']
        title = content['contentTitle']
        summary = content['summary']
        mp4 = content['contentMediaBackupVOList'][1]['aliBackupVideoMap']['mp4']
        mp3 = content['contentMediaBackupVOList'][0]['backupAudioUrl']
        mediaUrl = {'mp3': mp3, 'mp4': mp4}
        # print('----',mediaUrl)

        item = ShukeItem()
        item['title'] = title
        item['summary'] = summary
        item['mediaUrl'] = mediaUrl
        yield item







