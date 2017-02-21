#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii
import json
import requests
import time
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from PIL import Image
from bs4 import BeautifulSoup

userid = 'xaoq'
pwd = '123456'
vdcode = ''

s = requests.session()
s.get('https://passport.bilibili.com/login')
vdcode_content = s.get('https://passport.bilibili.com/captcha?%d' % (time.time() * 1000)).content

with open('vdcode.jpeg', 'wb') as fp:
    fp.write(vdcode_content)
im = Image.open('vdcode.jpeg')
im.show()
vdcode = raw_input('Enter the captcha: ')

data = json.loads(s.get('https://passport.bilibili.com/login?act=getkey').content)

pub_key = RSA.importKey(data['key'].encode('utf-8'))
cipher = PKCS1_v1_5.new(pub_key)
ciphertext = binascii.b2a_base64(cipher.encrypt(data['hash'].encode('utf-8') + pwd))

postdata = {
    'act': 'login',
    'gourl': 'http://www.bilibili.com/mobile/myspace.html',
    'keeptime': '604800',
    'userid': userid,
    'pwd': ciphertext,
    'vdcode': vdcode
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

s.post('https://passport.bilibili.com/login/dologin', postdata, headers=headers)
history = s.get('http://www.bilibili.com/account/history').content

print history

soup = BeautifulSoup(history, 'lxml')
for link in soup.findAll('a'):
    if 'href' in link.attrs:
        print link.attrs['href']
