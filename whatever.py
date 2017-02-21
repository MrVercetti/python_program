#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import urllib

import requests

s = requests.session()
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
s.post('http://www.hzlike.com/index.php/user/login', 'username=q_miranda&password=q_miranda14', headers=headers)
url = raw_input('url: ')
post_url = {
    'name': url
}
post_url = urllib.urlencode(post_url)
new_url = post_url + '&order=ch_add_like&value=100'
print 'Ready. Start liking in 30minutes.'
time.sleep(15 * 60)
s.post("http://www.hzlike.com/index.php?ch_add_likes", new_url, headers=headers)
print 'Done 100 likes.'
new_url = post_url + '&order=ch_add_like&value=100'
print 'Start liking in 60minutes.'
time.sleep(60 * 60)
s.post("http://www.hzlike.com/index.php?ch_add_likes", new_url, headers=headers)
print 'All done. '
