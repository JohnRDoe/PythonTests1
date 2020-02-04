import unittest
import xmlrunner
from SampleTests import *
 
if __name__ == '__main__':
    test = unittest.main()
    test.addTest(unittest.makeSuite(Test))
    runner = xmlrunner.XMLTestRunner(output='report')#指定报告放的目录
    runner.run(test)
