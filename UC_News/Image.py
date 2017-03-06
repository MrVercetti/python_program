#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

im1 = Image.open('218493_620.jpg')
im1 = im1.convert("RGBA")
im2 = Image.new('RGBA', (620, 80), (253, 196, 25))
im_UC_logo = Image.open('logo.png')
w, h = im_UC_logo.size
im_UC_logo.thumbnail((w // 5, h // 5))
im_GP_logo = Image.open('GPLOGO.png')
w, h = im_GP_logo.size
im_GP_logo.thumbnail((w // 4.2, h // 4.2))
im1.paste(im2, (0, 275))
im1.paste(im_UC_logo, (10, 280))
im1.paste(im_GP_logo, (470, 220))
draw = ImageDraw.Draw(im1)
font = ImageFont.truetype('C:\Windows\Fonts\MyriadPro-Regular.otf', 35)
draw.text((80, 300), "I love daily report.", (255, 255, 255), font=font)
print im1.size
im1.show()
