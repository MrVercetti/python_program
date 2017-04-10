#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import time

from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd


# 获取一页商品列表
def get_listitem(url):
    global try_times
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    list_item = soup.select('#list-items > ul > li')
    if list_item:
        for item in list_item:
            get_item(item)
            try_times = 0
    else:
        time.sleep(5)
        try_times += 1
        print 'try time:', try_times
        get_listitem(url)


# 提取每个商品的信息
def get_item(item):
    global df
    # 商品图 image
    image = item.select('div > div.img.img-border > div > a > img')[0]
    try:
        image = image.attrs['src']
    except:
        image = image.attrs['image-src']
    image = re.findall(r'(.*)_220x220\.jpg', image)[0]
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
    try:
        rate_percent = item.select('div > div.info > div > span.star.star-s')[0].attrs['title']
        rate_percent = re.findall(r'Star Rating: (.*) out of 5', rate_percent)[0]
    except:
        rate_percent = u''
    # print rate_percent

    # 评论数量 rate-num
    try:
        rate_num = item.select('div > div.info > div > a')[0].get_text()
        rate_num = re.findall(r'\((\d*)\)', rate_num)[0]
    except:
        rate_num = u''
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
    print data
    print

    # 写入DataFrame
    df_data = pd.DataFrame(data, [0])
    df = pd.concat([df, df_data], axis=0, ignore_index=True)


# 登录信息
login_url = 'https://login.aliexpress.com'
loginid = 'don.qiu@appcoachs.com'
password = 'Donqiu2017'

# 链接列表
list_url = map(lambda
                   page: 'https://www.aliexpress.com/category/200003482/dresses/{page}.html?site=glo&g=y&SortType=total_tranpro_desc&needQuery=n&tc=af&tag='.format(
    page=page), range(1, 11))

# 尝试次数
try_times = 0

# 初始化列表字段
df = pd.DataFrame(
    columns=[u'image', u'sku', u'product-name', u'product-link', u'price', u'unit', u'rate-percent', u'rate-num',
             u'order-num', u'store-name', u'store-link'])

# 打开浏览器
driver = webdriver.Chrome()
driver.maximize_window()

# 模拟登陆
driver.get(login_url)
driver.switch_to.frame('alibaba-login-box')
driver.find_element_by_id('fm-login-id').send_keys(loginid)
driver.find_element_by_id('fm-login-password').send_keys(password)
driver.find_element_by_id('fm-login-submit').click()
time.sleep(5)

# # 抓取信息
# for url in list_url:
#     get_listitem(url)
#     time.sleep(10)
#
# # 写入本地
# print df
# df.to_csv('Aliexpress-Dresses.csv', index=False, encoding='utf-8')

url = 'https://www.aliexpress.com/item/SheIn-Women-Brown-Velvet-Sheath-Dresses-Summer-Ladies-Round-Neck-Short-Sleeve-Knee-Length-Elegant-Pencil/32736396056.html?ws_ab_test=searchweb0_0,searchweb201602_2_10152_10066_10151_10065_10150_10068_10136_10137_10138_10060_10062_10141_10056_10055_10054_10059_10099_10103_10102_10096_10148_10147_10052_10053_10050_10107_10142_10051_10143_10084_10083_10119_10080_10082_10081_10110_10111_10112_10113_10114_130_10078_10079_10073_10070_10123_10120_10124,searchweb201603_4,afswitch_1_afChannel,ppcSwitch_2&btsid=cf7983b6-f45d-48a7-9ee3-70c89da5d12b&algo_expid=63988efa-13e3-4c79-82b3-4dc3bea9a159-15&algo_pvid=63988efa-13e3-4c79-82b3-4dc3bea9a159'
driver.get(url)
