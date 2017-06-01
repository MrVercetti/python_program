#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pickle

from bs4 import BeautifulSoup
from furl import furl

host = 'https://www.appannie.com'
f = furl(host)
ASO_links = []
with open('hehe.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')
    app_links = soup.find_all('a', {'class': 'app-link'})
    for i in app_links:
        try:
            f.path = i.attrs['href']
            f.path.segments.pop()
            f.path.segments.pop()
            f.path.segments.append('keywords')
            # print f.url
            fuck = f.url+'/#countries=TW'  # 临时添加 增加地区，默认为美国
            print fuck  # 临时添加
            # ASO_links.append(f.url)
            ASO_links.append(fuck)  # 临时添加
        except:
            pass
        with open('ASO_links.pkl', 'w') as fp:
            pickle.dump(ASO_links, fp)
