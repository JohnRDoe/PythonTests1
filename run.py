import unittest
from test_sort import TestSort
import xmlrunner

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSort))
    #runner=unittest.TextTestRunner(verbosity=2)
    runner = xmlrunner.XMLTestRunner(output='test-reports') #test-reports为生成报告的目录名
    runner.run(suite)
