#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import json
import time

import pandas as pd
import requests


def get_img(video_data):
    global error_times
    try:
        image = s.get(video_data['img_url']).content
        with open('vshow_pic/{v_id}.jpg'.format(v_id=video_data['v_id']), 'wb') as fp:
            fp.write(image)
    except requests.exceptions.ConnectionError, e:
        print 'requests.exceptions.ConnectionError', e
        time.sleep(5)
        error_times += 1
        if error_times == 4:
            with open('error_log.txt', 'w') as f:
                f.write(video_data['v_id'])
                f.write('\r\n')
            error_times = 0
        else:
            get_img(video_data)


error_times = 0
base = 'http://vshow.me'
s = requests.session()
s.get(base)
url_list = ['http://vshow.me/data/mvData?pn={pn}&rn=10'.format(pn=pn) for pn in range(1, 10000)]

index = 0
for url in url_list:
    data = json.loads(s.get(url).text)['body']['mvData']
    for i in data:
        print i['img_url']
        print i['v_id']
        get_img(i)
        print "Done~"
    df = pd.DataFrame(data)
    df.to_csv('vshow_data/vshow_{index}.csv'.format(index=index))
    index += 1
    # print df
    # break
