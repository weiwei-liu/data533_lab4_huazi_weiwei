import unittest
import pandas as pd
from datetime import datetime

import os
import sys
if os.path.dirname(os.getcwd()) not in sys.path:
    sys.path.append(os.path.dirname(os.getcwd()))

from tradingaccount.account.account import Account


class TestAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Initialize account instance in setUpClass')
        cls.t1=Account(3000)
        print('')

    def setUp(self):
        print('No testcase setup needed')
        print(self.__class__())

    def tearDown(self):
        print('No testcase tearDown needed')
        print('')


    ##test the deposit method
    def test_deposit(self):
        ##check if deposit function return True
        self.assertTrue(self.t1.deposit(200,'2019-02-10'),True)
        ##check account balance after deposit
        self.assertEqual(self.t1.balance,3200)
        ##check if attribute account_history is pandas df
        self.assertIsInstance(self.t1.account_history,pd.DataFrame)
        #check previous balance before deposit in account history dataframe
        self.assertEqual(self.t1.account_history['Previous_Balance'][0],3000)
        #check the length of the df
        self.assertEqual(len(self.t1.account_history),1)
        #check if the deposit value is negative
        self.assertFalse(self.t1.deposit(-200,'2019-02-10'),False)


    ##test the withdraw method
    def test_withdraw(self):
        ##check if withdraw function return True
        self.assertTrue(self.t1.withdraw(200))
        ##assert account balance after withdrawal
        self.assertEqual(self.t1.balance,3000)
        ##check if attribute account_history is pandas dataframe
        self.assertIsInstance(self.t1.account_history,pd.DataFrame)
        #check previous balance before withdraw in account history dataframe
        self.assertEqual(self.t1.account_history['Previous_Balance'][1],3200)
        #check the length of the dataframe
        self.assertEqual(len(self.t1.account_history),2)
        #check the case when withdraw if over current blance
        self.assertEqual(self.t1.withdraw(3500),False)

    @classmethod
    def tearDownClass(cls):
        print('print account_history in this test in tearDownClass:')
        print(cls.t1.account_history)

if __name__=='__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
