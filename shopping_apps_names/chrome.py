#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"


from selenium import webdriver

url = 'https://www.appannie.com'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

with open("hehe.html",'w') as f:
    f.write(driver.page_source.encode('utf-8'))
