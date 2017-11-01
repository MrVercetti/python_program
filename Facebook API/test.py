#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from facebookads.api import FacebookAdsApi
from facebookads import adobjects

my_app_id = '2379820422243900'
my_app_secret = 'a9a6ec38fca144f43c03af042a3cc023'
my_access_token = '8b7f2b3913f3d32cbb36206ef5a49228'
my_account_id = 'act_891110457737447'
proxies = {'http': '127.0.0.1:1080', 'https': '127.0.0.1:1080'}

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token, my_account_id, proxies)
