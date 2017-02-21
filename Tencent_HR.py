#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'DonQ'

import time

from bs4 import BeautifulSoup
from selenium import webdriver

url = "http://hr.tencent.com/position.php"


def download_html(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    driver.close()
    return html


html = download_html(url)
soup = BeautifulSoup(html, 'lxml')

job_titiles = soup.select("#position > div.left.wcont_b.box > table > tbody > tr > td.l.square > a")
job_categories = soup.select("#position > div.left.wcont_b.box > table > tbody > tr > td:nth-of-type(2)")
del job_categories[0]
hcs = soup.select("#position > div.left.wcont_b.box > table > tbody > tr > td:nth-of-type(3)")
del hcs[0]
locations = soup.select("#position > div.left.wcont_b.box > table > tbody > tr > td:nth-of-type(4)")
del locations[0]
release_times = soup.select("#position > div.left.wcont_b.box > table > tbody > tr > td:nth-of-type(5)")
del release_times[0]

for job_titile, job_categorie, hc, location, release_time in zip(job_titiles, job_categories, hcs, locations,
                                                                 release_times):
    print job_titile.get_text().encode("utf-8")
    print job_categorie.get_text().encode("utf-8")
    print hc.get_text().encode("utf-8")
    print location.get_text().encode("utf-8")
    print release_time.get_text().encode("utf-8")
    print ""

"""#position > div.left.wcont_b.box > table > tbody > tr:nth-child(2) > td:nth-child(2)"""
"""#position > div.left.wcont_b.box > table > tbody > tr:nth-child(3) > td:nth-child(2)"""
"""#position > div.left.wcont_b.box > table > tbody > tr.h > td:nth-child(2)"""
"""#position > div.left.wcont_b.box > table > tbody > tr:nth-child(11) > td:nth-child(2)"""
"""#position > div.left.wcont_b.box > table > tbody > tr.h > td:nth-child(2)"""
