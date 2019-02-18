# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 下午5:35
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : tomysql.py
# @Software: PyCharm

import pymysql
import json
import sys
from flask import jsonify

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    db_user = 'root'
    db_host = '127.0.0.1'
    db_pwd = 'guo'
    db_base = 'test'
    db = pymysql.connect(db_host, db_user, db_pwd, db_base, charset='utf8')
    cursor = db.cursor()
    cursor.execute('select * from test')
    list = cursor.fetchall()
    print(type(list))

    data = []
    for i in list:
        dict = {}
        dict['id'] = i[0]
        dict['title'] = i[1]
        dict['score'] = i[2]
        dict['num'] = i[3]
        # print(dict)
        data.append(dict)

    # print(dict)
    dc = json.dumps(data, ensure_ascii=False)
    # print(dc)
    return dc



class ToMysql():


    def databa(self):
        db_user = 'root'
        db_host = '127.0.0.1'
        db_pwd = 'guo'
        db_base = 'test'
        db = pymysql.connect(db_host, db_user, db_pwd, db_base, charset='utf8')
        cursor = db.cursor()
        data = []
        with open('/Users/guo/PycharmProjects/First/pub.json','r', encoding='utf-8') as f:
            for line in f:
                data.append(json.loads(line))

        for item in data:
            sql = 'insert into pua(title,content) values(%s,%s)'
            content = ''.join(item['content'])
            cursor.execute(sql,(item['title'],content))
            db.commit()
        print('done')


def GetLagou():
    ll = []
    with open('/Users/guo/PycharmProjects/First/lagou.json', 'r', encoding='utf-8') as f:
        for item in f:
            ll.append(json.loads(item))

    print(ll)

def books():
    with open('/Users/guo/PycharmProjects/First/books.json', 'r', encoding='utf-8') as f:
        dict = json.load(f)

    ll = dict['books']
    lis = []
    for item in ll:
        dic = item['contents']
        for it in dic:
            if it['type'] == 3:
                lis.append(it['fragmentId'])

    print(lis)




if __name__ == '__main__':
    # app.run()
    books()




