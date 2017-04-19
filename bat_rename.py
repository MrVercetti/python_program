#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

import os


def bat_rename(file_name):
    global num
    name = '[R_{abi}_{num}]_{size}.{file_type}'.format(abi=abi, num=num, size=size, file_type=file_type)
    os.rename(file_name, name)
    print name
    num += 1


file_type = raw_input('File_type: ')
file_list = [x for x in os.listdir('.') if file_type in x]
num = input('Number: ')
abi = raw_input('Abi code: ')
size = raw_input('Size: ')

for i in file_list:
    bat_rename(i)
