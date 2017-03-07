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
# # for i in Soup.find_all('div'):
# #     print i
#
# """
# http://vshow.me/data/mvData?pn=2&rn=10
# http://vshow.me/data/mvData?pn=3&rn=10
# """
# url2 = 'http://vshow.me/data/mvData?pn=2&rn=10'
# html = requests.get(url2).text
# html = json.loads(html)
# for i in html['body']['mvData']:
#     print i['play_url']
#     print i['play_count']
#     print i['img_url']
#     print i['source_url']
#     # for i in i:
#     #     print i, ':', i[i]
#     break

import pandas as pd

df = pd.DataFrame([{'A': u'\u27a1'}])
print df
df.to_csv('heiheihei.csv',encoding='utf-8')

