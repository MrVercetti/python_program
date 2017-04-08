#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import time

from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.tempo.co/indeks'
driver = webdriver.Chrome()
driver.maximize_window()
# driver = webdriver.PhantomJS()
driver.get(url)
web_data = driver.page_source
soup = BeautifulSoup(web_data, 'lxml')
titles = soup.select('#sub-1 > div > ul > li > div.box-text > h3 > a')
for title in titles:
    link = title.attrs['href']
    driver.get(link)
    driver.execute_script("window.scrollBy(0,3000)")
    time.sleep(2)
    web_data = driver.page_source
    soup = BeautifulSoup(web_data, 'lxml')
    images = soup.select(
        'body > div.full-body > div > div.pages-col > div.double-block > div > div > div.artikel > div.block-display > div.single-img_original > img_original')
    if images != []:
        time.sleep(2)
        fb = soup.select(
            'body > div.full-body > div > div.pages-col > div.double-block > div > div > div.share-konten.m20-b.m30-t > ul > li.fb > a > div.angka.angka-fb')
        twitter = soup.select(
            'body > div.full-body > div > div.pages-col > div.double-block > div > div > div.share-konten.m20-b.m30-t > ul > li.twitter > a > div.angka.angka-twitter')
        google = soup.select(
            'body > div.full-body > div > div.pages-col > div.double-block > div > div > div.share-konten.m20-b.m30-t > ul > li.google > a > div.angka.angka-google')
        like = soup.select(
            'body > div.full-body > div > div.pages-col > div.double-block > div > div > div.share-konten.m20-b.m30-t > ul > li.like > a > div.angka.angka-like')
        pin = soup.select(
            'body > div.full-body > div > div.pages-col > div.double-block > div > div > div.share-konten.m20-b.m30-t > ul > li.pinterest > a > div.angka.angka-pin')
        hot = sum([int(x[0].get_text()) for x in [fb, twitter, google, like, pin]])
        print 'Title:', title.get_text()
        print 'Url:', title.attrs['href']
        print 'Image:', images[0].attrs['src']
        print 'Hot:', hot
        print ''
        # if hot > 0:
        #     print 'Title:', title.get_text()
        #     print 'Image:', images[0].attrs['src']
        #     print 'Hot:', hot
        #     print ''
        # else:
        #     print 'No hot.'

driver.quit()
