import unittest
import xmlrunner
import SampleTests
 
if __name__=='__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(SampleTests))
    #使用makeSuite方法添加所有的测试方法
    #test_suite.addTest(SampleTests(SampleTests1， SampleTests2))
    # 测试套件中添加测试用例
    runner = xmlrunner.XMLTestRunner(output='report')
    #指定报告放的目录
    runner.run(test_suite)
