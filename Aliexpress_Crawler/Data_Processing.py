#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pandas as pd

df = pd.read_csv('Aliexpress-Dresses.csv')

for i in df.index:
    price = float(df.loc[i, 'price'].split('-')[0].split('$')[1])
    price = str(round(price * 3.15, 2)).split('.')
    price = ','.join(price)
    price = 'R$ ' + price
    # print price
    df.loc[i, 'price'] = price

print df

df.to_csv('fuck.csv', index=False, encoding='utf-8')
