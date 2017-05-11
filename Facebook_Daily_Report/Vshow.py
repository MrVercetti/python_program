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
df['国家'] = '印度尼西亚'
df['媒体'] = 'Facebook'
df['CID'] = '1061662900598451'
df['OS'] = 'Android'
df['CTR'] = df['点击量（全部）'] / df['展示次数']
df['CPC'] = df['总费用 (USD)'] / df['点击量（全部）']
df['CVR'] = df['移动应用安装'] / df['点击量（全部）']
df['实际CPA'] = df['总费用 (USD)'] / df['移动应用安装']
df['结算CPA'] = 0.3
df['Revenue'] = df['结算CPA'] * df['移动应用安装']
df['Margin'] = df['Revenue'] - df['总费用 (USD)']
df = df.loc[:,
     ['报告开始日期', '项目名称', '国家', '媒体', 'CID', 'OS', '展示', '点击量（全部）', '移动应用安装', '总费用 (USD)', 'CTR',
      'CPC', 'CVR', '实际CPA', '结算CPA', 'Revenue', 'Margin']]
df.columns = ['日期', '项目名称', '国家', '媒体', 'CID', 'OS', 'Impression', 'Click', 'Conversion', 'Cost', 'CTR', 'CPC',
              'CVR', '实际CPA', '结算CPA', 'Revenue', 'Margin']
print df
store_path = os.path.join(get_desktop(), 'Daily Report-Vshow-Facebook-{:%Y.%m.%d}.csv'.format(yesterday))
df.to_csv(store_path, index=False, encoding='gbk')
