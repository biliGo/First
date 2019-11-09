# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 下午5:45
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : __init__.py.py
# @Software: PyCharm

from scrapy.exporters import JsonLinesItemExporter

class JsonChongXie(JsonLinesItemExporter):
    def __init__(self, file, **kwargs):
        super(JsonChongXie, self).__init__(file, ensure_ascii=None)