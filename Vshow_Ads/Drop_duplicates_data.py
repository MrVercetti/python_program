#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pandas as pd
import _winreg
import os


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0]


df = pd.read_csv('vshow_data/vshow_data.csv')
df = df.drop_duplicates('v_id')
print df

df.to_csv(os.path.join(get_desktop(), 'vshow_DropDuplicates.csv'), index=False, encoding='utf-8')
