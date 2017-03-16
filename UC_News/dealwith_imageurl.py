#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def parse_image(src):
    Soup = BeautifulSoup(src, 'lxml')
    df['image_url']=Soup.select('body > source > source')[0]['data-srcset'].split(',')[1].split(' ')[1]
    print df['image_url']

df = pd.read_csv('C:/Users/donq2/Desktop/liputan6_data_data.csv')
src = df['image']
# print src
df['hehe']=1

df['xixi'] = df['hehe'].pipe(sum, 4)
print df['xixi'] ,df['hehe']
# parse_image(src)

# Soup = BeautifulSoup(src, 'lxml')
# print Soup.select('body > source > source')[0]['data-srcset'].split(',')[1].split(' ')[1]