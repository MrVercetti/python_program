#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.aliexpress.com/'

driver = webdriver.Chrome()

driver.get(url)
# 关闭Coupon
driver.find_element_by_class_name('close-layer').click()
# 打开女装
driver.find_element_by_css_selector(
    '#home-firstscreen > div > div.categories > div > div.categories-list-box > dl.cl-item.cl-item-women > dt > span > a').click()
# 打开dress
driver.find_element_by_css_selector(
    '#broad-category-main > div.container.bc-not-standard.no-standard-more-eight > div.bc-list-wrap > ul > li:nth-child(1) > div.bc-cate-name.bc-nowrap-ellipsis > a').click()
# 切换句柄
driver.switch_to.window(driver.window_handles[1])
# 按照下单数量排序
driver.find_element_by_id('sortBySelect').click()
driver.find_element_by_css_selector('#sortBySelect > ul > li:nth-child(2)').click()

soup = BeautifulSoup(driver.page_source, 'lxml')
print soup
