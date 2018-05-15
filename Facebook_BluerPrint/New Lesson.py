#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome()


def fuck():
    web_data = BeautifulSoup(driver.page_source, 'lxml')
    for js in ["var q=document.documentElement.scrollTop={num}".format(num=x) for x in range(0, 8000, 1000)]:
        driver.execute_script(js)
        time.sleep(1)
    if web_data.select("div.co-jump_text > a")[0].get_text() != u'\u70b9\u51fb\u6b64\u5904':
        driver.find_element_by_css_selector("div.co-jump_text > a").click()
    else:
        driver.find_element_by_css_selector("div.co-jump_text > a.co-jump-link > div > button").click()


def shit():
    # 启动课程
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_css_selector("div.instructionspanel__actions > a").click()
    time.sleep(15)

    # 进入句柄1 查看所有章节 进入章节1
    driver.switch_to.window(driver.window_handles[1])
    web_data = BeautifulSoup(driver.page_source, 'lxml')
    item_num = len(web_data.select('div.menu-item-button > a'))
    print "item_num:", item_num
    driver.find_element_by_css_selector("div.menu-item-button > a").click()
    time.sleep(5)

    for i in range(item_num):
        fuck()
        time.sleep(2)

    time.sleep(5)

def ed(x):
    driver.switch_to.window(driver.window_handles[0])
    for j in range(x):
        shit()
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_css_selector('#next_activity > a > div.nextactivity__content > div').click()


# driver.switch_to.window(driver.window_handles[0])
# web_data = BeautifulSoup(driver.page_source, 'lxml')
# len(web_data.select("#pathnav-container > div > ul > li"))
# for j in range(len(web_data.select("#pathnav-container > div > ul > li"))):
#     shit()
#     driver.switch_to.window(driver.window_handles[0])
#     driver.find_element_by_css_selector('#next_activity > a > div.nextactivity__content > div').click()
# driver.switch_to.window(driver.window_handles[0])
# driver.find_element_by_css_selector(
#     "#pathnav-container > div > a.pathbar__pathnav.pathbar__pathnav--next.theme__link--nondefault > h3").click()
