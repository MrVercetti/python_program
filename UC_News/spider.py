#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import requests
from bs4 import BeautifulSoup

# url = 'http://id.ucnews.ucweb.com/story/3566794351185755'
url = 'http://id.ucnews.ucweb.com/story/3393855968693502'

s = requests.session()
web_data = s.get(url)
soup = BeautifulSoup(web_data.content, 'lxml')
title = soup.select('body > div.layout > div > div.p-story-article > div > h1')[0].get_text()
like = \
    soup.select(
        'body > div.layout > div > div.p-story-article > div > div.w-article-flavor-choice > div.w-like > span')[
        0].get_text()
print 'Title:', title
print 'Like:', like

"""
w-article-title
body > div.layout > div > div.p-story-article > div > h1
like
body > div.layout > div > div.p-story-article > div > div.w-article-flavor-choice > div.w-like > span
"""
