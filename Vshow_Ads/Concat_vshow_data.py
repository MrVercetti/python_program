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


def concat2csv(x, y):
    return pd.concat([x, y], axis=0, ignore_index=True)


base = 'vshow_data'
files_names = [x for x in os.listdir(base) if 'vshow' in x]
files = map(lambda x: os.path.join(base, x), files_names)
joint_list = map(pd.read_csv, files)
res = reduce(concat2csv, joint_list)
store_path = os.path.join(get_desktop(), 'vshow_data.csv')
res.to_csv(store_path, index=False, encoding='utf-8')
print "Done"
