#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from bs4 import BeautifulSoup

with open('adsee.html', 'r') as fp:
    soup = BeautifulSoup(fp.read(),'lxml')
    for i in soup.select('#ads > div > div.right_a_d_l > div.rank_right_a_img_div > div > video > source'):
        print i.attrs['src']

"""
#ads > div:nth-child(1) > div.right_a_d_l > p.right_a_d_l_text
#ads > div:nth-child(1) > div.right_a_d_l > div.rank_right_a_img_div > div > div > img
#ads > div:nth-child(720) > div.right_a_d_l > p.right_a_d_l_text
#ads > div:nth-child(1) > div.right_a_d_l > div.rank_right_a_img_div > div > video
"""