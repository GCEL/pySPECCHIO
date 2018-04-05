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

path = "/home/centos/Downloads/DATA/Spectra_dir/"
spectra_file_test = "QEP1USB1_b000000_s000002_light.pico"

def read_json():
    """Simple JSON reader"""
    with open(path + spectra_file_test, "r") as f:
        data = json.load(f)
        print(type(data))
        return data

def pandas_read_json():
    """pandas read json to dataframe"""
    with open(path + spectra_file_test, "r") as f:
        data = json.load(f)
    dataframe = pd.DataFrame(data)
    return dataframe

if __name__ == "__main__":
    data1 = read_json()
    df = pandas_read_json()
    