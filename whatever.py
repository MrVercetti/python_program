#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

url = raw_input('Enter the url: ')
os.system('you-get -x 127.0.0.1:1080 {url}'.format(url=url))
