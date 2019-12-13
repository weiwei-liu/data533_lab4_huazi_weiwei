import unittest
import pandas as pd
from datetime import datetime

import os
import sys
if os.path.dirname(os.getcwd()) not in sys.path:
    sys.path.append(os.path.dirname(os.getcwd()))

from tradingaccount.account.cnaccount import cnAccount

class TestCnAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Initialize account instance in setUpClass')
        cls.t1=cnAccount(33000)
        cls.t1.buy('162411',100,0.45,'2019-05-17')
        print('')

    def setUp(self):
        print('No testcase setup needed')

    def tearDown(self):
        print('No testcase tearDown needed')
        print('')


    ##test the buy method
    def test_buy(self):
        ##check if buy function return True
        self.assertTrue(self.t1.buy('162411',100,0.45,'2019-02-10'),True)
        ##check account balance after buy
        self.assertEqual(self.t1.balance,32900)
        ##check if attribute stock_history is pandas df
        self.assertIsInstance(self.t1.stock_history,pd.DataFrame)
        #check if attribute stock is dictionary
        self.assertIsInstance(self.t1.stock,dict)
        #check previous balance before buying in stock_history dataframe
        self.assertEqual(self.t1.stock_history['Previous_Balance'][1],32950)
        #check the length of the stock_history df
        self.assertEqual(len(self.t1.stock_history),2)
        ##check the case when buying value is over 20000
        self.t1.buy('600000',300,100,'2019-04-10')
        self.assertEqual(self.t1.balance,2892.5)


    ##test the sell method
    def test_sell(self):
        ##check if sell function return True
        self.assertTrue(self.t1.sell('162411',200,0.45,'2019-06-10'))
        ##assert account balance after selling
        self.assertEqual(self.t1.balance,2977.5)
        ##check if attribute stock_history is pandas dataframe
        self.assertIsInstance(self.t1.stock_history,pd.DataFrame)
        #check if attribute stock is dictionary
        self.assertIsInstance(self.t1.stock,dict)
        #check previous balance before selling in stock_history dataframe
        self.assertEqual(self.t1.stock_history['Previous_Balance'][3],2892.5)
        #check the length of the dataframe
        self.assertEqual(len(self.t1.stock_history),4)
        #check the case when sell amount is over account balance
        self.assertEqual(self.t1.sell('600000',400,110,'2019-06-10'),False)

    @classmethod
    def tearDownClass(cls):
        print('print stock_history in this test in tearDownClass:')
        print(cls.t1.stock_history)

if __name__=='__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
