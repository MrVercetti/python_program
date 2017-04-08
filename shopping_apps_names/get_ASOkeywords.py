#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from bs4 import BeautifulSoup

with open('hehe.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')
    keywords = soup.find_all('tr', {'class': 'main-row table-row'})
    with open('keywords_earning','a') as fp:
        for i in keywords:
            fp.write(i.find('a').get_text().encode('utf-8'))
            fp.write('\n')
            print i.find('a').get_text()
