#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import re

import pandas as pd

df = pd.read_csv('C:/Users/donq2/Desktop/lily.csv', encoding='utf-8')

for i in df.index:
    settlement = df.loc[i, u'广告系列名称'].split('_')[-1].split('-')[-1]
    settlement = float(re.findall(r'(.*)\[LFR\]', settlement)[0])
    cpa = df.loc[i, u'单次成效费用 [点击后 1 天]']
    df.loc[i, u'margin_cpa'] = settlement - cpa
    df.loc[i, u'os'] = df.loc[i, u'广告系列名称'].split('_')[1]
    df.loc[i, u'country'] = df.loc[i, u'广告系列名称'].split('_')[2]

df[u'margin'] = df[u'margin_cpa']*df[u'成效 [点击后 1 天]']
print df
df.to_csv('C:/Users/donq2/Desktop/Analysis_Lily.csv', index=False, encoding='gbk')

