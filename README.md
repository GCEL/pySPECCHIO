# pySPECCHIO
[![Build Status](https://travis-ci.org/dvalters/pySPECCHIO.svg?branch=master)](https://travis-ci.org/dvalters/pySPECCHIO)
[![Documentation Status](https://readthedocs.org/projects/pyspecchio/badge/?version=latest)](http://pyspecchio.readthedocs.io/en/latest/?badge=latest)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b5322664e6a04d39bb6a6932472baf83)](https://www.codacy.com/app/dvalters/pySPECCHIO?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dvalters/pySPECCHIO&amp;utm_campaign=Badge_Grade)

## Overview

pySPECCHIO is a Python interface and command line utility to upload raw data such as spectra and metadata into the [SPECCHIO spectral information system](http://specchio.ch/). It uses the [JPype](http://jpype.sourceforge.net/) Python-Java bridge package to communicate with the [SPECCHIO API](http://www.specchio.ch/doc/index.html) (written in Java by the SPECCHIO developers). 

pySPECCHIO is currently configured to work with a specific field campaign at the University of Edinburgh, but you are welcome to fork and modify it for your own use.

## Installation notes

1. You must have the SPECCHIO java interface installed. You can either use the Virtual Machine supplied from the SPECCHIO website, or download the java interface (client) from the website and install it following the instructions on the site.

http://specchio.ch/app_download.php

The `SPECCHIO_ReleaseNotes.pdf` document contains instruction on how to set up, create a user account, and test the connection.

2. You must have made an initial connection to the database using the java client in step 1, and created a user account.

3. Having configured the above, you can now proceed to use the pySPECCHIO python program. To do this, download or clone this git repository and follow the [Documentation](https://pyspecchio.readthedocs.io/en/latest/) 

