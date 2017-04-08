#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import datetime

import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def image_processing(image_path, title):
    global index_number
    # 打开广告素材并调整尺寸
    img_original = Image.open(image_path)
    if img_original.size == (1200, 628):
        width, height = img_original.size
    elif img_original.size == (1280, 710):
        img_original.thumbnail((1200, 666))
        width, height = img_original.size
        img_original = img_original.crop((0, 19, width, height - 18))
        width, height = img_original.size  # width: 1200, height: 628
    # img_original.show()

    # 新建黄色封面并粘贴
    img_cover = Image.new("RGB", (1200, 190), (253, 196, 25))
    img_cover = Image.new("RGB", (1200, 190), (253, 0, 0))
    # img_cover.show()
    img_original.paste(img_cover, (0, 475))
    # img_original.show()

    # 打开UClogo，调整尺寸并粘贴
    img_uclogo = Image.open('uclogo.png')
    img_uclogo.thumbnail((120, 120))
    # img_uclogo.show()
    img_original.paste(img_uclogo, (20, 490), mask=img_uclogo)
    # img_original.show()

    # 打开GPlogo，调整尺寸并粘贴
    img_gplogo = Image.open('gplogo.png')
    img_gplogo.thumbnail((int(img_gplogo.size[0] / 2.5), int(img_gplogo.size[1] / 2.5)))
    # img_gplogo.show()
    img_original.paste(img_gplogo, (940, 380), mask=img_gplogo)
    # img_original.show()

    # 写入标题
    draw = ImageDraw.Draw(img_original)
    if len(title) < 38:  # 一行字符不要超过38
        font = ImageFont.truetype('C:\Windows\Fonts\consola.ttf', 50)
        draw.text((170, 530), title, (255, 255, 255), font=font)
    else:
        title_words = title.split(' ')
        # print title_words
        for i in range(len(title_words) + 1):
            if len(' '.join(title_words[:i])) < 44:  # 两行字符不要超过44
                title1 = ' '.join(title_words[:i])
                title2 = ''
                # print title1
            else:
                title2 = ' '.join(title_words[i - 1:])
                # print title2
                break

        font = ImageFont.truetype('C:\Windows\Fonts\consola.ttf', 42)
        draw.text((160, 510), title1, (255, 255, 255), font=font)
        draw.text((160, 560), title2, (255, 255, 255), font=font)
    # img_original.show()

    # 存储图片
    image_store_path = os.path.join(store_path, 'UCNews{index_number}_{date}.jpg'.format(index_number=index_number,
                                                                                         date=datetime.datetime.now().strftime(
                                                                                             ("%Y-%m-%d"))))
    img_original.save(image_store_path)
    print 'Done', image_store_path
    index_number += 1


# 图片索引编号
index_number = 1

# 创建存储路径
store_path = 'C:/Users/donq2/Desktop/UCNewsAD_{date}'.format(date=datetime.datetime.now().strftime(("%Y-%m-%d")))
os.mkdir(store_path)

if __name__ == '__main__':
    image_processing('1.jpg', '8 Hal Menakjubkan tentang Klitoris yang Perlu Diketahui Wanita')
