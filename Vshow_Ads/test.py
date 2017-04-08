#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

# import json
#
# import requests
# from bs4 import BeautifulSoup
#
# url = 'http://vshow.me/'
#
# web_data = requests.get(url).text
# Soup = BeautifulSoup(web_data, 'lxml')
# # for adset_name in Soup.find_all('div'):
# #     print adset_name
#
# """
# http://vshow.me/data/mvData?pn=2&rn=10
# http://vshow.me/data/mvData?pn=3&rn=10
# """
# url2 = 'http://vshow.me/data/mvData?pn=2&rn=10'
# html = requests.get(url2).text
# html = json.loads(html)
# for adset_name in html['body']['mvData']:
#     print adset_name['play_url']
#     print adset_name['play_count']
#     print adset_name['img_url']
#     print adset_name['source_url']
#     # for adset_name in adset_name:
#     #     print adset_name, ':', adset_name[adset_name]
#     break

import pandas as pd

df = pd.DataFrame([{'A': u'\u27a1'}])
print df
df.to_csv('heiheihei.csv',encoding='utf-8')

