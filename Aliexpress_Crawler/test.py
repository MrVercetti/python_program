#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from bs4 import BeautifulSoup
import re
import pandas as pd

df = pd.DataFrame(
    columns=[u'image', u'sku', u'product-name', u'product-link', u'price', u'unit', u'rate-percent', u'rate-num',
             u'order-num', u'store-name', u'store-link'])

with open('fuck.html', 'r') as web_data:
    soup = BeautifulSoup(web_data, 'lxml')
    list_item = soup.select('#list-items > ul > li')
    for item in list_item:
        # 商品缩略图 image
        image = item.select('div > div.img.img-border > div > a > img')[0]
        try:
            image = image.attrs['src']
        except:
            image = image.attrs['image-src']
        # print image

        # sku
        try:
            sku = item.select('div > div.has-sku-image > a')[0].get_text()
        except:
            sku = u''
        # print sku

        # 商品名称 product-name
        product_name = item.select('div > div.info > h3 > a')[0].get_text()
        # print product_name

        # 商品链接 product-link
        product_link = item.select('div > div.info > h3 > a')[0].attrs['href']
        product_link = re.findall(r'//(.*)', product_link)[0]
        # print product_link

        # 价格 price
        price = item.select('div > div.info > span > span.value')[0].get_text()
        # print price

        # 单位 unit
        unit = item.select('div > div.info > span > span.unit')[0].get_text()
        # print unit

        # 好评率 rate-percent
        rate_percent = item.select('div > div.info > div > span.star.star-s')[0].attrs['title']
        rate_percent = re.findall(r'Star Rating: (.*) out of 5', rate_percent)[0]
        # print rate_percent

        # 评论数量 rate-num
        rate_num = item.select('div > div.info > div > a')[0].get_text()
        rate_num = re.findall(r'\((\d*)\)', rate_num)[0]
        # print rate_num

        # 下单量 order-num
        order_num = item.select('div > div.info > div > span.order-num > a > em')[0].get_text()
        order_num = re.findall(r'Orders \((\d*)\)', order_num)[0]
        # print order_num

        # 商铺名称 store-name
        store_name = item.select('div > div.info-more > div.store-name-chat > div > a')[0].get_text()
        # print store_name

        # 商铺链接 store-link
        store_link = item.select('div > div.info-more > div.store-name-chat > div > a')[0].attrs['href']
        store_link = re.findall(r'//(.*)', store_link)[0]
        # print store_link

        # break

        # 数据打包
        data = {
            'image': image,
            'sku': sku,
            'product-name': product_name,
            'product-link': product_link,
            'price': price,
            'unit': unit,
            'rate-percent': rate_percent,
            'rate-num': rate_num,
            'order-num': order_num,
            'store-name': store_name,
            'store-link': store_link,
        }
        # print data

        df_data = pd.DataFrame(data, [0])
        df = pd.concat([df, df_data], axis=0, ignore_index=True)

print df
df.to_csv('text.csv', index=False, encoding='utf-8')
