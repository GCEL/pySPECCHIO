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

spclient = jp.JPackage('ch').specchio.client
spquery = jp.JPackage('ch').specchio.queries

print(spclient)
print(spquery)

#class testSpecchio(unittest.TestCase):
#
#  def test_bad_package(self):
spfoobarpkg = jp.JPackage('ch').specchio.foobar

# todo: doesn't fail: probably needs to actually call a Java method from 
# the class before failing??


