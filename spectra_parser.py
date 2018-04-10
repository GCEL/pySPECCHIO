#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 09:36:55 2018

This file takes the .pico spectrometer files and parses them to a numpy
or pandas 

@author: centos
"""

import json
import pandas as pd
from pandas.io.json import json_normalize

import unittest

path = "/home/centos/Downloads/DATA/Spectra_dir/"
spectra_file_test = "QEP1USB1_b000000_s000002_light.pico"

def read_json():
    """Simple JSON reader"""
    with open(path + spectra_file_test, "r") as f:
        data = json.load(f)
    return data

def pandas_read_json():
    """pandas read json to dataframe"""
    with open(path + spectra_file_test, "r") as f:
        data = json.load(f)
    dataframe = pd.DataFrame(data)
    return dataframe

def pandas_read_json_spectra():
    """Normalise the results to get the spectra"""
    with open(path + spectra_file_test, "r") as f:
        data = json.load(f)
        result = json_normalize(data["Spectra"])
    return result

def pandas_read_json_str():
    """Normalise the results to get the spectra"""
    with open(path + spectra_file_test, "r") as f:
        data = json.load(f)
    return data

def get_only_spectra_pixels():
    """Get just the spectra pixels"""
    with open(path + spectra_file_test, "r") as f:
        data = json.load(f)
        result = json_normalize(data["Spectra"])
    return result["Pixels"]

def valid_spectra(spectra_num):
    """Checks the index provided is a valid range for the spectrometer data
    """
    return spectra_num in range(0,4)

def get_spectra_metadata(spectra_number):
    """Returns the dict represtning the metadata from the spectra file.
    for ONE of the up/down pairs.
    
    Note the file layout is like this:
        
    Upwelling Spectra [0]
    Upwelling Spectra [1]
    Downwelling Spectra [2]
    Downwelling Spectra [3]
    
    So to get the first upwelling spetra, 0 is used."""
    if not valid_spectra(spectra_number):
        raise IndexError("Not a valid spectra number for this spectrometer: [0-3]")
    whole_file = read_json()
    # File format has spectra which contains a list of dicts:
    # Metadata [0] and Pixels [1]
    return whole_file['Spectra'][spectra_number]['Metadata']

def get_spectra_pixels(spectra_number):
    """Returns the dict represtning the metadata from the spectra file.
    for ONE of the up/down pairs.
    
    Note the file layout is like this:
        
    Upwelling Spectra [0]     len = 1044
    Upwelling Spectra [1]     len = 2048
    Downwelling Spectra [2]   len = 1044
    Downwelling Spectra [3]   len = 2048
    
    So to get the first upwelling spetra, 0 is used."""
    if not valid_spectra(spectra_number):
        raise IndexError("Not a valid spectra number for this spectrometer: [0-3]")
    whole_file = read_json()
    # File format has spectra which contains a list of dicts:
    # Metadata [0] and Pixels [1]
    return whole_file['Spectra'][spectra_number]['Pixels']


class spectra_metadata():
    """Stores the metadata for a set of spectra readings"""
    def __init__(self):
        pass

class TestSpectraParser(unittest.TestCase):
    
    def test_valid_sepctra(self):
        for x in range(0,4):
            self.assertTrue(valid_spectra(x))
    
    def test_invalid_spectra(self):
        for item in [1.5, "foobar", 7, -2]:
            self.assertFalse(valid_spectra(item))

if __name__ == "__main__":
    unittest.main()
    
    data1 = read_json()
    df = pandas_read_json()
    df1 = pandas_read_json_str()
    df2 = pandas_read_json_spectra() # This is getting all four spectra pairs (UP/DOWN)
    pixels = get_only_spectra_pixels()
    metadata_upwell_zero = get_spectra_metadata(0)
    
    