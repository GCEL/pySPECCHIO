# -*- coding: utf-8 -*-
"""
This submodule will parse the raw excel/csv/text files into pandas dataframes
first. Before another module will extract from the dataframes and load into
the database
"""

import os
import re
import unittest
import pandas as pd

DATADIR = "/home/dvalters/Projects/SPECCHIO/DATA/"

dataframes = {}

def file_and_dict_name(dirname, fname):
    filefullname = os.path.join(dirname, fname)
    dictname = os.path.splitext(os.path.basename(fname))[0]
    return (filefullname, dictname)

def extract_dataframes():
    for (dirname, subdirs, files) in os.walk(DATADIR):
        #print('[' + dirname + ']')
        for fname in files:
            # Only match "xlsx" files, exclude recovery/backup files
            if re.match("^(?![~$]).*.xlsx$", fname):
            # Could be try blocks here:
                extract_excel_format(*file_and_dict_name(dirname, fname))
            if re.match("^(?![~$]).*.PRN$", fname):
                extract_PRN_format(*file_and_dict_name(dirname, fname))
    return dataframes

def extract_excel_format(filefullname, dictname):
    dataframes[dictname] = pd.read_excel(filefullname, skiprows=1)
    
def extract_csv_format(filefullname, dictname):
    dataframes[dictname] = pd.read_csv(filefullname, skiprows=1)

def extract_PRN_format(filefullname, dictname):
    """This is the raw text file format that comes of the machine"""
    dataframes[dictname] = pd.read_table(filefullname, header=[7], delim_whitespace=True)
    
    
    
class TestParser(unittest.TestCase):
    
    def test_correct_files_parsed(self):

        BAD_STRINGS = ['$', '~', 'csv', 'xls']
        
        dfs = extract_dataframes()
        # Could be the other way round I suppose...
        for bad_string in BAD_STRINGS:
            self.assertFalse(any(bad_string in key for key in dfs.keys()))
    
    def test_PRN_parsing(self):
        filefullname = "/home/dvalters/Projects/SPECCHIO/DATA/ES/field_scale/ES_F1_2017/plot_scale_data/LAI/20170714_LAI.PRN"
        extract_PRN_format(filefullname, "TEST_PRN_dict")
        self.assertEquals(len(dataframes['TEST_PRN_dict'].columns), 9)

if __name__=='__main__':
    unittest.main()
