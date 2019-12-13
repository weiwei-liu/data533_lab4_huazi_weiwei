import unittest
from sub_package2.plotBalance import plotBalance
import matplotlib.pyplot as plt
import matplotlib.image as gImage


class Test2(unittest.TestCase):
    def setUp(self):
        # init a instance of class PlotStock
        self.pls = plotBalance('BABA_balance.csv')
        # read data form stock file
        self.data = self.pls.readData()
        self.fig = self.pls.plot()
        self.stockInfo = ['Open', 'High', 'Low', 'Adj Close', 'balance']

    def tearDown(self):
        figure = gImage.imread(self.pls.fig_path)
        plt.imshow(figure)
        plt.show()

    @classmethod
    def setUpClass(cls):
        print('Start to test module *pltBalance* in subpackage 2')

    @classmethod
    def tearDownClass(cls):
        print('Stop to test module *pltBalance* in subpackage 2')

    def test_readData(self):
        self.assertIsNotNone(self.data)
        self.assertIn('Open', self.stockInfo)
        self.assertIn('High', self.stockInfo)
        self.assertIn('Low', self.stockInfo)
        self.assertIn('Adj Close', self.stockInfo)
        self.assertIn('balance', self.stockInfo)

    def test_plot(self):
        # judge plot figure successfully or not
        self.assertTrue(self.fig)
