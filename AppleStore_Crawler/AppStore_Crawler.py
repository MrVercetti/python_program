#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import requests
from bs4 import BeautifulSoup

url = 'https://itunes.apple.com/us/genre/ios-games-casino/id7006?mt=8'

s = requests.session()
web_data = s.get(url).text
soup = BeautifulSoup(web_data, 'lxml')
for i in soup.select('#selectedcontent > div > ul > li > a'):
    with open('ios_games_casino.txt','a') as fp:
        fp.write(i.get_text().split('-')[0].encode('utf-8'))
        fp.write('\n')
    print i.get_text().split('-')[0]
print 'Done~'