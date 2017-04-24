#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import datetime

import os
import pandas as pd
import _winreg


def get_downloads():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    home = os.path.split(_winreg.QueryValueEx(key, "Desktop")[0])[0]
    return os.path.join(home, 'Downloads').encode('utf-8')


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0].encode('utf-8')


# Aliexpress文件原始数据路径
base = get_downloads()
file_name = [x for x in os.listdir(base) if 'AC-Alibaba-Group-7' in x][0]
file_path = os.path.join(base, file_name.decode('gbk'))

# Settlement
settlement = {
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

df = pd.read_csv(file_path, encoding='utf-8')
df[u'项目名称'] = u'Aliexpress'
df[u'媒体'] = u'facebook'
df[u'cid'] = u'762587770589717'
df[u'ctr'] = df[u'点击量（全部）'] / df[u'展示']
df[u'cpc'] = df[u'总费用 (USD)'] / df[u'点击量（全部）']
df[u'cvr'] = df[u'移动应用安装 [点击后 1 天]'] / df[u'点击量（全部）']
df[u'cpa'] = df[u'总费用 (USD)'] / df[u'移动应用安装 [点击后 1 天]']
for i in df.index:
    df.loc[i, u'结算cpa'] = settlement[df.loc[i, u'国家/地区']]
df[u'revenue'] = df[u'结算cpa'] * df[u'移动应用安装 [点击后 1 天]']
df[u'margin'] = df[u'revenue'] - df[u'总费用 (USD)']
df = df.sort_values(by=[u'国家/地区', u'报告开始日期'], ascending=True)
df = df.loc[:,
     [u'国家/地区', u'项目名称', u'报告开始日期', u'媒体', u'cid', u'展示', u'点击量（全部）', u'移动应用安装 [点击后 1 天]',
      u'总费用 (USD)', u'ctr', u'cpc', u'cvr', u'cpa', u'结算cpa', u'revenue', u'margin']]
df.columns = [u'国家', u'项目名称', u'日期', u'媒体', u'CID', u'Impression', u'Click',
              u'Conversion', u'Cost', u'CTR', u'CPC', u'CVR', u'实际CPA', u'结算CPA',
              u'Revenue', u'Margin']

# 添加汇总
df_tail = pd.DataFrame(index=[0], columns=df.columns)
df_tail.loc[0, u'国家'] = u'汇总'
df_tail.loc[0, u'项目名称'] = u'Aliexpress'
df_tail.loc[0, u'媒体'] = u'facebook'
df_tail.loc[0, u'CID'] = u'762587770589717'
df_tail.loc[0, u'Impression'] = df[u'Impression'].sum()
df_tail.loc[0, u'Click'] = df[u'Click'].sum()
df_tail.loc[0, u'Conversion'] = df[u'Conversion'].sum()
df_tail.loc[0, u'Cost'] = df[u'Cost'].sum()
df_tail[u'CTR'] = df_tail[u'Click'] / df_tail[u'Impression']
df_tail[u'CPC'] = df_tail[u'Cost'] / df_tail[u'Click']
df_tail[u'CVR'] = df_tail[u'Conversion'] / df_tail[u'Click']
df_tail[u'实际CPA'] = df_tail[u'Cost'] / df_tail[u'Conversion']
df_tail.loc[0, u'Revenue'] = df[u'Revenue'].sum()
df_tail.loc[0, u'Margin'] = df[u'Margin'].sum()
# print df_tail

df = pd.concat([df, df_tail], axis=0, ignore_index=True)
print df

yesterday = datetime.date.today() - datetime.timedelta(days=1)
store_path = os.path.join(get_desktop(), 'Daily Report-Aliexpress-Facebook-{:%Y.%m.%d}.csv'.format(yesterday))
df.to_csv(store_path, index=False, encoding='gbk')

os.remove(file_path)
