.. pySPECCHIO documentation master file, created by
   sphinx-quickstart on Tue Apr 17 15:11:48 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pySPECCHIO Documentation 
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

pySPECCHIO is a Python interface to the SPECCHIO spectral information system. (http://www.specchio.ch).

pySPECCHIO contains a command-line interface for scanning directories of metadata and spectra files and uploading them to the SPECCHIO database.

Installation Requirements
-------------------------

pySPECCHIO is designed to run with Python version 3 and above. (If you are using the virtual machine image to run SPECCHIO, it should be available already simply by running the command `python3`. But otherwise it can be installed from any of the standard python distributions, such as Anaconda or Miniconda, or through your operating system package manager.

You will need the following Python packages installed:

 - pandas
 - numpy
 - xlrd
 - jpype1


Basic Usage
-----------

Download the software from the github repository at: https://github.com/dvalters/pySPECCHIO

There is no need to 'install' the software, though a setup.py script will be made available.

To upload plot-level data, navigate to the `pyspecchio` folder and run the uploader with:

.. code-block:: shell

   python3 specchio_main.py --data-path [PATH_TO_DATADIR]

The path should point to the top level directory that contains either the spectra file(s) or the metadata files to be uploaded to the database.

To upload a spectra file (.pico format), the following command is used.

.. code-block:: shell

   python3 specchio_main.py --spectra-path [PATH_TO_SEPCTRA_FILE] --spectra-name [NAME_OF_PICO_SPECTRA_FILE]

Test usage
----------

A set of test options are included to upload test data to the database.

.. code-block:: shell

   python3 specchio_main.py --test-metadata-upload
   python3 specchio_main.py --test-spectra-upload

These may be useful to run to verify your SPECCHIO installation is correctly set up and pySPECCHIO can interface with it.


Full usage
----------

.. code-block:: shell

   usage: specchio_main.py [-h] [--data-path PATH] [--spectra-path PATH]
                        [--spectra-name SPECTRAFILE_NAME [SPECTRAFILE_NAME ...]]
                        [--campaign-name CAMPAIGN-NAME] [--use-dummy-spectra]
                        [--test-metadata-upload] [--test-spectra-upload]

   Process data files to be uploaded to the SPECCHIO database.

   optional arguments:
     -h, --help            show this help message and exit

     --data-path PATH      The path to the ancillary data files (Plot-level data
                           that are not spectra files.)

     --spectra-path PATH   The path to the PICO Spectra (.pico) file(s)

     --spectra-name SPECTRAFILE_NAME [SPECTRAFILE_NAME ...]
                           The name to the PICO Spectra (.pico) file(s)

     --campaign-name CAMPAIGN-NAME
                           The name of the field campaign. This will be created
                           in the SPECCHIO database if it does not already exist.

     --use-dummy-spectra   Generate dummy spectra for ancillary data files.This
                           option will generate dummy spectra files if none
                           are asscoiated with the data files provided. Dummy
                           spectraare required due to the design of the SPECCHIO
                           software, which is centred around the spectra files.
                           Dummy spectra will be written to disk.

     --test-metadata-upload
                           Runs the program in test mode, using the data fromthe
                           test directory, uploading it to a test campaign. No
                           further arguments are required.

     --test-spectra-upload
                           Runs the program in test mode, using the data from the
                           test directory, uploading it to a test campaign. No
                           further arguments are required.




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
