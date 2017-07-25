#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import _winreg
import datetime
import os
import re
import urllib

from bs4 import BeautifulSoup


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0].encode('utf-8')


# 生成桌面文件夹
desk_dir = os.path.join(get_desktop(), 'Aliexpress-{:%Y.%m.%d}'.format(datetime.date.today()))
os.mkdir(desk_dir)

with open('product.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')

    # 产品名字 product-name
    product_name = soup.find('span', {'class': 'img-thumb-item'}).find('img').attrs['alt']
    print product_name

    # 生成文件夹
    product_dir = os.path.join(desk_dir, product_name)
    os.mkdir(product_dir)

    # 评分 percent-num
    percent_num = soup.find('span', {'class': 'percent-num'}).get_text()
    print 'percent-num:', percent_num

    # 评分人数 rantings-num
    rantings_num = soup.find('span', {'class': 'rantings-num'}).get_text()
    print 'rantings-num: ', rantings_num

    # 下单数 order-num
    order_num = soup.find('span', {'class': 'order-num'}).get_text()
    print 'order-num:', order_num

    # 原价 price
    # 货币 p-symbol
    p_symbol = soup.find('span', {'class': 'p-symbol'}).get_text()
    # 产品价格 p-price
    sku_price = soup.find('span', {'id': 'j-sku-price'}).get_text()
    # 产品单位 p-unit
    p_unit = soup.find('span', {'class': 'p-unit'}).get_text()
    price = '{p_symbol}{sku_price}/{p_unit}'.format(p_symbol=p_symbol, sku_price=sku_price, p_unit=p_unit)
    print 'price:', price

    # 折扣价格 discount-price
    sku_discount_price = soup.find('span', {'id': 'j-sku-discount-price'}).get_text()
    discount_price = '{p_symbol}{sku_discount_price}/{p_unit}'.format(p_symbol=p_symbol,
                                                                      sku_discount_price=sku_discount_price,
                                                                      p_unit=p_unit)
    print 'discount_price:', discount_price

    # 折扣力度 p-discount-rate
    discount_rate = soup.find('span', {'class': 'p-discount-rate'}).get_text()
    print 'discount_rate: ', discount_rate

    # 写入商品信息
    info_path = os.path.join(product_dir, 'info.txt')
    with open(info_path, 'w') as fp:
        fp.write(product_name)
        fp.write('\n')
        fp.write('percent-num: {percent_num}'.format(percent_num=percent_num))
        fp.write('\n')
        fp.write('rantings-num: {rantings_num}'.format(rantings_num=rantings_num))
        fp.write('\n')
        fp.write('order-num: {order_num}'.format(order_num=order_num))
        fp.write('\n')
        fp.write('price: {price}'.format(price=price))
        fp.write('\n')
        fp.write('discount_price: {discount_price}'.format(discount_price=discount_price))
        fp.write('\n')
        fp.write('discount_rate: {discount_rate}'.format(discount_rate=discount_rate))
        fp.write('\n')

    print "img_thumb_item: "
    # 图片缩略图 img-thumb-item
    for index, img_thumb_item in enumerate(soup.find_all('span', {'class': 'img-thumb-item'})):
        img_thumb_item = img_thumb_item.img.attrs['src']
        img_thumb_item = re.findall(r'(.*)_50x50\.jpg', img_thumb_item)[0]
        print img_thumb_item
        store_path = os.path.join(product_dir, 'img_thumb_item_{index}.jpg'.format(index=index))
        urllib.urlretrieve(img_thumb_item, store_path)
        print "Done"
        index += 1

    print

    print 'item_sku_image: '
    # 图片SKU缩略图 item-sku-image
    for index, item_sku_image in enumerate(soup.find_all('li', {'class': 'item-sku-image'})):
        item_sku_image = item_sku_image.a.img.attrs['src']
        item_sku_image = re.findall(r'(.*)_50x50\.jpg', item_sku_image)[0]
        print item_sku_image
        store_path = os.path.join(product_dir, 'item_sku_image_{index}.jpg'.format(index=index))
        urllib.urlretrieve(item_sku_image, store_path)
        print "Done"
        index += 1
        