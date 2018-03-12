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
import pandas as pd

def init_jvm(jvmpath=None):
    """
    Checks first to see if JVM is already running.
    """
    if jp.isJVMStarted():
        return
    jp.startJVM(jp.getDefaultJVMPath(), "-ea", "-Djava.class.path=/usr/local/SPECCHIO/specchio-client.jar")

def read_metadata(filename):
    """ Reads the example metadata csv file and returns a pandas dataframe"""
    
    # Read in the csv, transposing it because the names are actually in the 1st column
    df = pd.read_csv(filename, header=None).transpose()
    # Now use the transposed 1st row to create the column names
    df.columns = df.iloc[0]
    # Now we can drop row 1 as it is loaded as column names
    df = df.reindex(df.index.drop(0))
    return df
    
init_jvm()

spclient = jp.JPackage('ch').specchio.client
spquery = jp.JPackage('ch').specchio.queries
sptypes = jp.JPackage('ch').specchio.types
spgui = jp.JPackage('ch').specchio.gui
spreader_campaign = jp.JPackage('ch').specchio.file.reader.campaign

# TODO: Call or attribute? Check API here...
spspectra_file = sptypes.SpectralFile()
metaparam = sptypes.MetaParameter

# Connect to server (make this into method as is often called)
client_factory = spclient.SPECCHIOClientFactory.getInstance()
descriptor_list = client_factory.getAllServerDescriptors()
specchio_client = client_factory.createClient(descriptor_list.get(0))

# Create a new campaign programatically
# DV: Note this by default inserts into the localhost db.

c = sptypes.SpecchioCampaign()
c.setName('Python Uploader Monday')

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
    
    # Now get the metadata
    metadata = read_metadata(filepath + "metadata.csv")
    
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

# A numpy temporary holding array, dims of no of spectra x no of wvls
spectra_array = np.zeros( ( np.size(spectra,1), len(wavelengths) ) )

# Create an array for wavelengths
# Translated from MATLAB's javaArray - not sure if this is entirely possbile...
java_wavelengths = jp.JArray(jp.JFloat)(list(wavelengths))

for i in range(0,np.size(spectra, 1)):
    vector = spectra[:,i]
    for w in range(0,len(wavelengths)):
        # Perhaps create a numpy array first and then populate?
        spectra_array[i,w] = vector[w]
    
    # Add the wavelengths
    # This seems horrendously hacky...
    # TODO: Also it would make the first declartion redundant now? (Revisit later)
    spspectra_file.addWvls([jp.java.lang.Float(x) for x in java_wavelengths])
    
    # Add filename: we add an automatic number here to make them distinct
    fname_spectra = filename + str(i)
    spspectra_file.addSpectrumFilename(fname_spectra)
    
    # Add plot number 
    smd = sptypes.Metadata()
    
    if i > 0:   
        mp = metaparam.newInstance(specchio_client.getAttributesNameHash().get('Target ID'))
        mp.setValue(str(metadata['Plot'][i]))
        smd.addEntry(mp)
        
        # Add Nitrate
        mp = metaparam.newInstance(specchio_client.getAttributesNameHash().get('Nitrate Nitrogen'))
        mp.setValue(metadata['Nitrate Nitrogen Mg/Kg'][i])
        smd.addEntry(mp)
        
        # Add Phosphorous
        mp = metaparam.newInstance(specchio_client.getAttributesNameHash().get('Phosphorus'))
        mp.setValue(metadata['Phosphorus %'][i])
        smd.addEntry(mp)
        
        spspectra_file.addEavMetadata(smd)

# Convert to a java array the spectra_array
#java_spectra_array = jp.JArray(float, 2)(spectra_array.tolist())
# does not work when passed to java function expecting float[][]

spectra_list = spectra_array.tolist()
javafloat_spectra_array = [[jp.java.lang.Float(j) for j in i] for i in spectra_list]

spspectra_file.setMeasurements(javafloat_spectra_array)

specchio_client.insertSpectralFile(spspectra_file)    






