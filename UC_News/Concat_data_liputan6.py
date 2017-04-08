#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import datetime

import os
import pandas as pd

base = 'liputan6_data'
files_names = [x for x in os.listdir(base) if 'liputan6' in x]
files = map(lambda x: os.path.join(base, x), files_names)
joint_list = map(pd.read_csv, files)
res = pd.concat(joint_list, axis=0, ignore_index=True)
path = 'C:/Users/donq2/Desktop/liputan6_data_{date}.csv'.format(date=datetime.datetime.now().strftime(("%Y-%m-%d")))
res.to_csv(path, index=False, encoding='utf-8')
print "Done!"
