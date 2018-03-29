# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:14:32 2018

@author: dvalters

SPECCHIO driver

Coordinates the parsing and uploading of the spectral data to the SPECCHIO d
database


"""

import parser_pandas as parse
import specchio_db_interface as specchio


def upload_new_data():
    """Checks the data dir for newly added data and uploads it to specchio."""
    pass

def check_data():
    """Check for new data in the data dir"""
    # Could invlove a database query as well?
    # Don't waste time overwriting exsiting data
    pass

