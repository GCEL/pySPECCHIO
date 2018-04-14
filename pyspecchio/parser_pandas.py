# -*- coding: utf-8 -*-
"""
This submodule will parse the raw excel/csv/text files into pandas dataframes
first. Before another module will extract from the dataframes and load into
the database
"""

import os
import re
import unittest
import warnings
import pandas as pd


dataframes = {}

# Names of soil sheets in the Soils directory
SOILS_SUBTABLES = ('Moisture', 'ResinExtracts', 'pH', 'NitrateAmmonia')

# Expected names of ancil data
ANCIL_DATA_NAMES = ('Fluorescence', 'GS', 'Harvest', 'CN', 'HI', 'Height',
                    'LAI', 'SPAD', 'ThetaProbe',
                    'NitrateAmmonia', 'ResinExtracts', 'Moisture', 'pH')


def file_and_dict_name(dirname, fname):
    filefullname = os.path.join(dirname, fname)
    # Get a list of the subdirs, then get the field name folder
    site_code = os.path.relpath(dirname).split(os.path.sep)[3]
    # Take off the year bit, as it is also in the filename later
    site_code = site_code[:-4]
    dictname = site_code + os.path.splitext(os.path.basename(fname))[0]
    return (filefullname, dictname)


def extract_dataframes(directory):
    for (dirname, subdirs, files) in os.walk(directory):
        for fname in files:
            # Only match "xlsx" files, exclude recovery/backup files
            if re.match("^(?![~$]).*.xlsx$", fname):
                # Could be try blocks here:
                try:
                    extract_excel_format(*file_and_dict_name(dirname, fname))
                except ImportError:
                    print("You must have the xlrd python module installed"
                          "...Skipping " + fname)
            if re.match("^(?![~$]).*.PRN$", fname):
                extract_PRN_format(*file_and_dict_name(dirname, fname))
    return dataframes


def extract_excel_format(filefullname, dictname):
    dataframes[dictname] = pd.read_excel(filefullname, skiprows=1)
    if 'Fluorescence' in dictname:
        upper_header = pd.MultiIndex.from_product(
            [['Sample1', 'Sample2',
                'Sample3', 'Sample4', 'Sample5', 'PlotAverage'],
                ['Fo', 'Fv', 'Fm', 'Fv/Fm', 'Fv/Fo']])
        new_header = dataframes[dictname].columns[0:3].union(upper_header)
        dataframes[dictname].columns = new_header
    if dictname in dataframes:
        # Perhaps log as well if duplicate
        warnings.warn("always", UserWarning)
    else:
        dataframes[dictname] = pd.read_excel(filefullname, skiprows=1)


def extract_csv_format(filefullname, dictname):
    if dictname in dataframes:
        # Perhaps log as well if duplicate
        warnings.warn("always", UserWarning)
    else:
        dataframes[dictname] = pd.read_csv(filefullname, skiprows=1)


def extract_PRN_format(filefullname, dictname):
    """This is the raw text file format that comes of the machine"""
    if dictname != "TEST_PRN_dict" and dictname in dataframes:
        # Perhaps log as well if duplicate
        warnings.warn("always", UserWarning)
    else:
        # Build dataframe manually using the generator.
        PRN_dataframe = pd.DataFrame(columns=['Time', 'Plot', 'Sample',
                                              'Transmitted', 'Spread',
                                              'Incident',
                                              'Beam Frac', 'Zenith',  'LAI'])
        for i, line in enumerate(generate_goodPRNline(filefullname)):
            PRN_dataframe.loc[i] = line.split()
        PRN_dataframe = PRN_dataframe.apply(pd.to_numeric, errors='ignore')
        dataframes[dictname] = PRN_dataframe


def generate_goodPRNline(filename):
    """Generator that yields a data line from the PRN file"""
    with open(filename) as f:
        for line in f:
            if line[0].isdigit() and ':' in line:
                yield line


def extract_PRN_header_info():
    pass


def read_PRN_to_dataframe():
    pass


class PRNdata(object):
    """Class that defines the data in a PRN file"""
    pass


class TestParser(unittest.TestCase):

    # DATADIR = "/home/dav/SPECCHIO-QGIS-python/DATA/"
    # DATADIR = "/home/dvalters/Projects/SPECCHIO/DATA/"
    DATADIR = "/home/centos/Python/test/DATA/"

    # TEST_PRN_DIR = ("/home/dav/SPECCHIO-QGIS-python/DATA/ES/field_scale/"
    #                "ES_F1_2017/plot_scale_data/LAI/")
    # TEST_PRN_DIR = ("/home/dvalters/Projects/SPECCHIO/DATA/ES/field_scale/"
    #                "ES_F1_2017/plot_scale_data/LAI/")
    TEST_PRN_DIR = ("/home/centos/Python/test/DATA/ES/field_scale/"
                    "ES_F1_2017/plot_scale_data/LAI/")

    def test_correct_files_parsed(self):

        BAD_STRINGS = ['$', '~', 'csv', 'xls']

        dfs = extract_dataframes(self.DATADIR)
        # Could be the other way round I suppose...
        for bad_string in BAD_STRINGS:
            self.assertFalse(any(bad_string in key for key in dfs.keys()))

    def test_PRN_parsing_columns(self):
        """PRN data should have nine columns if correctly ingested"""
        filefullname = self.TEST_PRN_DIR + "20170714_LAI.PRN"
        extract_PRN_format(filefullname, "TEST_PRN_dict")
        self.assertEqual(len(dataframes['TEST_PRN_dict'].columns), 9)

    def test_PRN_parsing_rows(self):
        """PRN data should have 261 rows if correctly ingested"""
        filefullname = self.TEST_PRN_DIR + "20170714_LAI.PRN"
        extract_PRN_format(filefullname, "TEST_PRN_dict")
        self.assertEqual(len(dataframes['TEST_PRN_dict']), 261)

    def test_PRN_line(self):
        """Test a line has been correctly parsed"""
        filefullname = self.TEST_PRN_DIR + "20170714_LAI.PRN"
        extract_PRN_format(filefullname, "TEST_PRN_dict")

        df_line = dataframes['TEST_PRN_dict'].loc[0]

    def test_generate_PRN_lines(self):
        """Test that we can strip and print the PRN text file lines.
        Print statement around next() is removed now."""
        reader = generate_goodPRNline(self.TEST_PRN_DIR + "20170714_LAI.PRN")
        while True:
            try:
                next(reader)
            except StopIteration:
                break

if __name__ == '__main__':
    unittest.main()
