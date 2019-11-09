# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 上午11:08
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : proxy.py
# @Software: PyCharm


from bs4 import BeautifulSoup
import requests
import random



def get_ip_list(url, headers):

    html = requests.get(url=url, headers=headers).text
    bs = BeautifulSoup(html,'lxml')
    ips = bs.find_all('tr')
    ip_list = []
    for i in range(1,len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':'+ tds[2].text)
        return ip_list



def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    print(proxies)
    return proxies



if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    proxies=get_random_ip(get_ip_list(url, headers))

    urls = 'http://fanyi.baidu.com/'
    #使用proxy
    web_data = requests.get(url=urls,headers=headers,proxies=proxies)
    print(web_data.text.encode('utf-8'))

    # from scrapy.commands import list
    # from First.spiders.douban import DouBan
    #
    # db = DouBan()
    #
    # print(db.name=='douban')

    # for item in list:
    #     print(item)

