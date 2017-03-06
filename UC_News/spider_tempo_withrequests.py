#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import requests
from bs4 import BeautifulSoup

url = 'https://www.tempo.co/indeks'
r = requests.get(url)
Soup = BeautifulSoup(r.text, 'lxml')
titles = Soup.select('#sub-1 > div > ul > li > div.box-text > h3 > a')
for i in titles:
    Soup = BeautifulSoup(requests.get(i.attrs['href']).text)
    print Soup
