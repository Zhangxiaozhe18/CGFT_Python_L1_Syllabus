#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' my first module '

__author__ = 'CGFT'

import sys

def hello_method():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    hello_method()