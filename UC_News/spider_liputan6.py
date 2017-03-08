#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import datetime
import re

import requests
from bs4 import BeautifulSoup
from furl import furl


def get_data(url):
    web_data = s.get(url).text
    Soup = BeautifulSoup(web_data, 'lxml')
    article_numbers = re.findall(r'article_\d{7}', web_data)
    selector_titles = ["#{article_number} > aside > header > h4 > a > span".format(article_number=article_number) for
                       article_number in article_numbers]
    selector_tags = ["#{article_number} > aside > header > a ".format(article_number=article_number) for
                     article_number in article_numbers]
    selector_links = ["#{article_number} > aside > header > h4 > a ".format(article_number=article_number) for
                      article_number in article_numbers]
    titles = map(Soup.select, selector_titles)
    tags = map(Soup.select, selector_tags)
    links = map(Soup.select, selector_links)
    for title, tag, link in zip(titles, tags, links):
        if tag:
            data = {
                'title': title[0].get_text(),
                'tag': tag[0].get_text(),
                'link': link[0].attrs["href"]
            }
            print data
        else:
            data = {
                'title': title[0].get_text(),
                'tag': [],
                'link': link[0].attrs["href"]
            }


# 处理url日期参数
How_long = 90
dates = [[(datetime.datetime.now() - datetime.timedelta(i)).strftime(("%Y,%m,%d"))][0].split(',') for i in
         range(1, 1 + How_long)]
for i in range(How_long):
    dates[i].insert(0, 'indeks')

# 建立url_list
url_list = []
host = 'http://www.liputan6.com/'
f = furl(host)
for i in range(How_long):
    f.path.segments = dates[i]
    for j in range(1, 16):
        f.set({'page': j}).url
        url_list.append(f.url)

s = requests.session()
for i in url_list:
    get_data(i)
