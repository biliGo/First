# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 4:12 下午
# @Author  : guo
# @Email   : lessguo@163.com
# @File    : fandeng_merge.py
# @Software: PyCharm

import json

def merge_media():
    vf = []
    with open('/Users/guo/PycharmProjects/First/fandeng_video.json', encoding='utf-8') as f:
        vf = json.load(f)

    af = []
    with open('/Users/guo/PycharmProjects/First/fandeng_audio.json', encoding='utf-8') as f:
        af = json.load(f)

    lis = []
    for v in vf:
        v_title = v['title']
        for a in af:
            a_title = a['title']
            if v_title == a_title:
                summary = v['summary']
                audio = a['mediaUrls'][0]
                video = v['mediaUrls'][0]
                dic = {'title': v_title, 'summary': summary, 'mediaUrls': {'audio': audio, 'video': video}}
                lis.append(dic)


    print(json.dumps(lis, ensure_ascii=False))
    # print(len(lis))
    # a = ''.join("".join('%s' %id for id in lis))
    # print(len(a))

    # with open('/Users/guo/PycharmProjects/First/fandeng_media.json',  'w', encoding='utf-8') as f:
    #     f.write(json.dumps(lis, ensure_ascii=False))


if __name__ == '__main__':
    merge_media()