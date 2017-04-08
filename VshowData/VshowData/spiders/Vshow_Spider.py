#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import scrapy


class VshowSpider(scrapy.Spider):
    name = 'vshow'

    start_urls = ['http://vshow.me/data/mvData?pn={pn}&rn=10'.format(pn=pn) for pn in range(1, 100000)]

    def parse(self, response):
        yield response
