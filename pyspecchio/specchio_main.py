# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:14:32 2018

@author: dvalters

SPECCHIO driver

Coordinates the parsing and uploading of the spectral data to the SPECCHIO
database


"""
import sys
import os
import argparse

import specchio_db_interface as specchio
import spectra_parser as spectraparser
import ancildata_parser as ancilparser

"""Read in from command line, datadir, pico spectra dir or files.,
Date since for new files.
Get DB interface from a config file
"""
parser = argparse.ArgumentParser(description='Process data files to be'
                                 'uploaded to the SPECCHIO database.')
parser.add_argument('--data-path', metavar='PATH', type=str,
                    dest='datapath',
                    help='The path to the ancillary data files'
                    '(Plot-level data that are not spectra files.)')
parser.add_argument('--spectra-path', metavar='PATH', type=str,
                    dest='spectrapath',
                    help='The path to the PICO Spectra (.pico) file(s)')
parser.add_argument('--spectra-name', metavar='SPECTRAFILE_NAME', type=str,
                    dest='spectraname', nargs='+',
                    help='The name to the PICO Spectra (.pico) file(s)')
parser.add_argument('--campaign-name', metavar='CAMPAIGN-NAME', type=str,
                    dest='campaign_name',
                    help='The name of the field campaign. This will be'
                    ' created in the SPECCHIO database if it does not'
                    ' already exist.')
parser.add_argument('--use-dummy-spectra', dest='use_dummy_spectra',
                    action='store_const',
                    const=True,
                    help='Generate dummy spectra for ancillary data files.'
                    'This option will generate dummy spectra files if none are'
                    'asscoiated with the data files provided. Dummy spectra'
                    'are required due to the design of the SPECCHIO software,'
                    'which is centred around the spectra files.\n'
                    'Dummy spectra will be written to disk.')
parser.add_argument('--test-metadata-upload', dest='test_metadata_mode',
                    action='store_const',
                    const=True,
                    help='Runs the program in test mode, using the data from'
                    'the test directory, uploading it to a test campaign.\n'
                    'No further arguments are required.')
parser.add_argument('--test-spectra-upload', dest='test_spectra_mode',
                    action='store_const',
                    const=True,
                    help='Runs the program in test mode, using the data from'
                    'the test directory, uploading it to a test campaign.\n'
                    'No further arguments are required.')

args = parser.parse_args()
# Must have at least one of these options:
if not (args.datapath or args.spectrapath or args.test_spectra_mode or args.test_metadata_mode):
    parser.error("No action requested, you must either supply the location"
                 " of the metadata directory with"
                 " the --datapath option or specify --test-mode.")
    sys.exit(0)

# Assumes a single spectra file for now
if args.spectrapath and args.spectrafile:
    spectra_filename = args.spectraname
    spectra_filepath = args.spectrapath
    campaign_name = args.campaign_name
 
    spectrafile = spectraparser.SpectraFile(spectra_filename, spectra_filepath)
    db_interface = specchio.specchioDBinterface(campaign_name)
    db_interface.db_interface.specchio_upload_pico_spectra(spectrafile)

if args.spectrapath and not args.spectrafile:
    parser.error("You supplied a path to the spectra files, but not the name"
                 " of a spectra file.")
    sys.exit(0)

if args.datapath:
    # Upload the metadata in the data path
    # TODO: Normalise filepath perhaps?
    ancilpath = args.datapath
    campaign_name = args.campaign_name
    # Initialise the database interface object for data upload
    db_interface = specchio.specchioDBinterface(campaign_name)
    db_interface.specchio_upload_ancil_with_dummy_spectra(ancilpath)

if args.test_metadata_mode:
    if args.campaign_name is None:
        campaign_name = "Test Campaign"
    else:
        campaign_name = args.campaign_name
    
    ancilpath = os.path.join(os.path.abspath("../test/DATA/"), '')
    
    # VALIDATE PATH!
    
    db_interface = specchio.specchioDBinterface(campaign_name)
    db_interface.specchio_upload_ancil_with_dummy_spectra(ancilpath)  

if args.test_spectra_mode:
    spectra_filepath = os.path.join(os.path.abspath("../test/PICO_testdata/"), '')
    spectra_filename = "QEP1USB1_b000000_s000002_light.pico"
    if args.campaign_name is None:
        campaign_name = "Test Campaign (spectra_file)"
    else:
        campaign_name = args.campaign_name
 
    spectrafile = spectraparser.SpectraFile(spectra_filename, spectra_filepath)
    db_interface = specchio.specchioDBinterface(campaign_name)
    db_interface.specchio_upload_pico_spectra(spectrafile)   
    
    
def new_data():
    """Check for new data in the data dir"""
    # Could invlove a database query as well?
    # Don't waste time overwriting exsiting data
    raise NotImplemented("Not Implemented this feature yet")
    return True
