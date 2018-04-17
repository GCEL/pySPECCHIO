.. pySPECCHIO documentation master file, created by
   sphinx-quickstart on Tue Apr 17 15:11:48 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pySPECCHIO Documentation 
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

pySPECCHIO is a Python interface to the SPECCHIO spectral information system. (www.specchio.ch).

pySPECCHIO contains a command-line interface for scanning directories of metadata and spectra files and uploading them to the SPECCHIO database.

Basic Usage
-----------

Download the software from the github repository at: https://github.com/dvalters/pySPECCHIO

There is no need to 'install' the software, though a setup.py script will be made available. 

Alternatively, navigate to the `pyspecchio` folder and run the uploader with:

```
python3 specchio_main.py [PATH_TO_DATADIR]
```
The path should point to the top level directory that contains either the spectra file(s) or the metadata files to be uploaded to the database.




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
