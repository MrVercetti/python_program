#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"


from selenium import webdriver
import time
url = 'https://www.appannie.com/account/login/?_ref=header'
email = 'don.qiu@appcoachs.com'
password = 'appannie0221'
try_times = 0

# 模拟登陆
driver = webdriver.Chrome()
driver.maximize_window()
# driver = webdriver.PhantomJS()
driver.get(url)
driver.implicitly_wait(30)
driver.find_element_by_css_selector('#email').send_keys(email)
driver.find_element_by_css_selector('#password').send_keys(password)
driver.find_element_by_id("submit").click()
time.sleep(2)


##with open("hehe.html",'w') as f:
##    f.write(driver.page_source.encode('utf-8'))
