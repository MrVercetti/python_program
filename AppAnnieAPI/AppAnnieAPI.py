#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import json
import pickle

import requests
from furl import furl

host = 'https://api.appannie.com'
f = furl(host)
url = f.url
# url = 'https://api.appannie.com/v1.2/apps/google-play/keywords/explorer?' \
#       'keyword=hello' \
#       '&date=2017-03-27' \
#       '&country=US' \
#       '&device=android'

url = 'https://api.appannie.com/v1.2/apps/google-play/top-chart'
url = 'https://api.appannie.com/v1.2/accounts?page_index=0'
print url

proxies = {
    'http': 'http://101.251.219.122:7070',
    'https': 'http://101.251.219.122:7070',
}

key = '91375f242460cfa247f69d5b3cb809f34c174e95'

headers = {
    'Authorization': 'Bearer {key}'.format(key=key)
}

r = requests.get(url=url, headers=headers, proxies=proxies)
data = json.loads(r.text)
print data
with open('data.pkl', 'w') as fp:
    pickle.dump(data, fp)
