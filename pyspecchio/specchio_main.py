# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:14:32 2018

@author: dvalters

SPECCHIO driver

Coordinates the parsing and uploading of the spectral data to the SPECCHIO d
database


"""
import sys
import argparse

import specchio_db_interface as specchio
import ancildata_parser as ancilparser

"""Read in from command line, datadir, pico spectra dir or files.,
Date since for new files.
Get DB interface from a config file
"""
parser = argparse.ArgumentParser(description='Process data files to be'
                                 'uploaded to the SPECCHIO database.')
parser.add_argument('ancilpath', metavar='PATH', type=str, nargs='+',
                    help='The path to the ancillary data files'
                    '(Plot-level data that are not spectra files.)')
parser.add_argument('spectrapath', metavar='PATH', type=str, nargs='+',
                    help='The path to the PICO Spectra (.pico) files')
parser.add_argument('--use-dummy-spectra', dest='use_dummy_spectra',
                    action='store_const',
                    const=True, default=True,
                    help='Generate dummy spectra for ancillary data files.'
                    'This option will generate dummy spectra files if none are'
                    'asscoiated with the data files provided. Dummy spectra'
                    'are required due to the design of the SPECCHIO software,'
                    'which is centred around the spectra files.\n'
                    'Dummy spectra will be written to disk.')
parser.add_argument('--test-mode', dest='test_mode',
                    action='store_const',
                    const=True, default=True,
                    help='Runs the program in test mode, using the data from'
                    'the test directory, uploading it to a test campaign.\n'
                    'No further arguments are required.')

args = parser.parse_args()
print(args)


def test_upload_sample_data():
    specchio.specchio_uploader_test()


def new_data():
    """Check for new data in the data dir"""
    # Could invlove a database query as well?
    # Don't waste time overwriting exsiting data
    return True


def main():

    campaign_name = "Python test campaign"
    db_interface = specchio.specchioDBinterface(campaign_name)

    # filepath = '/home/centos/Downloads/'
    # filename = 'spectra.csv'
    ancil_testpath = "../test/DATA/"

    spectra_testpath = "../test/PICO_testdata/"
    spectra_file_test = "QEP1USB1_b000000_s000002_light.pico"

    subhierarchy = 'PlotScale'
    # Create a file object to handle parsing of the files.
    # spectrafile = specp.SpectraFile(spectra_file_test, spectra_testpath)
    # Create an interface object to handling interfaceing with SPECCHIO
    # db_interface.specchio_upload_pico_spectra(spectrafile)
    db_interface.specchio_upload_ancil_with_dummy_spectra(ancil_testpath)
    """
    if new_data():
        print("New data found...uploading to specchio database")
        test_upload_sample_data()
        print("Upload done.")
    """
