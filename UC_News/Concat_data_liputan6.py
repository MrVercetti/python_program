#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pandas as pd
import os

base = 'liputan6_data'
files_names = [x for x in os.listdir(base) if 'liputan6' in x]
files = map(lambda x: os.path.join(base, x), files_names)
joint_list = map(pd.read_csv, files)
res = pd.concat(joint_list, axis=0, ignore_index=True)
res.to_csv('C:/Users/donq2/Desktop/liputan6_data_data.csv', index=False, encoding='utf-8')
print "Done!"