#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"


from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

with open("hehe.html",'w') as f:
    f.write(driver.page_source.encode('utf-8'))
