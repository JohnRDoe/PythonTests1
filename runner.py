import unittest
import xmlrunner
from SampleTests import *
# from SampleTests2 import *
 
if __name__=='__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(SampleTests1, SampleTests2))
    #使用makeSuite方法添加所有的测试方法
    #test_suite.addTest(SampleTests(SampleTests1， SampleTests2))
    # 测试套件中添加测试用例
    runner = xmlrunner.XMLTestRunner(output='report')
    #指定报告放的目录
    runner.run(test_suite)
