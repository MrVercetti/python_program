#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from bs4 import BeautifulSoup
from selenium import webdriver


# 登录
def login():
    driver.get(login_url)
    driver.find_element_by_css_selector('#nav_login > a').click()
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('log_box_button').click()


login_url = 'https://www.adseedata.com/'
email = 'lu.fan@appcoachs.com'
password = 'appcoachom0428'

url = 'https://www.adseedata.com/apps/ios/app/1084930849/ad-details/?_ref=search_page#video'

# 打开浏览器
driver = webdriver.Chrome()
driver.maximize_window()

# 登录
login()

# 数据抓取
raw_input()
driver.get(url)
soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'lxml')

css_list = ['#ads > div:nth-of-type({num}) > div.right_a_d_l > div.rank_right_a_img_div > div > div > img'.format(num=x)
            for x in range(1, 721)]

for i in css_list:
    try:
        driver.find_element_by_css_selector(i).click()
    except:
        pass


# with open('adsee.html', 'w') as fp:
#     fp.write(driver.page_source.encode('utf-8'))
