#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

client = pymongo.MongoClient('localhost', 27017)
walden = client['walden']
sheet_tab = walden['sheet_tab']

# with open('walden.txt', 'r') as f:
#     lines = f.readlines()
#     for index, line in enumerate(lines):
#         data = {
#             'index': index,
#             'line': line,
#             'words': len(line.split())
#         }
#         sheet_tab.insert_one(data)

for item in sheet_tab.find({'words': 0}):
    print item
