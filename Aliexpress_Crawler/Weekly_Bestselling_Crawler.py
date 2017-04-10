#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import time

from selenium import webdriver

# 登录信息
login_url = 'https://login.aliexpress.com'
loginid = 'don.qiu@appcoachs.com'
password = 'Donqiu2017'

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

# Weekly Bestselling
url = 'https://bestselling.aliexpress.com/en?spm=2114.11010108.21.3.bscESE'
driver.get(url)

# CSS selector list
selector_list = ['#widgetlsc2z2 > div.item-box > ul > li:nth-child({x})'.format(x=x) for x in range(1, 9)]
for selector in selector_list:
    driver.find_element_by_css_selector(selector).click()  # 显示完整的页面（然而并没有）
    time.sleep(1)

# 写入本地
with open("Weekly Bestselling.html",'w') as f:
    f.write(driver.page_source.encode('utf-8'))

