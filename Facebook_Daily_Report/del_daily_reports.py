#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import os

base = 'C:/Users/donq2/Downloads/'
files_names = [x for x in os.listdir(base) if 'Appcoach' in x]
files = map(lambda x: os.path.join(base, x.decode('gbk')), files_names)
map(os.remove, files)
print "Done~"
