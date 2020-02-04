import unittest

class Tests1(unittest.TestCase):
    
    def test_method1(self):
        print('Failed test')
        self.assertEqual(True, False)

    def test_method2(self):
        print('Passed test')
        self.assertEqual(True, True)

    def test_method3(self):
        self.assertEqual(True, False)

    def test_method4(self):
        print('Random gibberish')
        self.assertEqual(True, True)

#     def test_method5(self):
#         throw ('some exception')

    def test_method1(self):
        print('Failed test')
        self.assertEqual(True, False)

    def test_method2(self):
        print('Passed test')
        self.assertEqual(True, True)

    def test_method3(self):
        self.assertEqual(True, False)

    def test_method4(self):
        print('Random gibberish')
        self.assertEqual(True, True)
        
#     @unittest.skip("demonstrating skipping")
#     def test_method5(self):
#         pass

#     def test_method6(self):
#         throw ('some exception')
if __name__ == '__main__':
    unittest.main()
