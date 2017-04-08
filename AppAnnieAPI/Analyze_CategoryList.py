#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pickle

pickle_file = open('category_list.pkl', 'r')
data = pickle.load(pickle_file)
pickle_file.close()

appannie_categories = data.get('categories')
for i in appannie_categories:
    print i