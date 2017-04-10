#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import re

from bs4 import BeautifulSoup

with open('product.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')

    # 图片缩略图 img-thumb-item
    for img_thumb_item in soup.find_all('span', {'class': 'img-thumb-item'}):
        img_thumb_item = img_thumb_item.img.attrs['src']
        img_thumb_item = re.findall(r'(.*)_50x50\.jpg', img_thumb_item)[0]
        print img_thumb_item

    # 图片SKU缩略图 item-sku-image
    for item_sku_image in soup.find_all('li', {'class': 'item-sku-image'}):
        item_sku_image = item_sku_image.a.img.attrs['src']
        item_sku_image = re.findall(r'(.*)_50x50\.jpg', item_sku_image)[0]
        print item_sku_image


