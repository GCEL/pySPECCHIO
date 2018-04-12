#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 09:36:55 2018

This file takes the .pico spectrometer files and parses them to a numpy
or pandas 

@author: Declan Valters
"""

import json
import pandas as pd
from pandas.io.json import json_normalize

import unittest

class SpectraFile(object):
    SPECTRAFILE = "None"
    SPECTRA_PATH = "None"
    
    def set_spectra_file(self, spectra_filename, spectra_filepath):
        self.SPECTRA_PATH = spectra_filepath
        self.SPECTRAFILE = spectra_filename

    def read_json(self, path, spectra_file):
        """Simple JSON reader"""
        with open(path + spectra_file, "r") as f:
            data = json.load(f)
        return data
    
    def pandas_read_json(self, path, spectra_file):
        """pandas read json to dataframe"""
        with open(path + spectra_file, "r") as f:
            data = json.load(f)
        dataframe = pd.DataFrame(data)
        return dataframe
    
    def pandas_read_json_spectra(self, path, spectra_file):
        """Normalise the results to get the spectra"""
        with open(path + spectra_file, "r") as f:
            data = json.load(f)
            result = json_normalize(data["Spectra"])
        return result
    
    def pandas_read_json_str(self, path, spectra_file):
        """Normalise the results to get the spectra"""
        with open(path + spectra_file, "r") as f:
            data = json.load(f)
        return data
    
    def get_only_spectra_pixels(self, path, spectra_file):
        """Get just the spectra pixels"""
        with open(path + spectra_file, "r") as f:
            data = json.load(f)
            result = json_normalize(data["Spectra"])
        return result["Pixels"]
    
    def valid_spectra(self, spectra_num):
        """Checks the index provided is a valid range for the spectrometer data
        """
        return spectra_num in range(0,4)
    
    def get_spectra_metadata(self, spectra_number):
        """Returns the dict represtning the metadata from the spectra file.
        for ONE of the up/down pairs.
        
        Note the file layout is like this:
            
        Upwelling Spectra [0]
        Upwelling Spectra [1]
        Downwelling Spectra [2]
        Downwelling Spectra [3]
        
        So to get the first upwelling spetra, 0 is used."""
        if not self.valid_spectra(spectra_number):
            raise IndexError("Not a valid spectra number for this spectrometer: [0-3]")
        whole_file = self.read_json()
        # File format has spectra which contains a list of dicts:
        # Metadata [0] and Pixels [1]
        return whole_file['Spectra'][spectra_number]['Metadata']
    
    def get_spectra_pixels(self, spectra_number, path, filename):
        """Returns the dict represtning the metadata from the spectra file.
        for ONE of the up/down pairs.
        
        Note the file layout is like this:
            
        Upwelling Spectra [0]     len = 1044
        Upwelling Spectra [1]     len = 2048
        Downwelling Spectra [2]   len = 1044
        Downwelling Spectra [3]   len = 2048
        
        So to get the first upwelling spetra, 0 is used."""
        if not self.valid_spectra(spectra_number):
            raise IndexError("Not a valid spectra number for this spectrometer: [0-3]")
        whole_file = self.read_json(path, filename)
        # File format has spectra which contains a list of dicts:
        # Metadata [0] and Pixels [1]
        return whole_file['Spectra'][spectra_number]['Pixels']


class spectra_metadata():
    """Stores the metadata for a set of spectra readings"""
    def __init__(self):
        pass

class TestSpectraParser(unittest.TestCase):
    
    def test_valid_sepctra(self):
        sf = SpectraFile()
        for x in range(0,4):
            self.assertTrue(sf.valid_spectra(x))
    
    def test_invalid_spectra(self):
        sf = SpectraFile()
        for item in [1.5, "foobar", 7, -2]:
            self.assertFalse(sf.valid_spectra(item))

if __name__ == "__main__":
    unittest.main()
    
    sf = SpectraFile()
       
    path = '/home/centos/Downloads/'
    filename = 'spectra.csv'
    
    data1 = sf.read_json(path, filename)
    df = sf.pandas_read_json(path, filename)
    df1 = sf.pandas_read_json_str(path, filename)
    df2 = sf.pandas_read_json_spectra(path, filename) # This is getting all four spectra pairs (UP/DOWN)
    pixels = sf.get_only_spectra_pixels(path, filename)
    metadata_upwell_zero = sf.get_spectra_metadata(0)
    
    