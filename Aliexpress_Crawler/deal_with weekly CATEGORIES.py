#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import re
import _winreg
from bs4 import BeautifulSoup
import pandas as pd
import os


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0].encode('utf-8')


df = pd.DataFrame(columns=[u'cate_header', u'image', u'link', u'price', u'title'])

with open('Weekly Bestselling.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')

    # CATEGORIES
    for i in soup.find_all('div', {'class': 'cate-panel'}):
        # cate-header 标签头
        cate_header = i.select('div.cate-header')[0].get_text()
        # print cate_header

        prime_list = i.find('ul', {'class': 'horizontal wrap prime-list'})
        for j in prime_list.find_all('li', {'class': 'vertical'}):

            # link
            link = j.find('div', {'class': 'image-box vertical center flex-auto'}).a.attrs['href']
            # print link

            # image
            try:
                image = j.find('div', {'class': 'image-box vertical center flex-auto'}).a.img.attrs['data-src']
            except:
                image = j.find('div', {'class': 'image-box vertical center flex-auto'}).a.img.attrs['src']
            image = re.findall(r'(.*)_350x350\.jpg', image)[0]
            # print image

            # title
            title = j.find('div', {'class': 'title'}).a.attrs['title']
            # print title

            # price
            price = j.find('div', {'class': 'price'}).get_text()
            # print price

            # 数据打包
            data = {
                'link': link,
                'image': image,
                'title': title,
                'price': price,
                'cate_header': cate_header,
            }
            # print data

            df_data = pd.DataFrame(data, [0])
            df = pd.concat([df, df_data], axis=0, ignore_index=True)

print df
store_path = os.path.join(get_desktop(), 'Weekly Categories.csv')
df.to_csv(store_path, index=False, encoding='utf-8')
