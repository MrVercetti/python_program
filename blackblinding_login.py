#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select

url = "http://luru.hict.org.cn/"

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get(url)
driver.find_element_by_id("tbYHM").send_keys("建经168030".decode('utf-8'))
driver.find_element_by_id("tbPSW").send_keys("1")
sel = driver.find_element_by_id("ddlSF")
Select(sel).select_by_value("学生".decode("utf-8"))
driver.find_element_by_id("imgDL").click()
driver.implicitly_wait(30)
driver.switch_to_frame('topFrame')
driver.find_element_by_id('hlGRXX').click()
driver.switch_to_default_content()
driver.switch_to_frame('mainFrame')

soup = BeautifulSoup(driver.page_source, 'lxml')


def print_info(info):
    info_content = soup.find(id=info).get_text().encode("utf-8")
    print info + "：" + info_content


info_list = ['xh', 'xm', 'csrq', 'xb', 'jg', 'rxrq', 'mz', 'zymc', 'zyfx', 'xymc', 'bjmc', 'sfzh', 'dqszj', 'lxdh',
             'ksh', 'zkzh', 'xz', 'kslb', 'syszd', 'jtdz', 'yzbm', 'zzmm', 'rxzf', 'xjzt', 'bz']

for info in info_list:
    print_info(info)
