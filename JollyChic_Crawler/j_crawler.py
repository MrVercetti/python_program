#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import _winreg
import re


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0].encode('utf-8')


def create_urllist(url):
    soup = BeautifulSoup(s.get(url).text, 'lxml')
    last_page = soup.select('#changePage > span.page-num')[0].get_text()
    last_page = int(re.findall(r'/ (\d{,2}) Page', last_page)[0])
    query_list = ['?jsort=011{page}-120'.format(page=x) for x in range(1, last_page + 1)]
    url_list = [url + query for query in query_list]
    return url_list


def get_index_data(url):
    global df
    soup = BeautifulSoup(s.get(url).text, 'lxml')

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


url = 'http://www.jollychic.com/'
s = requests.session()
web_data = s.get(url).text
soup = BeautifulSoup(web_data, 'lxml')
os.mkdir('nav')
print 'Create directory nav.'

# 初始化最终dataframe
df_res = pd.DataFrame(
    columns=[u'add_wish', u'discount_price', u'original_price', u'product_link', u'product_name', u'header_block',
             u'nav_item'])
for i in range(2, 9):
    # 导航栏分类
    nav_item = \
        soup.select('body > div.header-nav-wrap > ul > li:nth-of-type({i}) > a'.format(i=i))[0].get_text().split('/')[0]
    os.mkdir(nav_item)
    print 'Create {nav_item} directory.'.format(nav_item=nav_item)

    # 初始化nav分类dataframe
    df_nav = pd.DataFrame(
        columns=[u'add_wish', u'discount_price', u'original_price', u'product_link', u'product_name', u'header_block'])
    header_block_list = soup.select(
        'body > div.header-nav-wrap > ul > li:nth-of-type({i}) > div > div > dl > dd > a'.format(i=i))
    for header_block_item in header_block_list:
        try:
            # 分类的名字
            header_block_name = header_block_item.get_text()
            print header_block_name

            # 分类的链接主体
            header_block_link = header_block_item.attrs['href']
            print header_block_link

            # 初始化index信息dataframe
            df = pd.DataFrame(
                columns=[u'add_wish', u'discount_price', u'original_price', u'product_link', u'product_name'])
            url_list = create_urllist(header_block_link)
            for page_num, url in enumerate(url_list):
                get_index_data(url)
                print
                print 'Done Page {page_num} in {header_block_name}.'.format(page_num=page_num + 1,
                                                                            header_block_name=header_block_name)
                # time.sleep(1)
            df[u'header_block'] = header_block_name
            df.to_csv(
                os.path.join(nav_item,
                             'jollychic_{header_block_name}.csv'.format(
                                 header_block_name=header_block_name.split('/')[0])),
                index=False, encoding='utf-8')
            df_nav = pd.concat([df_nav, df], axis=0, ignore_index=True)
            print 'Done {header_block_name}!'.format(header_block_name=header_block_name)
        except Exception:
            print 'Nothing in {header_block_name}!'.format(header_block_name=header_block_name)

    df_nav['nav_item'] = nav_item
    df_nav.to_csv(os.path.join('nav', '{nav_item}.csv'.format(nav_item=nav_item)), index=False, encoding='utf-8')
    df_res = pd.concat([df_res, df_nav], axis=0, ignore_index=True)
    print '{nav_item}, Done!'.format(nav_item=nav_item)

df_res.to_csv(os.path.join(get_desktop(), 'jollychic_data.csv'), index=False, encoding='utf-8')
print 'ALL DONE!'
