#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 09:54:34 2018

@author: centos
"""

import jpype as jp
import time
import unittest

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

# Connect to server (make this into method as is often called)
client_factory = spclient.SPECCHIOClientFactory.getInstance()
descriptor_list = client_factory.getAllServerDescriptors()
specchio_client = client_factory.createClient(descriptor_list.get(0))

# Create a new campaign programatically
c = sptypes.SpecchioCampaign()
c.setName('Test (Python)')

c_id = specchio_client.insertCampaign(c)
c.setId(c_id)  # Store the campaign ID in the campaign object.

# The id of the new campaign is stored in the c_id variable
