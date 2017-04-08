#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pickle

pickle_file = open('country_list.pkl', 'r')
data = pickle.load(pickle_file)
pickle_file.close()
country_list = data.get('country_list')
print len(country_list)
for i in country_list:
    print i
