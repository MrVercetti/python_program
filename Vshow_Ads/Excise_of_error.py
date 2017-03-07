#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "DonQ"

##try:
##    print 'try...'
##    r = 10 / 0
##    print 'result:', r
##except ZeroDivisionError, e:
##    print 'except:', e
##finally:
##    print 'finally...'
##print 'END'

index = 0
def calc():
    global index
    try:
        print "haha"
        print 1/0
        print 'hehe'
    except ZeroDivisionError, e:
        print "ZeroDivisionError", e
        index += 1
        if index == 3:
            print "I can't solve thie problem."
            index = 0
        else:
            calc()

if __name__=='__main__':
    calc()