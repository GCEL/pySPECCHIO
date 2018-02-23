import jpype as jp

jp.startJVM(jp.getDefaultJVMPath(), "-ea")

testpackage = jp.JPackage('Test').Test
Test = testpackage

Test.speak("Hello from a custom Java class")
t = Test()
print t.getString()

jp.shutdownJVM()

