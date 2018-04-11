import jpype as jp
import unittest

def init_jvm(jvmpath=None):
    """
    Checks first to see if JVM is already running.
    """
    if jp.isJVMStarted():
        return
    jp.startJVM(jp.getDefaultJVMPath(), "-ea", "-Djava.class.path=/usr/local/SPECCHIO/specchio-client.jar")

init_jvm()

SPECCHIO = jp.JPackage('ch').specchio.client

# Create a client factor instance and get a list of all connection details
cf = SPECCHIO.SPECCHIOClientFactory.getInstance()
db_descriptor_list = cf.getAllServerDescriptors()

# Create a client for the first entry of the database connection list
specchio_client = cf.createClient(db_descriptor_list.get(0))

# No error return indicates succesful connection

# See what server you are connected to
db_descriptor = db_descriptor_list.get(0)
print(db_descriptor.getDataSourceName())

# Create a query object
QUERIES = jp.JPackage('ch').specchio.queries
query = QUERIES.Query()

# Create a query conditio for the altitude attribute and configure it
attr = specchio_client.getAttributesNameHash().get('Altitude')

cond = QUERIES.EAVQueryConditionObject(attr)
cond.setValue('50.0')
cond.setOperator('>=')
query.add_condition(cond)

# Now get the spectrum IDs that match the query
ids = specchio_client.getSpectrumIdsMatchingQuery(query)

print(ids.size())
print(ids)

# Add another condition to restrict maximum altitude
cond = QUERIES.EAVQueryConditionObject(attr)
cond.setValue('55.0')
cond.setOperator('<')
query.add_condition(cond)

ids = specchio_client.getSpectrumIdsMatchingQuery(query)
print(ids)
print(ids.size())

# LOADING SPECTRAL DATA FROM THE DATABASE

# Create spectral spaces and order the spectra bt their acquisationtime
# Note: this does not load the spectral dta yet but only prepares the containers
spaces = specchio_client.getSpaces(ids, 'Acquisition Time')

# Find out how many spaces we have received
len(spaces)

# Get the first space
space = spaces[0]

ids = space.getSpectrumIds() # get them sorted by acquisition time

# Load the spectral data from the database into the space
space = specchio_client.loadSpace(space)

# Get the spectral vectors, wavelengths, and measurement unit
vectors = space.getVectorsAsArray()
wvl = space.getAverageWavelengths()
unit = space.getMeasurementUnit().getUnitName()

def plot_spectra():
    import numpy as np
    import matplotlib.pyplot as plt
    
    axes = plt.gca()
    axes.set_xlim([350,2500])
    axes.set_ylim([0,1])
    y = np.rot90(vectors, 3)
    plt.plot(wvl, y)
    plt.show()

plot_spectra()

jp.shutdownJVM()




















