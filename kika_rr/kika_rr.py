#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import os

import pandas as pd

base = 'C:/Users/donq2/Downloads/kika2'
files_names = [x for x in os.listdir(base) if 'appcoachs' in x]
files = map(lambda x: os.path.join(base, x), files_names)
joint_list = map(lambda x: pd.read_excel(x, sheetname='fb_appcoach_kika'), files)
res = pd.concat(joint_list, axis=0, ignore_index=True)
# res.to_csv('C:/Users/donq2/Desktop/kika.csv', index=False, encoding='gbk')
print res
