#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import _winreg
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
from selenium import webdriver


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0].encode('utf-8')


def get_index_data(url):
    global df
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    # 获取商品列表
    product_list = soup.select('#J-pro-list > li')

    for product in product_list:
        # print i
        # 产品名字
        product_name = product.select('a > h5')[0].get_text()
        # print product_name

        # 产品链接
        product_link = product.select('a')[0].attrs['href']
        # print product_link

        # 心愿数
        add_wish = product.find_all('span')[0].get_text()
        # print add_wish

        # 折扣价
        try:
            discount_price = product.find_all('span')[1].get_text()
        except Exception:
            discount_price = ''
        # print discount_price

        # 原价
        try:
            original_price = product.find_all('span')[2].get_text()
        except Exception:
            original_price = ''
        # print original_price

        # 数据打包
        data = {
            'product_name': product_name,
            'product_link': product_link,
            'add_wish': add_wish,
            'discount_price': discount_price,
            'original_price': original_price,
        }
        print data
        df_data = pd.DataFrame(data, index=[0])
        # print df_data
        df = pd.concat([df, df_data], axis=0, ignore_index=True)


# 国家
regioncode_list = ['sa', 'ae', 'kw', 'qa', 'bh', 'om', 'id', 'eg']

# 货币
currency_dict = {'sa': 'sar',
                 'ae': 'aed',
                 'kw': 'kwd',
                 'qa': 'qar',
                 'bh': 'bhd',
                 'om': 'omr',
                 'id': 'idr',
                 'eg': 'egp'}

# 打开浏览器
driver = webdriver.Chrome()
driver.maximize_window()

for rc in regioncode_list:
    url_list = [
        'http://www.jollychic.com/womens-dresses-h6?jsort=011{page}-120&regioncode={rc}&_xc_cs={currency}'.format(
            page=x, rc=rc, currency=currency_dict[rc]) for x in range(1, 51)]
    print url_list
    df = pd.DataFrame(columns=[u'add_wish', u'discount_price', u'original_price', u'product_link', u'product_name'])
    for page_num, url in enumerate(url_list):
        get_index_data(url)
        print
        print 'Done Page {page_num}.'.format(page_num=page_num + 1)
        time.sleep(2)
    df[u'rc'] = rc
    df.to_csv(os.path.join(get_desktop(), 'jollychic_dress_{rc}.csv'.format(rc=rc)), index=False, encoding='utf-8')


print 'All Done.'

"""
http://www.jollychic.com/womens-dresses-h6?jsort=0111-120
http://www.jollychic.com/womens-dresses-h6?jsort=0112-120&router=ar&regioncode=sa
http://www.jollychic.com/womens-dresses-h6?jsort=0112-120&regioncode=sa
http://www.jollychic.com/womens-dresses-h6?jsort=0112-120&regioncode=sa&_xc_cs=sar
http://ar.jollychic.com/womens-dresses-h6?jsort=0112-120&regioncode=sa&_xc_cs=usd&changeLanguage=ar
"""
