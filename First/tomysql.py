# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 下午5:35
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : tomysql.py
# @Software: PyCharm

import pymysql
import json
import sys

class ToMysql():


    def databa(self):
        db_user = 'root'
        db_host = '127.0.0.1'
        db_pwd = 'guo'
        db_base = 'test'
        db = pymysql.connect(db_host, db_user, db_pwd, db_base, charset='utf8')
        cursor = db.cursor()
        data = []
        with open('/Users/guo/PycharmProjects/First/douban.json','r', encoding='utf-8') as f:
            for line in f:
                data.append(json.loads(line))

        for item in data:
            sql = 'insert into test(title,score,num) values(%s,%s,%s)'
            cursor.execute(sql,(item['title'],item['score'],item['num']))
            db.commit()







if __name__ == '__main__':
    ToMysql().databa()




