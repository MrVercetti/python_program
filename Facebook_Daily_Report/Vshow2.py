#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import datetime
import os
import _winreg
import pandas as pd


def get_downloads():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    home = os.path.split(_winreg.QueryValueEx(key, "Desktop")[0])[0]
    return os.path.join(home, 'Downloads').encode('utf-8')


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0].encode('utf-8')


yesterday = datetime.date.today() - datetime.timedelta(days=1)
base = get_downloads()
vshow = [x for x in os.listdir(base) if 'VSHOW' in x]
vshow = map(lambda x: os.path.join(base, x.decode('gbk')), vshow)
df = pd.read_csv(vshow[0])
df['项目名称'] = 'Vshow'
df['媒体'] = 'Facebook'
df['CID'] = '899593780177355'
df['OS'] = 'Android'
df['CTR'] = df['点击量（全部）'] / df['展示次数']
df['CPC'] = df['总费用 (USD)'] / df['点击量（全部）']
df['CVR'] = df['移动应用安装'] / df['点击量（全部）']
df['实际CPA'] = df['总费用 (USD)'] / df['移动应用安装']
df['结算CPA'] = 0.3
df['Revenue'] = df['结算CPA'] * df['移动应用安装']
df['Margin'] = df['Revenue'] - df['总费用 (USD)']
df = df.sort_values(by=['国家/地区', '报告开始日期'], ascending=True)
df = df.loc[:,
     ['报告开始日期', '项目名称', '国家/地区', '媒体', 'CID', 'OS', '展示次数', '点击量（全部）', '移动应用安装', '总费用 (USD)', 'CTR',
      'CPC', 'CVR', '实际CPA', '结算CPA', 'Revenue', 'Margin']]
df.columns = ['日期', '项目名称', '国家', '媒体', 'CID', 'OS', 'Impression', 'Click', 'Conversion', 'Cost', 'CTR', 'CPC',
              'CVR', '实际CPA', '结算CPA', 'Revenue', 'Margin']

# 添加汇总
df_tail = pd.DataFrame(index=[0], columns=df.columns)
df_tail.loc[0, '日期'] = '汇总'
df_tail.loc[0, '项目名称'] = 'Vshow'
df_tail.loc[0, '媒体'] = 'Facebook'
df_tail.loc[0, 'CID'] = '899593780177355'
df_tail.loc[0, 'OS'] = 'Android'
df_tail.loc[0, 'Impression'] = df['Impression'].sum()
df_tail.loc[0, 'Click'] = df['Click'].sum()
df_tail.loc[0, 'Conversion'] = df['Conversion'].sum()
df_tail.loc[0, 'Cost'] = df['Cost'].sum()
df_tail['CTR'] = df_tail['Click'] / df_tail['Impression']
df_tail['CPC'] = df_tail['Cost'] / df_tail['Click']
df_tail['CVR'] = df_tail['Conversion'] / df_tail['Click']
df_tail['实际CPA'] = df_tail['Cost'] / df_tail['Conversion']
df_tail.loc[0, 'Revenue'] = df['Revenue'].sum()
df_tail.loc[0, 'Margin'] = df['Margin'].sum()
# print df_tail

df = pd.concat([df, df_tail], axis=0, ignore_index=True)
print df

store_path = os.path.join(get_desktop(), 'Daily Report-Vshow2-Facebook-{:%Y.%m.%d}.csv'.format(yesterday))
df.to_csv(store_path, index=False, encoding='gbk')

os.remove(vshow[0])
