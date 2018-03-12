# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 下午5:15
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : second.py
# @Software: PyCharm

import scrapy
from First.items import FirstItem


class LaGou(scrapy.Spider):
    name = 'lagou'
    start_urls = [
        'https://www.lagou.com/'
    ]

    cookie = {
        "_ga": "GA1.2.1610156637.1520500822",
        "_gid": "GA1.2.1662027180.1520500822",
        "user_trace_token": "20180308172025-ef2c659c-22b1-11e8-b133-5254005c3644",
        "LGUID": "20180308172025-ef2c68d9-22b1-11e8-b133-5254005c3644",
        "index_location_city": "%E5%85%A8%E5%9B%BD",
        "JSESSIONID": "ABAAABAAAIAACBI0677B671F720AE7B1CB7070DED046318",
        "hideSliderBanner20180305WithTopBannerC": "1",
        "X_HTTP_TOKEN": "bd19c61a88d80bf9d923f3c790a53c42",
        "_gat": "1",
        "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1520500822,1520563613,1520579845",
        "LGSID": "20180309151725-eadfeb7b-2369-11e8-a4ed-525400f775ce",
        "PRE_UTM": "m_cf_cpt_baidu_pc",
        "PRE_HOST": "www.baidu.com",
        "PRE_SITE": "https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26oq%3D40%252526lt%25253B%26rsv_pq%3Dc09eb728000a5141%26rsv_t%3D823b4%252FJB09qAkCtUTkMEwg8bcxtpGhIoupoDAN2v3v72FTqpyCOOBaytX30%26rqlang%3Dcn%26rsv_enter%3D1%26inputT%3D264%26rsv_sug3%3D128%26rsv_sug1%3D81%26rsv_sug7%3D100%26bs%3D403",
        "PRE_LAND": "https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc",
        "TG-TRACK-CODE": "index_navigation",
        "SEARCH_ID": "2bcf871a84154624846f8ceadcd4c9a0",
        "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1520580120",
        "LGRID": "20180309152159-8e72b96a-236a-11e8-b173-5254005c3644"
    }

    def parse(self, response):
        for item in response.xpath('//*[@id="sidebar"]/div/div/div/div/a'):
            joburl = item.xpath('@href').extract_first()

            for i in range(1):
                joburl2 = joburl + str(i + 1)
                try:
                    yield scrapy.Request(url=joburl2, cookies=self.cookie, callback=self.parse_url)
                except:
                    pass
            # yield fi

    def parse_url(self, response):

        for sel in response.xpath('//*[@id="s_position_list"]/ul/li'):
            jname = sel.xpath('div/div/div/a/h3/text()').extract_first()
            jmoney = sel.xpath('div/div/div/div/span/text()').extract_first()

            jcompany = sel.xpath('div/div/div/a/text()').extract()
            jcompany = jcompany[3].strip()

            jneed = sel.xpath('div/div/div/div/text()').extract()

            jneed = jneed[2].strip()
            jaddress = sel.xpath('div/div/div/a/span/em/text()').extract_first()

            fi = FirstItem()
            fi['jname'] = jname
            fi['jmoney'] = jmoney
            fi['jneed'] = jneed
            fi['jcompany'] = jcompany
            fi['jaddress'] = jaddress

            yield fi
