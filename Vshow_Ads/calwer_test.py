#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from urlparse import urljoin

import requests
from bs4 import BeautifulSoup

url = 'http://vshow.me/'
s = requests.session()
web_data = s.get(url)
soup = BeautifulSoup(web_data.content, 'lxml')
links = soup.select("body > div > div > div.title_words.cf > div > a.cover")
images = soup.select("body > div > div > div.title_words.cf > div > a.cover > img_original")
playnum_list = soup.select("body > div > div > div.title_words.cf > div > a.sec.cf > span.playnum")
index = 0
for link, image, playnum in zip(links, images, playnum_list):
    if int(playnum.get_text()) > 10000:
        data = {
            'link': urljoin(url, link.get('href')),
            'image': image.get('src'),
            'playnum': int(playnum.get_text())
        }
        # print data
        with open('vshow/{index}.jpg'.format(index=index), 'wb') as fp:
            fp.write(s.get(data['image']).content)
        print index, data['link']
        index += 1
