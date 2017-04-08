#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import pickle

from furl import furl

pickle_file = open('ASO_links.pkl', 'r')
data = pickle.load(pickle_file)
pickle_file.close()
data = map(lambda x: furl(x).path.segments[-2], data)

