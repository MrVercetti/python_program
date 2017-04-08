#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import urllib

import pandas as pd

from image_processing import *

df = pd.read_csv('liputan6_data_2017-03-31.csv')
df = df[df['adult_popup'] == '21 Tahun']
for i in df.index:
    image_url = df.loc[i, 'image']
    urllib.urlretrieve(image_url, 'raw_image.jpg')
    image_processing('raw_image.jpg', df.loc[i, 'title'])
