import unittest
from test_module1 import Test1
from test_module2 import Test2

import unittest
import os
import sys
if os.path.dirname(os.getcwd()) not in sys.path:
    sys.path.append(os.path.dirname(os.getcwd()))

from account_module_test import TestAccount
from cnaccount_module_test import TestCnAccount
from usaccount_module_test import TestUsAccount
from test_module1 import Test1
from test_module2 import Test2

def testSuite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    
    suite.addTest(Test1('test_readData'))
    suite.addTest(Test1('test_plot'))
    suite.addTest(Test2('test_readData'))
    suite.addTest(Test2('test_plot'))
    
    suite.addTest(unittest.makeSuite(TestAccount))
    suite.addTest(unittest.makeSuite(TestCnAccount))
    suite.addTest(unittest.makeSuite(TestUsAccount))
    suite.addTest(unittest.makeSuite(Test1))
    suite.addTest(unittest.makeSuite(Test2))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

if __name__=='__main__':
    testSuite()