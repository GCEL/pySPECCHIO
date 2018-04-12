#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 05:14:35 2018

Test suite for the parser modules in pySPECCHIO

@author: DAV
"""

import unittest

from pyspecchio import spectra_parser

class testSpectraParser(unittest.TestCase):
    
    def test_valid_sepctra(self):
        for x in range(0,4):
            self.assertTrue(spectra_parser.valid_spectra(x))
    
    def test_invalid_spectra(self):
        for item in [1.5, "foobar", 7, -2]:
            self.assertFalse(spectra_parser.valid_spectra(item))
            
if __name__ == '__main__':
    unittest.main()
