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

init_jvm()

spclient = jp.JPackage('ch').specchio.client
spquery = jp.JPackage('ch').specchio.queries
sptypes = jp.JPackage('ch').specchio.types
spgui = jp.JPackage('ch').specchio.gui
spreader_campaign = jp.JPackage('ch').specchio.file.reader.campaign

# TODO: Call or attribute? Check API here...  
metaparam = sptypes.MetaParameter

class SpecchioClient(object):
    """Specchio db client in Python object form"""
    pass

class Campaign(object):
    """Object for storing an instance of a campaign"""
    def __init__(self, campaign_name):
        pass

class specchioDBinterface(object):
    """Object to manage interations with the SPECCHIO db and handle uplodas 
    from pandas dataframes"""

    def __init__(self, campaign_name):
        
        # Check JVm is up and running, set up a database client and connect 
        # to the server
        init_jvm()
        self.campaign_name = campaign_name
        client_factory = spclient.SPECCHIOClientFactory.getInstance()
        descriptor_list = client_factory.getAllServerDescriptors()
        self.specchio_client = client_factory.createClient(descriptor_list.get(0))
        
        # Set the campaign name and ID
        self.campaign = sptypes.SpecchioCampaign()
        self.campaign.setName(self.campaign_name)
        self.c_id = self.specchio_client.insertCampaign(self.campaign)
        self.campaign.setId(self.c_id)  # Store the campaign ID in the campaign object.

    def read_metadata(self, filename):
        """ Reads the example metadata csv file and returns a pandas dataframe"""
        # Read in the csv, transposing it because the names are actually in the 1st column
        df = pd.read_csv(filename, header=None).transpose()
        # Now use the transposed 1st row to create the column names
        df.columns = df.iloc[0]
        # Now we can drop row 1 as it is loaded as column names
        df = df.reindex(df.index.drop(0))
        return df
    
    def set_spectra_file_info(self, spspectra_file):
        """Set basic info about the spectra file being processed"""
        # What happens if is dataframe?
        spspectra_file.setPath(filepath)
        spspectra_file.setFilename(filename)
        
        spspectra_file.setCompany('UoE')      
        # Creating a metadata hierarchy
        hierarchy_id = self.specchio_client.getSubHierarchyId(self.campaign, subhierarchy, 0)
        # 0 argument specifices the hierarchy has no parent.
        # Set the campaign and hierarchy to store in
        spspectra_file.setHierarchyId(hierarchy_id)
        spspectra_file.setCampaignId(self.c_id)
    
    def upload_dataframe(self, dataframe, campaign, hierarchy_id):
        """Uploads a pandas dataframe to SPECCHIO"""
        raise NotImplementedError
        """Convert the below function accept a dartaframe and extract the 
        relevant spectra to be uploaded. This must invlve converting
        the pandas dartaframe columns to various java array types before they can 
        be uploaded."""
        self.set_spectra_file_info()
    
    def read_test_data(self):
        with open(filepath + filename, 'r') as csvfile:
            wavelens_and_spectra = np.loadtxt(csvfile, delimiter=',')
            wavelengths = wavelens_and_spectra[:,0]
            spectra = wavelens_and_spectra[:,1:]
            
            # Now get the metadata
            metadata = self.read_metadata(filepath + "metadata.csv")
            return wavelengths, spectra, metadata
    
    def specchio_uploader_test(self, filename, filepath, subhierarchy):
        """Uploadr for the test data"""
        # Create a spectra file object and set its params
        spspectra_file = sptypes.SpectralFile()
        self.set_spectra_file_info(spspectra_file)
        
        # read test data
        wavelengths, spectra, metadata = self.read_test_data()
        
        # Now we can set the number of spectra
        spspectra_file.setNumberOfSpectra(np.size(spectra,1))   

        """ The following code takes the spectral file object and fills the spectral data
        into a Java array and the Metadata into a metadata object. The spectral file
        object is then stored in the database under the campaign and hierarchy we 
        created.
        
        This code is specific to the spectra file/data being uploaded 
        it should be made more general purpose
        """

        # A numpy temporary holding array, dims of no of spectra x no of wvls
        spectra_array = np.zeros( ( np.size(spectra,1), len(wavelengths) ) )

        for i in range(0,np.size(spectra, 1)):
            vector = spectra[:,i]
            for w in range(0,len(wavelengths)):
                # Perhaps create a numpy array first and then populate?
                spectra_array[i,w] = vector[w]
            
            spspectra_file.addWvls([jp.java.lang.Float(x) for x in wavelengths])

            # Add filename: we add an automatic number here to make them distinct
            fname_spectra = filename + str(i)
            spspectra_file.addSpectrumFilename(fname_spectra)
            
            # Add plot number 
            smd = sptypes.Metadata()
            
            if i > 0:   
                mp = metaparam.newInstance(self.specchio_client.getAttributesNameHash().get('Target ID'))
                mp.setValue(str(metadata['Plot'][i]))
                smd.addEntry(mp)
                
                # Add Nitrate
                mp = metaparam.newInstance(self.specchio_client.getAttributesNameHash().get('Nitrate Nitrogen'))
                mp.setValue(metadata['Nitrate Nitrogen Mg/Kg'][i])
                smd.addEntry(mp)
                
                # Add Phosphorous
                mp = metaparam.newInstance(self.specchio_client.getAttributesNameHash().get('Phosphorus'))
                mp.setValue(metadata['Phosphorus %'][i])
                smd.addEntry(mp)
                
                spspectra_file.addEavMetadata(smd)
        
        javafloat_spectra_array = [[jp.java.lang.Float(j) for j in i] for i in spectra_array]
        
        spspectra_file.setMeasurements(javafloat_spectra_array)
        
        self.specchio_client.insertSpectralFile(spspectra_file)    

if __name__ == "__main__":
    
    db_interface = specchioDBinterface("Python test campaign")
    
    filepath = '/home/centos/Downloads/'
    filename = 'spectra.csv'
    subhierarchy = 'Pasture'
    db_interface.specchio_uploader_test(filename, filepath, subhierarchy)




