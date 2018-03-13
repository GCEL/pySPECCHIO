# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

datadir = "/home/dvalters/Projects/SPECCHIO/DATA/"

def tree_files():
    for (dirname, subdirs, files) in os.walk(datadir):
        print('[' + dirname + ']')
        for fname in files:
            print(os.path.join(dirname, fname))

if __name__=='__main__':
    tree_files()