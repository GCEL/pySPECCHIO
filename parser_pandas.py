# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import re
import unittest
import pandas as pd

datadir = "/home/dvalters/Projects/SPECCHIO/DATA/"

dataframes = {}
csvs = []



def extract_dataframes():
    for (dirname, subdirs, files) in os.walk(datadir):
        #print('[' + dirname + ']')
        for fname in files:
            # Only match "xlsx" files, exclude recovery/backup files
            if re.match("^(?![~$]).*.xlsx$", fname):
                filefullname = os.path.join(dirname, fname)
                #print(filefullname)
                dictname = os.path.splitext(os.path.basename(fname))[0]
                print(dictname)
                dataframes[dictname] = pd.read_excel(filefullname)
    return dataframes

    
class TestParser(unittest.TestCase):
    
    def test_correct_files_parsed(self):

        BAD_STRINGS = ['$', '~', 'csv', 'xls']
        
        dfs = extract_dataframes()
        # Could be the other way round I suppose...
        for bad_string in BAD_STRINGS:
            self.assertFalse(any(bad_string in key for key in dfs.keys()))


if __name__=='__main__':
    unittest.main()