#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 05:14:35 2018

Test suite for the parser modules in pySPECCHIO

@author: DAV
"""

import unittest

from pyspecchio.spectra_parser import SpectraFile 

class testSpectraParser(unittest.TestCase):    

    def test_valid_sepctra(self):
        sf = SpectraFile(None, None)
        for x in range(0,4):
            self.assertTrue(sf.valid_spectra(x))
    
    def test_invalid_spectra(self):
        sf = SpectraFile(None, None)
        for item in [1.5, "foobar", 7, -2]:
            self.assertFalse(sf.valid_spectra(item))
            
if __name__ == '__main__':
    unittest.main()
