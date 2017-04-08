#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pandas as pd
import _winreg
import os


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0]


df = pd.read_csv(os.path.join(get_desktop(), 'don.csv'), encoding='utf-8')

for i in df.index:
    settlement = float(df.loc[i, u'广告系列名称'].split('_')[-1].split('-')[3])
    cpa = df.loc[i, u'单次成效费用 [点击后 1 天]']
    # print settlement
    # print type(cpa)
    df.loc[i, u'margin_cpa'] = settlement - cpa
    df.loc[i, u'os'] = df.loc[i, u'广告系列名称'].split('_')[1]
    df.loc[i, u'country'] = df.loc[i, u'广告系列名称'].split('_')[2]

df[u'margin'] = df[u'margin_cpa'] * df[u'成效 [点击后 1 天]']

print df
df.to_csv(os.path.join(get_desktop(), 'Analysis_Don.csv'), index=False, encoding='gbk')
