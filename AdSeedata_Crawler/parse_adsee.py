#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import _winreg

import os
import pandas as pd
from bs4 import BeautifulSoup


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0].encode('utf-8')


res = pd.DataFrame(columns=[u'call to action', u'date', u'message', u'title'])

with open('adsee.html', 'r') as fp:
    soup = BeautifulSoup(fp.read(), 'lxml')
    for i in soup.select('#ads > div > div.right_a_d_l'):
        date = i.select('div.right_a_d_l_app > div.right_a_d_l_app_nt > p')[0].get_text()
        # print date
        message = i.select('p.right_a_d_l_text')[0].get_text()
        # print message
        title = i.select('p.right_a_d_l_text_bottom')[0].get_text()
        # print title
        call_to_action = i.select('a')[0].get_text()
        # print call_to_action

        data = {
            'date': date,
            'message': message,
            'title': title,
            'call to action': call_to_action,
        }
        # print data
        df = pd.DataFrame(data, [0])
        res = pd.concat([res, df], axis=0, ignore_index=True)

        # break

print res
res.to_csv(os.path.join(get_desktop(), 'adsee.csv'), index=False, encoding='gb18030')

"""
#ads > div:nth-child(1) > div.right_a_d_l > p.right_a_d_l_text
#ads > div:nth-child(1) > div.right_a_d_l > div.rank_right_a_img_div > div > div > img
#ads > div:nth-child(720) > div.right_a_d_l > p.right_a_d_l_text
#ads > div:nth-child(1) > div.right_a_d_l > div.rank_right_a_img_div > div > video > source

date
body > div:nth-child(1) > div.right_a_d_l_app > div.right_a_d_l_app_nt > p
message
body > div:nth-child(1) > p.right_a_d_l_text
title
body > div:nth-child(1) > p.right_a_d_l_text_bottom
call to action
body > div:nth-child(1) > a

"""
