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

# Connect to server
client_factory = spclient.SPECCHIOClientFactory.getInstance()
descriptor_list = client_factory.getAllServerDescriptors()
specchio_client = client_factory.createClient(descriptor_list.get(0))

# Set up a campaign data loader
cdl = spreader_campaign.SpecchioCampaignDataLoader(specchio_client)

campaign = specchio_client.getCampaign(18)

cdl.set_campaign(campaign)
cdl.start()

delay = 0.01

while cdl.isAlive:
    time.sleep(delay)

print('Number of parsed files: ', cdl.getParsed_file_Counter)
print('Number of inserted files: ', cdl.getSuccessful_file_counter)    


#class testSpecchio(unittest.TestCase):
#
#  def test_bad_package(self):



