# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import time

from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://business.facebook.com/"
email = "hazel.fu@appcoachs.com"
psd = "Appcoach&WayneEnterprises"

driver = webdriver.Chrome()
driver.maximize_window()
# driver = webdriver.PhantomJS()
driver.get(url)
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(psd)
driver.find_element_by_id("u_0_1").click()
driver.implicitly_wait(30)
print driver.get_cookies()
soup = BeautifulSoup(driver.page_source, 'lxml')
links = soup.select(
    "#bizsitePageContainer > div._4-u2._19lb._4-u8._52jv > div > div:nth-of-type(3) > table > tbody > tr > td > a")
accounts = soup.select(
    "#bizsitePageContainer > div._4-u2._19lb._4-u8._52jv > div > div:nth-of-type(3) > table > tbody > tr > td > a > div > div > div > div > div:nth-of-type(2) > div._c24._50f7")

# for link, accout in zip(links, accounts):
#     data = {
#         'account': accout.get_text().encode("utf-8") ,
#         'link': link.attrs['href']
#     }
#     print data

account_dir = {
    'papaya': 'https://business.facebook.com/?business_id=327496050974777',
    'meetsocial': 'https://business.facebook.com/?business_id=626641800801863',
    'pzoom': 'https://business.facebook.com/?business_id=315360665315324',
    'lanhan': 'https://business.facebook.com/?business_id=164993980520476',
    'madhouse': 'https://business.facebook.com/?business_id=818736204824088'
}

driver.get(account_dir['papaya'])
time.sleep(2)
driver.find_element_by_css_selector(
    "#u_0_a > div > div._1eo6._5aj7 > div._4bl9 > ul > div:nth-child(2) > li > em").click()
driver.implicitly_wait(30)
driver.find_element_by_css_selector(
    "#u_0_a > div > div._4ts2 > div > div._4hw3._4bl9 > div > div > div > div:nth-child(2) > div._2ph_._5aj7 > div:nth-child(3) > span > a > em").click()
driver.find_element_by_css_selector(
    "#globalContainer > div.uiContextualLayerPositioner.uiLayer > div > div > div > div > div._4iqr > div._2pi5._4iqs > ul > li:nth-child(2)").click()
driver.find_element_by_css_selector(
    "#globalContainer > div.uiContextualLayerPositioner.uiLayer > div > div > div > div > div._4iqv.clearfix._2pi9._2pi3 > div > button._4jy0._4jy3._4jy1._51sy.selected._42ft").click()
driver.find_element_by_css_selector(
    "#u_0_a > div > div._4ts2 > div > div._4hw3._4bl9 > div > div > div > div._3_vt._3-8z > div._3_vy._5aj7 > div:nth-child(3) > button").click()
driver.find_element_by_css_selector(
    "body > div._10._t5y.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div._4-i2._50f4 > div > div._t5-._4bl7 > div > div > ul > div:nth-child(2) > button").click()
driver.find_element_by_css_selector(
    "body > div._10._t5y.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div._4-i2._50f4 > div > div._t5-._4bl7 > div > div > ul > div:nth-child(2) > button").click()
driver.find_element_by_css_selector(
    "body > div._10._t5y.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div._4-i2._50f4 > div > div._t5-._4bl7 > div > div > ul > div:nth-child(2) > button").click()
driver.find_element_by_css_selector(
    "body > div._10._t5y.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div._4-i2._50f4 > div > div._t5-._4bl7 > div > div > ul > div:nth-child(2) > button").click()
print "fuck!"
driver.find_element_by_css_selector(
    "body > div._10._t5y.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div._4-i2._50f4 > div > div._t5o._4bl7 > ul > a:nth-child(2) > div > ul > a._1pgv._45hc._468f").click()
# driver.find_element_by_css_selector(
#     "body > div._10._t5y.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div._4-i2._50f4 > div > div._t5r._4bl9 > div._37z0 > div > div:nth-child(1) > div:nth-child(6) > div._28r7 > section > ul > span:nth-child(6) > li > div > label._2jiq.uiInputLabelInput._55sg._kv1").click()
# driver.find_element_by_css_selector(
#     "body > div._10._t5y.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div._4-i2._50f4 > div > div._t5o._4bl7 > ul > a:nth-child(3) > div > ul > a._1pgv._45hc._468f").click()
# driver.find_element_by_css_selector(
#     "body > div._10._t5y.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div._4-i2._50f4 > div > div._t5r._4bl9 > div._37z0 > div > div:nth-child(1) > div:nth-child(10) > div._28r7 > section > ul > span:nth-child(14) > li > div > label._2jir.uiInputLabelLabel > span").click()
# driver.find_element_by_css_selector(
#     "body > div._10._t5y.uiLayer._4-hy._3qw > div._59s7 > div > div > div > div > div._5a8u._5lnf.uiOverlayFooter > div > div > div._ohf.rfloat > div > button").click()
# driver.find_element_by_css_selector(
#     "#u_0_a > div > div._4ts2 > div > div._4hw3._4bl9 > div > div > div > div._3_vt._3-8z > div._3_vy._5aj7 > div:nth-child(4) > a").click()
