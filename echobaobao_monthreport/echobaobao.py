#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

url = 'http://appcoachs.fuseclick.com/report/campaign'

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

email = 'echo.huang@appcoachs.com'
password = 'mikishishi708049'

driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > input[type="text"]').send_keys(email)
driver.find_element_by_css_selector(
    '#loginForm > div > div:nth-child(2) > input[type="password"]:nth-child(1)').send_keys(password)

"""
#loginForm > div > div:nth-child(1) > input[type="text"]
#loginForm > div > div:nth-child(2) > input[type="password"]:nth-child(1)
"""
