# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:14:32 2018

@author: dvalters

SPECCHIO driver

Coordinates the parsing and uploading of the spectral data to the SPECCHIO d
database


"""

import specchio_db_interface as specchio

"""Read in from command line, datadir, pico spectra dir or files.,
Date since for new files.
Get DB interface from a config file
"""

def test_upload_sample_data():
    specchio.specchio_uploader_test()


def upload_new_data():
    """Checks the data dir for newly added data and uploads it to specchio."""
    pass


def check_data():
    """Check for new data in the data dir"""
    # Could invlove a database query as well?
    # Don't waste time overwriting exsiting data
    return True

# parse the data from the raw data files, converts to pandas dataframe
data = parse.extract_dataframes()

# Upload the dataframe to the database
specchio.specchio_uploader_test()    # Test function
specchio.upload_dataframe(data)

#if __name__ == "__main__":
#    if check_data():
#        print("new data found...uploading to specchio database")
#        test_upload_sample_data()
#        print("test done.")