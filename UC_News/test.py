#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import requests
from bs4 import BeautifulSoup

url = 'http://health.liputan6.com/read/2898188/memahami-ereksi-pria-dari-remaja-sampai-lansia#'
# url = 'http://health.liputan6.com/read/2693890/rahasia-panjang-umur-para-lansia-di-spanyol-ternyata-sederhana?HouseAds&campaign=TipsKesehatan_Health_STM'

r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
print type(soup.find('p', {'class': 'adult-popup__age'}).get_text())
