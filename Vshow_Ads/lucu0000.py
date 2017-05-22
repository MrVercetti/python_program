#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import _winreg
import json

import os
import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0].encode('utf-8')


def get_src(url):
    global i
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    print str(i) + ':', soup.find('video').attrs['src']
    i += 1
    return soup.find('video').attrs['src']


url_list = ['http://vshow.me/user/videos?user_id=c0a644bc4f7865466c778997ab9766af&pn={pn}&rn=100'.format(pn=pn) for pn
            in
            range(10)]
res = pd.DataFrame(columns=[u'height', u'img_url', u'play_url', u'ratio', u'v_id', u'width'])
i = 1

for url in url_list:
    data = json.loads(requests.get(url).text)['body']['list']
    df = pd.DataFrame(data)
    res = pd.concat([res, df], axis=0, ignore_index=True)

# 将相对路径改成绝对路径
res[u'play_url'] = res[u'play_url'].map(lambda x: "http://vshow.me" + x)

# 写入下载链接
res[u'source_url'] = res[u'play_url'].map(get_src)

store_path = os.path.join(get_desktop(), 'lucu0000.csv')
res.to_csv(store_path, index=False, encoding='utf-8')
print res
