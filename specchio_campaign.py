#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 09:54:34 2018

@author: centos
"""

import jpype as jp
import time
import unittest
import numpy as np

def init_jvm(jvmpath=None):
    """
    Checks first to see if JVM is already running.
    """
    if jp.isJVMStarted():
        return
    jp.startJVM(jp.getDefaultJVMPath(), "-ea", "-Djava.class.path=/usr/local/SPECCHIO/specchio-client.jar")

init_jvm()

spclient = jp.JPackage('ch').specchio.client
spquery = jp.JPackage('ch').specchio.queries
sptypes = jp.JPackage('ch').specchio.types
spgui = jp.JPackage('ch').specchio.gui
spreader_campaign = jp.JPackage('ch').specchio.file.reader.campaign
spspectra_file = sptypes.SpectralFile()

# Connect to server (make this into method as is often called)
client_factory = spclient.SPECCHIOClientFactory.getInstance()
descriptor_list = client_factory.getAllServerDescriptors()
specchio_client = client_factory.createClient(descriptor_list.get(0))

# Create a new campaign programatically
# DV: Note this by default inserts into the localhost db.

c = sptypes.SpecchioCampaign()
c.setName('Test (Python)')

c_id = specchio_client.insertCampaign(c)
c.setId(c_id)  # Store the campaign ID in the campaign object.

# The id of the new campaign is stored in the c_id variable

# Creating a metadata hierarchy
hierarchy_id = specchio_client.getSubHierarchyId(c, 'Pasture', 0)
# 0 argument specifices the hierarchy has not parent.

# LOADING THE SPECTRAL CSV AND METADATA CSV FILES INTO MATLAB
filepath = '/home/centos/Downloads/'
filename = 'spectra.csv'

with open(filepath + filename, 'r') as csvfile:
# Pandas or Numpy?
    wavelens_and_spectra = np.loadtxt(csvfile, delimiter=',')
    wavelengths = wavelens_and_spectra[:,1]
    spectra = wavelens_and_spectra[:,2:]
    
# Reading and processing Input files.
""" The following code generates a spectral file object fills the spectral data
into a Java array and the Metadata into a metadata object. The spectral file
object is then stored in the database under the campaign and hierarchy we 
created.
"""

# Create a spectral file 
#spectra_obj = spspectra_file.
spspectra_file.setNumberOfSpectra(np.size(spectra,1))
spspectra_file.setPath(filepath)
spspectra_file.setFilename(filename)
spspectra_file.setCompany('UoE')

# Set the campaign and hierarchy to store in
spspectra_file.setHierarchyId(hierarchy_id)
spspectra_file.setCampaignId(c_id)

# Create array for spectral data
spectra_array = jp.JArray(jp.JFloat, np.size(spectra,1))(len(wavelengths))

# Create an array for wavelengths
java_wavelengths = jp.JArray(jp.JFloat, np.size(spectra,1))(len(wavelengths))

for w in range(1, len(wavelengths)):
    java_wavelengths[w] = jp.java.lang.Float(wavelengths[w])
















