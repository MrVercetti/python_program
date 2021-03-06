#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import _winreg
import datetime
import os
import re
import time
import urllib

from bs4 import BeautifulSoup
from selenium import webdriver


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0].encode('utf-8')


def get_product_info(url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # 产品名字 product-name
    product_name = soup.find('span', {'class': 'img-thumb-item'}).find('img').attrs['alt']
    print product_name

    # 生成文件夹
    product_dir = os.path.join(desk_dir, "sb")
    os.mkdir(product_dir)

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


# url = 'https://www.aliexpress.com/item/SheIn-Women-Brown-Velvet-Sheath-Dresses-Summer-Ladies-Round-Neck-Short-Sleeve-Knee-Length-Elegant-Pencil/32736396056.html?ws_ab_test=searchweb0_0,searchweb201602_2_10152_10066_10151_10065_10150_10068_10136_10137_10138_10060_10062_10141_10056_10055_10054_10059_10099_10103_10102_10096_10148_10147_10052_10053_10050_10107_10142_10051_10143_10084_10083_10119_10080_10082_10081_10110_10111_10112_10113_10114_130_10078_10079_10073_10070_10123_10120_10124,searchweb201603_4,afswitch_1_afChannel,ppcSwitch_2&btsid=cf7983b6-f45d-48a7-9ee3-70c89da5d12b&algo_expid=63988efa-13e3-4c79-82b3-4dc3bea9a159-15&algo_pvid=63988efa-13e3-4c79-82b3-4dc3bea9a159'

# 生成桌面文件夹
desk_dir = os.path.join(get_desktop(), 'Aliexpress-{:%Y.%m.%d}'.format(datetime.date.today()))
os.mkdir(desk_dir)

# 登录信息
login_url = 'https://login.aliexpress.com'
loginid = 'don.qiu@appcoachs.com'
password = 'Donqiu2017'

# 尝试次数
try_times = 0

# 打开浏览器
driver = webdriver.Chrome()
driver.maximize_window()

# # 模拟登陆
# driver.get(login_url)
# driver.switch_to.frame('alibaba-login-box')
# driver.find_element_by_id('fm-login-id').send_keys(loginid)
# driver.find_element_by_id('fm-login-password').send_keys(password)
# driver.find_element_by_id('fm-login-submit').click()
# time.sleep(5)

get_product_info('https://www.aliexpress.com/store/product/10-colors-big-Hand-t-shirt-Man-men-clothes-Printing-Hot-3D-visual-creative-personality-spoof/1168434_1846297552.html?spm=a2g01.8005315.2002.5.8T0X4X&sdom=704.123484.111128.0_1846297552')
