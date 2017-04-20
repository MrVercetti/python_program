#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import _winreg

import os
import pandas as pd


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0]


def newdf(vid, url):
    global df_res
    # df['Ad Set Name'] = df['Ad Set Name'].map(
    #     lambda x: x.replace('Video', 'Video{vid}'.format(vid=vid)))
    # df['Ad Name'] = df['Ad Name'].map(lambda x: x.replace('Video', 'Video{vid}'.format(vid=vid)))

    # for i in df.index:
    #     # Ad Set Name
    #     Ad_Set_Name = df.loc[i, 'Ad Set Name'].split('_')
    #     Ad_Set_Name.insert(2, str(vid))
    #     Ad_Set_Name = "_".join(Ad_Set_Name)
    #     df.loc[i, 'Ad Set Name'] = Ad_Set_Name
    #
    #     # Ad Name
    #     Ad_Name = df.loc[i, 'Ad Name'].split('_')
    #     Ad_Name.insert(2, str(vid))
    #     Ad_Name = "_".join(Ad_Name)
    #     df.loc[i, 'Ad Name'] = Ad_Name

    df['Ad Set Name'] = df['Ad Name'] = 'Video{vid}'.format(vid=vid)
    df['Template URL'] = url
    # print df.loc[:, ['Ad Set Name', 'Ad Name', 'Template URL']]
    df_res = pd.concat([df_res, df], axis=0, ignore_index=True)


# 初始化一个df
df = pd.read_csv('export_20170420_1221.csv', sep='\t', encoding='utf-16-le')
df['Campaign ID'] = ''
df['Ad Set ID'] = ''
df['Ad ID'] = ''
df['Video ID'] = ''
df['Ad Set Time Start'] = ''

# 投放url
df_data = pd.read_csv('after_remove.csv')

# 初始化一个res_df
df_res = pd.DataFrame(columns=df.columns)
# print df_res

for i in df_data.index:
    vid = df_data.loc[i, 'vid']
    url = df_data.loc[i, 'url']
    # print vid
    # print url
    newdf(vid, url)
    # break

# print df_res.loc[:, ['Ad Set Name', 'Ad Name', 'Template URL']]

for i in df_res.index:
    if df_res.loc[i, 'Automatically Set Bid'] == 'No':
        df_res.loc[i, 'Ad Set Name'] = df_res.loc[i, 'Ad Set Name'] + '_Manul'
    else:
        df_res.loc[i, 'Ad Set Name'] = df_res.loc[i, 'Ad Set Name'] + '_Auto'
    if df_res.loc[i, 'Use Accelerated Delivery'] == 'No':
        df_res.loc[i, 'Ad Set Name'] = df_res.loc[i, 'Ad Set Name'] + '_Even'
    else:
        df_res.loc[i, 'Ad Set Name'] = df_res.loc[i, 'Ad Set Name'] + '_Accelerate'

print df_res.loc[:, ['Ad Set Name', 'Ad Name', 'Template URL']]

df_res.to_csv(os.path.join(get_desktop(), 'VshowUpload.csv'), index=False, encoding='utf-8')
