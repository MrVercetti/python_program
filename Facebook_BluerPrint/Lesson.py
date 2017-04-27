#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://facebook.exceedlms.com/student/enrollments/create_enrollment_from_token/Ape7XyWYezorLZG7NjUUzQT4'

email = "535868469@qq.com"
psd = "aspirine0810"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# 登录
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(psd)
driver.find_element_by_id('loginbutton').click()

# 浏览课程
# index选择课程
driver.find_element_by_css_selector(
    '#main > section > div > div > div.courselist > ul:nth-child(6) > li:nth-child(2) > div.courselist__content > a'
).click()

# 打开课程
driver.find_element_by_css_selector(
    '#student_enrollment > div > div.main-wrapper > div > div.activity__main > div > div.activity__courseinfo > div.activity__action > button'
).click()

# 切换句柄
driver.switch_to.window(driver.window_handles[1])

# 选择子课程
driver.find_element_by_css_selector(
    '#wrapper > div.menu.menu-course.undefined > div > div.menu-container-inner.box-menu-inner.clearfix > div.menu-item.menu-item-co-01.zh_cn.nth-child-1.nth-child-odd > div > div.menu-item-graphic > a > img'
).click()

web_data = BeautifulSoup(driver.page_source, 'lxml')
print web_data

"""
#wrapper > div.menu.menu-course.undefined > div > div.menu-container-inner.box-menu-inner.clearfix > div.menu-item.menu-item-co-01.zh_cn.nth-child-1.nth-child-odd > div > div.menu-item-graphic > a > img
"""
