#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 05:14:35 2018

Test suite for the parser modules in pySPECCHIO

@author: DAV
"""

import unittest
import pyspecchio.ancildata_parser as adp
from pyspecchio.spectra_parser import SpectraFile


class testSpectraParser(unittest.TestCase):

    def test_valid_sepctra(self):
        sf = SpectraFile(None, None)
        for x in range(0, 4):
            self.assertTrue(sf.valid_spectra(x))

    def test_invalid_spectra(self):
        sf = SpectraFile(None, None)
        for item in [1.5, "foobar", 7, -2]:
            self.assertFalse(sf.valid_spectra(item))


class testAncilParser(unittest.TestCase):

    DATADIR = "test/DATA/"
    TEST_PRN_DIR = ("test/DATA/ES/field_scale/"
                    "ES_F1_2017/plot_scale_data/LAI/")

    def test_correct_files_parsed(self):

        BAD_STRINGS = ['$', '~', 'csv', 'xls']

        dfs = adp.extract_dataframes(self.DATADIR)
        # Could be the other way round I suppose...
        for bad_string in BAD_STRINGS:
            self.assertFalse(any(bad_string in key for key in dfs.keys()))

    def test_PRN_parsing_columns(self):
        """PRN data should have nine columns if correctly ingested"""
        filefullname = self.TEST_PRN_DIR + "20170714_LAI.PRN"
        adp.extract_PRN_format(filefullname, "TEST_PRN_dict")
        self.assertEqual(len(adp.dataframes['TEST_PRN_dict'].columns), 9)

    def test_PRN_parsing_rows(self):
        """PRN data should have 261 rows if correctly ingested"""
        filefullname = self.TEST_PRN_DIR + "20170714_LAI.PRN"
        adp.extract_PRN_format(filefullname, "TEST_PRN_dict")
        self.assertEqual(len(adp.dataframes['TEST_PRN_dict']), 261)

    def test_PRN_line(self):
        """Test a line has been correctly parsed"""
        filefullname = self.TEST_PRN_DIR + "20170714_LAI.PRN"
        adp.extract_PRN_format(filefullname, "TEST_PRN_dict")

        df_line = adp.dataframes['TEST_PRN_dict'].loc[0]

    def test_generate_PRN_lines(self):
        """Test that we can strip and print the PRN text file lines.
        Print statement around next() is removed now."""
        reader = adp.generate_goodPRNline(
            self.TEST_PRN_DIR + "20170714_LAI.PRN")
        while True:
            try:
                next(reader)
            except StopIteration:
                break

    def test_get_date_from_df_dict(self):
        """Test the date stripper"""
        dfs = adp.extract_dataframes(self.DATADIR)

if __name__ == '__main__':
    unittest.main()
