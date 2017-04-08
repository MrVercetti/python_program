#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import datetime

import os
import pandas as pd


# 插入CTR,CVR,CPA,媒体四个columns
def insert_columns(df, file_name):
    df[u'ctr'] = df[u'点击量（全部）'] / df[u'展示']
    df[u'cvr'] = df[u'移动应用安装'] / df[u'点击量（全部）']
    df[u'cpa'] = df[u'总费用'] / df[u'移动应用安装']
    df[u'日期'] = str(yesterday)
    if u"Appcoach 报告" in file_name:
        df[u'媒体'] = u'FBpapaya'
    elif u"Appcoach Meetsocial 报告" in file_name:
        df[u'媒体'] = u'FB飞书'
    elif u'Appcoach Pzoom 报告' in file_name:
        df[u'媒体'] = u'FB品众'
    elif u'Appcoach-Madhouse 报告' in file_name:
        df[u'媒体'] = u'FBmadhouse'
    elif u'Appcoach 蓝翰报告' in file_name:
        df[u'媒体'] = u'FB蓝翰'


# 读取表格品并筛选参数以及选择columns
def filter_df(csv):
    df = pd.read_csv(csv, sep='\t', encoding='utf-16-le')
    # 插入columns
    insert_columns(df, csv)
    df = df[df[u'总费用'] > 0]
    df = df.loc[:, [u'日期', u'帐户', u'媒体', u'帐户编号', u'展示', u'点击量（全部）', u'移动应用安装', u'ctr', u'cvr', u'cpa', u'总费用']]
    return df


yesterday = datetime.date.today() - datetime.timedelta(days=1)
base = 'C:/Users/donq2/Downloads/'
files_names = [x for x in os.listdir(base) if 'Appcoach' in x]
files = map(lambda x: os.path.join(base, x.decode('gbk')), files_names)
joint_list = map(filter_df, files)
res = pd.concat(joint_list, axis=0, ignore_index=True)
res.columns = [u'日期', u'账户', u'媒体', u'CID', u'Impression', u'Click', u'Conversion', u'CTR', u'CVR', u'CPA', u'Cost']

# 降序排列
res = res.sort_values(by='Cost', ascending=False)

# 新建最后一行
df_tail = pd.DataFrame(index=[0], columns=res.columns)
df_tail.loc[0, u'日期'] = str(yesterday)
df_tail.loc[0, u'账户名称'] = u'汇总'
df_tail.loc[0, u'Impression'] = res[u'Impression'].sum()
df_tail.loc[0, u'Click'] = res[u'Click'].sum()
df_tail.loc[0, u'Conversion'] = res[u'Conversion'].sum()
df_tail.loc[0, u'Cost'] = res[u'Cost'].sum()
df_tail[u'CTR'] = df_tail[u'Click'] / df_tail[u'Impression']
df_tail[u'CVR'] = df_tail[u'Conversion'] / df_tail[u'Click']
df_tail[u'CPA'] = df_tail[u'Cost'] / df_tail[u'Conversion']
# print df_tail

# 拼接最后一行
res = pd.concat([res, df_tail], axis=0, ignore_index=True)
print res

res.to_csv("C:/Users/donq2/Desktop/Facebook Daily Report - {:%Y.%m.%d}.csv".format(yesterday), index=False,
           encoding='gbk')
