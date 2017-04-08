#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pickle

from bs4 import BeautifulSoup
from furl import furl

with open('hehe.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')
    app_names = soup.select(
        '#aa-app > div > div > div > div:nth-of-type(2) > app-group-table-container > div > div.ng-isolate-scope > div > div.dashboard-table.fixed-columns-table-container > div:nth-of-type(3) > table > tbody > tr > td.app-v2.tbl-col-app-v2.ng-scope > div > div > div.main-info > div > div.app-link-container > a > span')
    with open('names.txt', 'w') as f:
        for i in app_names:
            name = i.get_text().split('-')[0].encode('utf-8')
            f.write(name)
            f.write('\n')
            print name

# os.remove('hehe.html')



