#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import os

from bs4 import BeautifulSoup

with open('hehe.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')
    app_names = soup.select(
        "#aa-app > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div.ng-scope.ng-isolate-scope > div > div.dashboard-table.fixed-columns-table-container > div:nth-of-type(3) > table > tbody > tr > td.app-with-publisher-rank-iap.tbl-col-app-with-publisher-rank-iap > div > div.app-wrapper > div > a.app-name > span")
    with open('names.txt', 'w') as f:
        for i in app_names:
            f.write(i.get_text().encode('utf-8'))
            f.write('\n')
            print i.get_text()

os.remove('hehe.html')
print "shared in github~"