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


df = pd.read_csv(os.path.join(get_desktop(), 'vic.csv'), encoding='utf-8')

settlement_list = {
    'AU': 3,
    'BE': 3,
    'BR': 2,
    'CA': 2.5,
    'CH': 2,
    'CL': 1.5,
    'CZ': 1.5,
    'DE': 3.5,
    'ES': 3,
    'FR': 3.5,
    'GB': 3,
    'HU': 1,
    'IL': 2,
    'IT': 3,
    'JP': 1.5,
    'KR': 0.5,
    'MX': 0.8,
    'NL': 3.5,
    'NZ': 3,
    'PL': 2,
    'SA': 0.8,
    'SE': 2.5,
    'SK': 1,
    'TR': 0.8,
    'US': 3,
    'RU': 0.8,
    'BY': 0.8,
}

for i in df.index:
    settlement = settlement_list[df.loc[i, u'广告系列名称'].split('_')[2]]
    cpa = df.loc[i, u'单次成效费用 [点击后 1 天]']
    # print settlement
    # print type(cpa)
    df.loc[i, u'margin_cpa'] = settlement - cpa
    df.loc[i, u'os'] = df.loc[i, u'广告系列名称'].split('_')[1]
    df.loc[i, u'country'] = df.loc[i, u'广告系列名称'].split('_')[2]

df[u'margin'] = df[u'margin_cpa'] * df[u'成效 [点击后 1 天]']

print df
df.to_csv(os.path.join(get_desktop(), 'Analysis_Vic.csv'), index=False, encoding='gbk')
