#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"
import os

with open('vshowdrop.txt', 'r') as fp:
    for line in fp.readlines():
        os.remove(line.strip())
        print line.strip(), 'Done~'
