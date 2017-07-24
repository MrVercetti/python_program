#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import re

from bs4 import BeautifulSoup

with open('product.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')

    # 产品名字 product-name
    product_name = soup.find('h1', {'class': 'product-name'}).get_text()
    print product_name

    # 评分 percent-num
    percent_num = soup.find('span', {'class': 'percent-num'}).get_text()
    print 'percent-num: ', percent_num

    # 评分人数 rantings-num
    rantings_num = soup.find('span', {'class': 'rantings-num'}).get_text()
    print 'rantings-num: ', rantings_num

    # 下单数 order-num
    order_num = soup.find('span', {'class': 'order-num'}).get_text()
    print 'order-num: ', order_num

    # 原价 price
    # 货币 p-symbol
    p_symbol = soup.find('span', {'class': 'p-symbol'}).get_text()
    # 产品价格 p-price
    sku_price = soup.find('span', {'id': 'j-sku-price'}).get_text()
    # 产品单位 p-unit
    p_unit = soup.find('span', {'class': 'p-unit'}).get_text()
    price = '{p_symbol}{sku_price}/{p_unit}'.format(p_symbol=p_symbol, sku_price=sku_price, p_unit=p_unit)
    print 'price: ', price

    # 折扣价格 discount-price
    sku_discount_price = soup.find('span', {'id': 'j-sku-discount-price'}).get_text()
    discount_price = '{p_symbol}{sku_discount_price}/{p_unit}'.format(p_symbol=p_symbol,
                                                                      sku_discount_price=sku_discount_price,
                                                                      p_unit=p_unit)
    print 'discount_price: ', discount_price

    # 折扣力度 p-discount-rate
    discount_rate = soup.find('span', {'class': 'p-discount-rate'}).get_text()
    print 'discount_rate: ', discount_rate

    print "img_thumb_item: "
    # 图片缩略图 img-thumb-item
    for img_thumb_item in soup.find_all('span', {'class': 'img-thumb-item'}):
        img_thumb_item = img_thumb_item.img.attrs['src']
        img_thumb_item = re.findall(r'(.*)_50x50\.jpg', img_thumb_item)[0]
        print img_thumb_item

    print

    print 'item_sku_image: '
    # 图片SKU缩略图 item-sku-image
    for item_sku_image in soup.find_all('li', {'class': 'item-sku-image'}):
        item_sku_image = item_sku_image.a.img.attrs['src']
        item_sku_image = re.findall(r'(.*)_50x50\.jpg', item_sku_image)[0]
        print item_sku_image
