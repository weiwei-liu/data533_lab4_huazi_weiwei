from sub_package2.plotStock import *
import sub_package2.plotStock as plotStock


class plotBalance(plotStock.PlotStock):
    """
    class for reading stock balance data and plot it.
    """

    def __init__(self, filePath):
        super(plotBalance, self).__init__(filePath)
        self.fig_path = ''

    def plot(self):
        data = self.readData()  # get data
        try:
            # check if Open, Highest, Lowest, Adj_close exsit in data.columns
            stock_info = {'Open', 'High', 'Low', 'Adj Close', 'balance'}
            is_subset = stock_info.issubset(set(data.columns.tolist()))
            try:
                if not is_subset:
                    raise ColumnError()
            except ColumnError as e:
                print(e)

            # plot stock data and the balance
            plt.plot(data['Date'], data['balance'])
            plt.xlabel('time')
            plt.ylabel('$')
            plt.title('balance against time')

            self.fig_path = 'figs/stock_plot.jpg'
            plt.savefig(self.fig_path)

            plt.show()

            # fig = go.Figure(data=[go.Candlestick(x=data['Date'],
            #                                      balance=data['balance'])])
            # fig.show()

            return self.fig_path
        except:
            print('"{}" is Error data'.format(self.filePath))
