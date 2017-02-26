#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import requests

proxies = {
    'http': 'http://101.251.219.122:7070',
    'https': 'http://101.251.219.122:7070'
}
print requests.get('https://www.google.com/', proxies=proxies).content
