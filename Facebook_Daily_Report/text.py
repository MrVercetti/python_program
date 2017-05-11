#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import _winreg
import os


def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    desktop = _winreg.QueryValueEx(key, "Desktop")[0]
    home = os.path.split(desktop)[0]
    return os.path.join(home, 'Downloads')


fuck = get_desktop()
print fuck
