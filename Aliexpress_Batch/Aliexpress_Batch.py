#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pandas as pd

df = pd.read_csv('export_20170402_1449.csv', sep='\t', encoding='utf-16-le')

# for adset_name in df['Ad Set Name']:
#     if 'Auto' in adset_name:
#         i = adset_name
#         if '-' in i.split('_')[-1].split(' '):
#             j = i.split('_')[-1].split(' ')
#             j = map(lambda x: x.capitalize(), j)
#             j = ''.join(j)
#             print j

for adset_name in df['Ad Set Name']:
    i = adset_name.split('_')[-1]
    i = map(lambda x: x.capitalize(), i.split(' '))
    i = '-'.join(i)
    print i