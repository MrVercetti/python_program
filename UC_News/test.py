#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import datetime
import requests
import pandas as pd
from furl import furl


def datelist(start, end):
    start_date = datetime.date(*start)
    end_date = datetime.date(*end)

    result = []
    curr_date = start_date
    while curr_date != end_date:
        result.append([curr_date.year, curr_date.month, curr_date.day])
        curr_date += datetime.timedelta(1)
    result.append([curr_date.year, curr_date.month, curr_date.day])
    return result


date = [[(datetime.datetime.now() - datetime.timedelta(i)).strftime(("%Y,%m,%d"))][0].split(',') for i in
        range(1, 1 + 30)]
# date = [i[0].split(',') for i in date]
# print date
# print len(date)

df = pd.DataFrame(columns=[u'comments_count', u'image', u'link', u'share_count', u'tag', u'title'])
# print df.index

url = 'http://www.liputan6.com/indeks/2017/03/04?page=7'
full_url = furl(url)
full_url.path.segments.pop(0)
date = ".".join(full_url.path.segments)
page = full_url.args['page']

# print date, page
#
How_long = 90-17
dates = [[(datetime.datetime.now() -datetime.timedelta(17) -datetime.timedelta(i)).strftime(("%Y,%m,%d"))][0].split(',') for i in
         range(1, 1 + How_long)]
for i in dates:
    print i



# for i in dir(df.index):
#     print i

# a = furl('http://www.liputan6.com/indeks/2017/03/04?page=8')
# print a.path.segments.pop(0)
#
# print "/".join(a.path.segments)