#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import datetime
import os
import time

import pandas as pd
from furl import furl


# 处理日报链接
def dealwith_url(url):
    f = furl(url)
    if f.args['business_id'] == "327496050974777":
        f.args['since'] = f.args['until'] = str(yesterday)
        return f.url
    else:
        f.args['since'] = f.args['until'] = str(before_yesterday)
        return f.url


# 用chrome下载日报链接
def download_daily_report(daily_url):
    cmd = 'start \"%s\" \"%s\"' % (chrome_path, daily_url)
    return os.system(cmd)


# 检查5张日报是否下载完成
def check_completeness():
    if len([x for x in os.listdir(base) if 'Appcoach' in x]) < 5:
        time.sleep(1)
        print "Downloading..."
        check_completeness()
    else:
        print "Downloads completed."


# 插入CTR,CVR,CPA,媒体四个columns
def insert_columns(df, file_name):
    df[u'ctr'] = df[u'点击量（全部）'] / df[u'展示次数']
    df[u'cvr'] = df[u'移动应用安装'] / df[u'点击量（全部）']
    df[u'cpa'] = df[u'当前花费上限'] / df[u'移动应用安装']
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
    df = df[df[u'当前花费上限'] > 0]
    df = df.loc[:, [u'日期', u'帐户名称', u'媒体', u'帐户编号', u'展示次数', u'点击量（全部）', u'移动应用安装', u'ctr', u'cvr', u'cpa', u'当前花费上限']]
    return df


base = 'C:/Users/donq2/Downloads/'
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
yesterday = datetime.date.today() - datetime.timedelta(days=1)
before_yesterday = datetime.date.today() - datetime.timedelta(days=2)

# 原始日报链接
url_papaya = "https://business.facebook.com/home/reporting/exports/?business_id=327496050974777&fields[0]=impressions&fields[1]=spend&fields[2]=clicks&fields[3]=actions%3Amobile_app_install&filters[0][field]=account_status&filters[0][operator]=EQUAL&filters[0][value]=1&since=2017-02-12&until=2017-02-12&timezone_id=42"
url_meetsocial = "https://business.facebook.com/home/reporting/exports/?business_id=626641800801863&fields[0]=impressions&fields[1]=spend&fields[2]=clicks&fields[3]=actions%3Amobile_app_install&filters[0][field]=account_status&filters[0][operator]=EQUAL&filters[0][value]=1&since=2017-02-11&until=2017-02-11&timezone_id=1"
url_pzoom = "https://business.facebook.com/home/reporting/exports/?business_id=315360665315324&fields[0]=impressions&fields[1]=spend&fields[2]=clicks&fields[3]=actions%3Amobile_app_install&filters[0][field]=account_status&filters[0][operator]=EQUAL&filters[0][value]=1&since=2017-02-11&until=2017-02-11&timezone_id=1"
url_madhouse = "https://business.facebook.com/home/reporting/exports/?business_id=818736204824088&fields[0]=impressions&fields[1]=spend&fields[2]=clicks&fields[3]=actions%3Amobile_app_install&filters[0][field]=account_status&filters[0][operator]=EQUAL&filters[0][value]=1&since=2017-02-11&until=2017-02-11&timezone_id=1"
url_lanhan = "https://business.facebook.com/home/reporting/exports/?business_id=164993980520476&fields[0]=impressions&fields[1]=spend&fields[2]=clicks&fields[3]=actions%3Amobile_app_install&filters[0][field]=account_status&filters[0][operator]=EQUAL&filters[0][value]=1&since=2017-02-17&until=2017-02-17&timezone_id=1"

daily_urls = map(dealwith_url, [url_papaya, url_meetsocial, url_pzoom, url_madhouse, url_lanhan])
map(download_daily_report, daily_urls)
check_completeness()
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
df_tail.loc[0, u'账户'] = u'汇总'
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
map(os.remove, files)
print "All Done~"