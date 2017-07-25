#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import _winreg
import os


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0].encode('utf-8')


file_path = os.path.join(get_desktop(), 'shit.txt')
print file_path

with open(file_path, 'r') as fp:
    for line in fp.readlines():
        print line
