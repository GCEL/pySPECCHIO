#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 09:36:55 2018

This file takes the .pico spectrometer files and parses them to a numpy
or pandas

@author: Declan Valters
"""

import json
import os
import pandas as pd
from pandas.io.json import json_normalize


class SpectraFile(object):
    def __init__(self, spectrafile, spectrapath):
        self.sfile = spectrafile
        self.spath = spectrapath

    def read_json(self):
        """Simple JSON reader"""
        with open(self.spath + self.sfile, "r") as f:
            data = json.load(f)
        return data

    def pandas_read_json(self):
        """pandas read json to dataframe"""
        with open(self.spath + self.sfile, "r") as f:
            data = json.load(f)
        dataframe = pd.DataFrame(data)
        return dataframe

    def pandas_read_json_spectra(self):
        """Normalise the results to get the spectra"""
        with open(self.spath + self.sfile, "r") as f:
            data = json.load(f)
            result = json_normalize(data["Spectra"])
        return result

    def pandas_read_json_str(self):
        """Normalise the results to get the spectra"""
        with open(self.spath + self.sfile, "r") as f:
            data = json.load(f)
        return data

    def get_only_spectra_pixels(self):
        """Get just the spectra pixels"""
        with open(self.spath + self.sfile, "r") as f:
            data = json.load(f)
            result = json_normalize(data["Spectra"])
        return result["Pixels"]

    def valid_spectra(self, spectra_num):
        """Checks the index provided is a valid range for the spectrometer data
        """
        return spectra_num in range(0, 4)

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
            raise IndexError(
                "Not a valid spectra number for this spectrometer: [0-3]")
        whole_file = self.read_json()
        # File format has spectra which contains a list of dicts:
        # Metadata [0] and Pixels [1]
        return whole_file['Spectra'][spectra_number]['Metadata']

    def get_spectra_pixels(self, spectra_number):
        """Returns the dict represtning the metadata from the spectra file.
        for ONE of the up/down pairs.

        Note the file layout is like this:

        Upwelling Spectra [0]     len = 1044
        Upwelling Spectra [1]     len = 2048
        Downwelling Spectra [2]   len = 1044
        Downwelling Spectra [3]   len = 2048

        So to get the first upwelling spetra, 0 is used."""
        if not self.valid_spectra(spectra_number):
            raise IndexError(
                "Not a valid spectra number for this spectrometer: [0-3]")
        whole_file = self.read_json()
        # File format has spectra which contains a list of dicts:
        # Metadata [0] and Pixels [1]
        return whole_file['Spectra'][spectra_number]['Pixels']

class DummySpectraFile(SpectraFile):
    """Class that contains dummy spectra for when Metadata have no assoc.
    pico file but need to be inserted into SPECCHIO.
    """
    DUMMY_PICO_SPECTRA = """{
 "SequenceNumber": 0,
 "Spectra": [
  {
   "Metadata": {
    "Batch": 0,
    "Dark": false,
    "Datetime": "2000-01-00T00:00:00.000000Z",
    "Direction": "none",
    "IntegrationTime": 0.0,
    "IntegrationTimeUnits": "none",
    "NonlinearityCorrectionCoefficients": [0],
    "OpticalPixelRange": [0],
    "Run": "dummy",
    "SaturationLevel": 0,
    "SerialNumber": "QEP01651",
    "TemperatureDetectorActual": 0.0,
    "TemperatureDetectorSet": 0.0,
    "TemperatureHeatsink": null,
    "TemperatureMicrocontroller": 0.0,
    "TemperaturePCB": 0.0,
    "TemperatureUnits": "degrees Celcius",
    "Type": "light",
    "WavelengthCalibrationCoefficients": [0],
    "name": "none"
   },
   "Pixels": [0] }}"""

    def __init__(self, dummyspecfile, dummyspecpath):
        self.dummyfile = dummyspecfile
        self.dummspecpath = dummyspecpath
        self.generate_dummy_spectra_for_ancil(self.dummspecpath, self.dummyfile)

    def get_date_from_df_key(self, df):
        return df.split('_')[2]

    @classmethod
    def generate_dummy_spectra_for_ancil(self, pico_dir, dummy_pico_name):
        """Write dummy spectra files to disk"""
        if not os.path.isdir(pico_dir):
            os.mkdir(pico_dir)
        if not os.path.exists(pico_dir + dummy_pico_name):
            with open(pico_dir + dummy_pico_name, "w") as dummypico:
                dummypico.writelines(self.DUMMY_PICO_SPECTRA)

    def get_dummy_pico_name(self):
        pass


class spectra_metadata():
    """Stores the metadata for a set of spectra readings"""
    def __init__(self):
        pass

if __name__ == "__main__":

    path = '/home/centos/Downloads/'
    filename = 'spectra.csv'

    # Create a spectra file object
    sf = SpectraFile(filename, path)

    # Test the parse methods
    data1 = sf.read_json()
    df = sf.pandas_read_json()
    df1 = sf.pandas_read_json_str()
    # This is getting all four spectra pairs (UP/DOWN)
    df2 = sf.pandas_read_json_spectra()

    pixels = sf.get_only_spectra_pixels()
    metadata_upwell_zero = sf.get_spectra_metadata(0)
