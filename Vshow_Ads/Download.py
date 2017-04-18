#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import _winreg
import urllib

import os
import pandas as pd


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0]


def download_media(author):
    df1 = df[df['author'].str.contains(author)]
    for i in df1.index:
        v_id = df1.loc[i, 'v_id']
        # 下载图片
        urllib.urlretrieve(df1.loc[i, 'img_url'], os.path.join('vshow_img', '{v_id}.jpg'.format(v_id=v_id)))
        print os.path.join('vshow_img', '{v_id}.jpg'.format(v_id=v_id)), 'Done'

        # 下载视频
        urllib.urlretrieve(df1.loc[i, 'source_url'], os.path.join('vshow_video', '{v_id}.mp4'.format(v_id=v_id)))
        print os.path.join('vshow_video', '{v_id}.mp4'.format(v_id=v_id)), 'Done'


csv_path = os.path.join(get_desktop(), 'vshow_DropDuplicates.csv')
df = pd.read_csv(csv_path)
# print df.columns
author_list = ['Mey', 'lucu0000', 'Anti Galau']
for author in author_list:
    print author
    download_media(author)
    print

print 'All Done.'