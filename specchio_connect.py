import jpype as jp
import unittest

jp.startJVM(jp.getDefaultJVMPath(), "-ea", "-Djava.class.path=/usr/local/SPECCHIO/specchio-client.jar")


SPECCHIO = jp.JPackage('ch').specchio.client

# Craete a client factor instance and get a list of all connection details
cf = SPECCHIO.SPECCHIOClientFactory.getInstance()
db_descriptor_list = cf.getAllServerDescriptors()

# Createa a client for the first entry of the database connection list
specchio_client = cf.createClient(db_descriptor_list.get(0))

# No error return indicates succesful connection

# See what server you are connected to
db_descriptor = db_descriptor_list.get(0)
db_descriptor.getDataSourceName()

# Create a query object
QUERIES = jp.JPackage('ch').specchio.queries
query = QUERIES.Query()


