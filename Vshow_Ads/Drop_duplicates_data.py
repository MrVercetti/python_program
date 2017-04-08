#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pandas as pd

df = pd.read_csv('C:/Users/donq2/Desktop/vshow_data.csv')
df = df.drop_duplicates('v_id')
print df
df.to_csv('C:/Users/donq2/Desktop/vshow_DropDuplicates.csv', index=False, encoding='utf-8')