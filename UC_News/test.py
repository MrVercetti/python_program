#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import datetime


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


date = [[(datetime.datetime.now() - datetime.timedelta(i)).strftime(("%Y,%m,%d"))][0].split(',') for i in range(1, 1 + 30)]
# date = [i[0].split(',') for i in date]
print date
print len(date)
