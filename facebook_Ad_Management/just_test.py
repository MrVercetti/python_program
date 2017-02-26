#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from facebookads import objects
from facebookads.api import FacebookAdsApi

my_app_id = '1251527148216435'
my_app_secret = 'f5c8b29c2e3636d0112f8cebac0648da'
my_access_token = 'EAARyQd8YoHMBAMWk85H02JS90mfRz2bTvWcZB9cxjBvIwalFmmWmK5rcRTJ3ulTgFQ9Tt0KnFJtfZA4AND3FWkWpBEYhNSndZBi' \
                  'ZCF7iKStXhvBwX5eFNcQ6VwbmJ3lHcfmZC8tRZCZBYP8cRP2B7wj6JZCBczTQJnE8rqSPGSLgzh0d5ZBjjwWOIuLH8JgHLr9p0SgS' \
                  'iam01ObZB4rs5ruozs'
proxies = {
    'http': 'http://101.251.219.122:7070',
    'https': 'http://101.251.219.122:7070'
}
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token, proxies=proxies)
me = objects.AdUser(fbid='me')
my_accounts = list(me.get_ad_accounts())
print my_accounts
print type(my_accounts[0])
my_account = my_accounts[0]
print my_account
campaign = objects.Campaign(parent_id=my_account.get_id_assured())
campaign[objects.Campaign.Field.name] = "Potato Campain"  # sic
campaign[objects.Campaign.Field.configured_status] = objects.Campaign.Status.paused
campaign.remote_create()
