#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import re

import requests
from bs4 import BeautifulSoup

# url = "http://bola.liputan6.com/read/2875491/kick-off-persib-bandung-vs-pbfc-dimajukan-jam-berapa"
url = "http://video.liputan6.com/read/2879039/news-flash-kpk-sebut-korupsi-e-ktp-sudah-direncanakan"

s = requests.session()

read_data = s.get(url).text
read_soup = BeautifulSoup(read_data, 'lxml')

"""

#main > div.container-article > div > article > header.read-page--header > div.read-page--social-share.top > div > span.read-page--social-share__share-count-value
"""
# article_num_read = re.findall(r'article-\d{7}', read_data)[0]
# print article_num_read
# selector_article_num_read = '#core-{article_num_read} > header > div.read-page--social-share.top > div > span.read-page--social-share__share-count-value'.format(article_num_read=article_num_read)
# share_count = read_soup.select(selector_article_num_read)[0].get_text()
share_count = read_soup.find("span", {"class": 'read-page--social-share__share-count-value'}).get_text()
print share_count
try:
    gallery_image_num = re.findall(r'gallery-image-\d{7}', read_data)[0]
    print gallery_image_num
    image = read_soup.select('#gallery-image-1519509 > div > a > picture > source')
    print image[0].attrs['data-srcset'].split(',')[1].split(" ")[1]
    comments_count = read_soup.select("#open-conversation-button-2875491 > span")
    print comments_count[0].get_text()
except IndexError, e:
    image = []
    print image

"""
#vod-player > div.vjs-poster


# imge_url= "http://cdn0-a.production.images.static6.com/5JpNPcVdSoyC_uUlAw3LBWjFgu0=/1280x710/smart/filters:quality(75):strip_icc():format(webp)/liputan6-media-production/medias/1519509/original/009565600_1488076238-Persib-vs-Mitra-Kukar-6.jpg"
# with open('fuck.webp','wb') as fp:
#     fp.write(s.get(imge_url).content)


#
"""

#
# open-conversation-button-2875491 > span
# article_2876333 > aside > header > h4 > a > span
# core-article-2876333 > header > div.read-page--social-share.top > div > span.read-page--social-share__share-count-value
