#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from selenium import webdriver

url = 'https://facebook.exceedlms.com/student/enrollments/create_enrollment_from_token/Ape7XyWYezorLZG7NjUUzQT4'
url = 'https://facebook.exceedlms.com/student/home/show_enrollment/42043133'


driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)