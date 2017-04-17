#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import datetime
import re
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from furl import furl


def get_data(url):
    global date

    # 日期
    date = furl(url)
    date.path.segments.pop(0)
    date = "/".join(date.path.segments)
    # print date

    indeks_data = s.get(url).text
    indeks_soup = BeautifulSoup(indeks_data, 'lxml')
    article_numbers = re.findall(r'article_\d{7}', indeks_data)

    # CSS路径
    selector_titles = ["#{article_number} > aside > header > h4 > a > span".format(article_number=article_number) for
                       article_number in article_numbers]
    selector_tags = ["#{article_number} > aside > header > a ".format(article_number=article_number) for
                     article_number in article_numbers]
    selector_links = ["#{article_number} > aside > header > h4 > a ".format(article_number=article_number) for
                      article_number in article_numbers]

    # 首页标题，标签，链接合集
    titles = map(indeks_soup.select, selector_titles)
    tags = map(indeks_soup.select, selector_tags)
    links = map(indeks_soup.select, selector_links)
    for title, tag, link in zip(titles, tags, links):
        get_read_data(title, tag, link)


def get_read_data(title, tag, link):
    global df, error_times, share_count, image, comments_count, adult_popup
    try:
        title = title[0].get_text()
        link = link[0].attrs["href"]
        # print
        # print link
        read_data = s.get(link).text
        read_soup = BeautifulSoup(read_data, 'lxml')

        # 获取分享数量
        share_count = read_soup.find("span", {"class": 'read-page--social-share__share-count-value'}).get_text()
        # print share_count

        # 获取图像链接，空集为视频
        try:
            gallery_image_num = re.findall(r'gallery-image-\d{,8}', read_data)[0]
            # print gallery_image_num
            selector_image = '#{gallery_image_num} > div > a > picture > source > source'.format(
                gallery_image_num=gallery_image_num)
            image = read_soup.select(selector_image)
            # print image
            try:
                image = [image[0].attrs['data-srcset'].split(',')[1].split(' ')[1]]
            except KeyError:
                image = [image[0].attrs['srcset'].split(',')[1].split(' ')[1]]
        except IndexError, e:
            image = []
            # print image
        # break

        # 获取评论数量
        open_conversation_button_num = re.findall(r'open-conversation-button-\d{,8}', read_data)[0]
        # print open_conversation_button_num
        selector_comments_count = "#{open_conversation_button_num} > span".format(
            open_conversation_button_num=open_conversation_button_num)
        # print selector_comments_count
        comments_count = read_soup.select(selector_comments_count)[0].get_text()
        # print comments_count

        adult_popup = read_soup.find('p', {'class': 'adult-popup__age'})
        if adult_popup:
            adult_popup = adult_popup.get_text()
        else:
            adult_popup = u'Just For Kids'
            # print adult_popup

            # print
    except Exception:
        error_times += 1
        if error_times == 4:
            share_count = u''
            print share_count
            image = []
            comments_count = u''
            adult_popup = u''
            error_times = 0
        else:
            time.sleep(5)
            get_read_data(title, tag, link)

    # 打包数据
    data = {
        'date': date,
        'title': title,
        'link': link,
        'share_count': share_count,
        'image': image,
        'comments_count': comments_count,
        'adult_popup': adult_popup,
    }
    if tag:
        data['tag'] = tag[0].get_text()
    else:
        data['tag'] = ''
    # print data
    df_data = pd.DataFrame(data)
    df = pd.concat([df, df_data], axis=0, ignore_index=True)
    # print df


# 处理url日期参数
How_long = int(raw_input('How long: '))
dates = [
    [(datetime.datetime.now() - datetime.timedelta(i)).strftime(("%Y,%m,%d"))][0].split(',')
    for i in
    range(1, 1 + How_long)]
for i in range(How_long):
    dates[i].insert(0, 'indeks')

# 建立url_list
url_list = []
host = 'http://www.liputan6.com/'
f = furl(host)
for i in range(How_long):
    f.path.segments = dates[i]
    for j in range(1, 16):
        f.set({'page': j}).url
        url_list.append(f.url)

s = requests.session()
error_times = 0
df = pd.DataFrame(columns=[u'comments_count', u'date', u'image', u'link', u'share_count', u'tag', u'title'])
for i in url_list:
    get_data(i)
    full_url = furl(i)
    full_url.path.segments.pop(0)
    date = ".".join(full_url.path.segments)
    page = full_url.args['page']
    df.to_csv('liputan6_data/liputan6_{date}_page{page}.csv'.format(date=date, page=page), index=False,
              encoding='utf-8')
    print df
    df = pd.DataFrame(columns=[u'comments_count', u'date', u'image', u'link', u'share_count', u'tag', u'title'])
