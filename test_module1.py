import unittest
from sub_package2.plotStock import PlotStock


class Test1(unittest.TestCase):
    def setUp(self):
        # init a instance of class PlotStock
        self.pls = PlotStock('BABA.csv')
        # read data form stock file
        self.data = self.pls.readData()
        self.stockInfo = ['Open', 'High', 'Low', 'Adj Close']

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print('Start to test module *pltStock* in subpackage 2')

    @classmethod
    def tearDownClass(cls):
        print('Stop to test module *pltStock* in subpackage 2')

    def test_readData(self):
        self.assertIsNotNone(self.data)
        self.assertIn('Open', self.stockInfo)
        self.assertIn('High', self.stockInfo)
        self.assertIn('Low', self.stockInfo)
        self.assertIn('Adj Close', self.stockInfo)

    def test_plot(self):
        # judge plot figure successfully or not
        self.assertTrue(self.pls.plot())
