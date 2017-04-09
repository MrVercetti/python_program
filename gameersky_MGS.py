#!/usr/bin/python
# -*- coding: utf-8 -*-
import re 
import urllib

#定义获取html源码的函数
def getHtml(url): 
    page = urllib.urlopen(url)
    html = page.read()
    return html 

#建立url中变量的集合
looplist = [""]
for i in range(2,27):
    end = "_" + str(i)
    looplist.append(end)

#计数器
x = 0

#正则筛选条件
reg = r'href="http://www.gamersky.com/showimage/id_gamersky.*?(http://img1.*?\.jpg)"><'

for urlend in looplist:
    MGS = "http://pic.gamersky.com/html/229383" + urlend + ".shtml"
    html = getHtml(MGS)
    imglist = re.findall(reg, html)
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, "%s.jpg" % x)
        x+=1
