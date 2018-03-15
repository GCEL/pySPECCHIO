# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import re
import pandas as pd

datadir = "/home/dvalters/Projects/SPECCHIO/DATA/"

dataframes = {}
csvs = []



def tree_files():
    for (dirname, subdirs, files) in os.walk(datadir):
        #print('[' + dirname + ']')
        for fname in files:
            if re.match("^.*.xlsx$", fname):
                filefullname = os.path.join(dirname, fname)
                #print(filefullname)
                dictname = os.path.splitext(os.path.basename(fname))[0]
                print(dictname)
                dataframes[dictname] = pd.read_excel(filefullname)

if __name__=='__main__':
    tree_files()