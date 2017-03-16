#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pickle

from bs4 import BeautifulSoup
from furl import furl

# with open('hehe.html', 'r') as web_data:
#     soup = BeautifulSoup(web_data, 'lxml')
#     # 已失效
#     # app_names = soup.select(
#     #     "#aa-app > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div.ng-scope.ng-isolate-scope > div > div.dashboard-table.fixed-columns-table-container > div:nth-of-type(3) > table > tbody > tr > td.app-with-publisher-rank-iap.tbl-col-app-with-publisher-rank-iap > div > div.app-wrapper > div > a.app-name > span")
#     app_names = soup.select(
#         '#aa-app > div > div > div > div:nth-of-type(2) > div.ng-scope.ng-isolate-scope > div > div.dashboard-table.fixed-columns-table-container > div:nth-of-type(3) > table > tbody > tr > td.app-v2.tbl-col-app-v2 > div > div > div.main-info > div > div.app-link-container > a > span')
#     with open('names.txt', 'w') as f:
#         for i in app_names:
#             f.write(i.get_text().encode('utf-8'))
#             f.write('\n')
#             print i.get_text()

# os.remove('hehe.html')

# #ASO keywords
# with open('hehe.html', 'r') as web_data:
#     soup = BeautifulSoup(web_data, 'lxml')
#     keywords = soup.find_all('tr', {'class': 'main-row table-row'})
#     for i in keywords:
#         print i.find('a').get_text()

host = 'https://www.appannie.com'
f = furl(host)
ASO_links = []
with open('hehe.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')
    app_links = soup.find_all('a', {'class': 'app-link'})
    for i in app_links:
        f.path = i.attrs['href']
        f.path.segments.pop()
        f.path.segments.pop()
        f.path.segments.append('keywords')
        ASO_links.append(f.url)
    with open('ASO_links.pkl', 'w') as fp:
        pickle.dump(ASO_links, fp)
