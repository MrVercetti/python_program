#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pickle
import random
import time

from bs4 import BeautifulSoup
from selenium import webdriver


def collect_keywords():
    global try_times
    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'lxml')
    keywords = soup.find_all('tr', {'class': 'main-row table-row'})
    if keywords == []:
        try_times += 1
        if try_times == 5:
            try_times = 0
            pass
        else:
            time.sleep(3)
            collect_keywords()
    else:
        with open('keyword.txt', 'a') as fp:
            for keyword in keywords:
                keyword = keyword.find('a').get_text().encode('utf-8')
                fp.write(keyword)
                fp.write('\n')
                print keyword


# 读取APP的ASO链接列表
pickle_file = open('ASO_links.pkl', 'r')
ASO_links = pickle.load(pickle_file)

# 初始参数
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

for link in ASO_links:
    time.sleep(random.randint(20, 30))
    driver.get(link)
    collect_keywords()
