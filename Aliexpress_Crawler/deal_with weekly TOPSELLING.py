#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import re

from bs4 import BeautifulSoup

with open('Weekly Bestselling.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')

    # TOP SELLING
    for i in soup.find_all('li', {'class': 'top10-item'}):
        # rank
        rank = i.div.find('span', {'class': 'rank'}).get_text()
        # print rank

        # orders
        orders = i.div.find('span', {'class': 'orders'}).get_text().split(' ')[0]
        # print orders

        # img-wrap
        img_wrap = i.find('div', {'class': 'img-wrap'}).a.img.attrs['src']
        img_wrap = re.findall(r'(.*)_200x200\.jpg', img_wrap)[0]
        # print img_wrap

        # item-desc 产品描述
        item_desc = i.find('a', {'class': 'item-desc'}).get_text()
        # print item_desc

        # link
        link = i.find('a', {'class': 'item-desc'}).attrs['href']
        # print link

        # price
        price = i.find('span', {'class': 'price'}).get_text()
        # print price

        # unit
        unit = i.find('span', {'class': 'uint'}).get_text().split(' ')[1]
        # print unit
