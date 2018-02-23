import jpype as jp

jp.startJVM(jp.getDefaultJVMPath(), "-ea")
jp.java.lang.System.out.println("Hello JPype!")
jp.shutdownJVM()
