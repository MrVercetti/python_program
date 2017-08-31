#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import urllib

import pandas as pd

from image_processing import *

df = pd.read_csv('liputan6_data_2017-08-29.csv')

# df = df[df['adult_popup'] == '21 Tahun']  # 成人向
# df = df[(df['tag'] == 'Sports') | (df['tag'] == 'Sport')]  # 体育
# print df

# for i in df.index:
#     image_url = df.loc[i, 'image']
#     urllib.urlretrieve(image_url, 'raw_image.jpg')
#     image_processing('raw_image.jpg', df.loc[i, 'title'])

# 下载share_count带k的图片
for i in df.index:
    if "k" in df.loc[i, 'share_count']:
        image_url = df.loc[i, 'image']
        print image_url
        urllib.urlretrieve(image_url, 'raw_image.jpg')
        try:
            image_processing('raw_image.jpg', df.loc[i, 'title'])
        except:
            print "Something Wrong."
            pass
