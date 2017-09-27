#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import os
import _winreg
import pandas as pd


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0]


name = raw_input('Enter file name: ')
files = [x for x in os.listdir('.') if 'csv' in x]
joint_list = map(pd.read_csv, files)
df = pd.concat(joint_list, axis=0, ignore_index=True)
store_path = os.path.join(get_desktop(), '{name}.csv'.format(name=name))
df.to_csv(store_path, index=False, encoding='utf-8')
print 'Done!'
