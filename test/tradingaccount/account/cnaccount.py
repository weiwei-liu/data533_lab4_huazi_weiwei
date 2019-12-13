from .account import Account
import pandas as pd
from datetime import datetime

class cnAccount(Account):
    def __init__(self,balance):
        '''
        Initialize the Chinese stock market account with the balance provided.

        Args:
            balance: the initial amount of money in this account.

        Return:
            No return value. Create a balance,an account_history,a stock, and a stock_history attributes for the account instance.
        '''

        ##inherit from Account class
        Account.__init__(self,balance)
        ##create dict {stockname:stockbalance} to track current stocks in account
        self.stock={}
        #create data frame to record the transaction log of the money and stock activity
        self.stock_history=pd.DataFrame(columns=['Balance','Action','Stock','Amount','Price','Date','Previous_Balance','Commission'])

    def withdraw(self,amount,date=datetime.now()):
        '''
        See account module for more information
        '''
        Account.withdraw(self,amount,date)

    def deposit(self,amount,date=datetime.now()):
        '''
        See account module for more information
        '''
        Account.deposit(self,amount,date)

    def buy(self,stock,amount,price,date=datetime.now()):
        '''
        Buy given amount of a stock from Chinese stock market at given price and date

        Args:
            stock: the listed name or code of the stock in the market, for example 'APPL' stands for 'Apple company in US market'
            amount: the amount of share of one stock for puchasing
            price: the price of the stock purchased
            date: the date the buy is executed; if date parameter not passed, use datetime.now()

        Return:
            return True if stock bought successfully, otherwise return False
        '''
              #In this assumed trading provider, if buy money amount over 20000, the commision fee is amount*0.00025, if under
              #20000, the commission fee is 5.
        if amount*price>20000:
            ##check if there is enough money to buy and pay the commission fee
            if self.balance>=amount*price+amount*price*0.00025:
                previous_balance=self.balance
                self.balance=self.balance-amount*price-amount*price*0.00025
                commission=amount*price*0.00025
                ## if this is first time to buy this stock, add a new dict pair in self.stock
                if stock not in self.stock.keys():
                    self.stock[stock]=amount
                else:
                    self.stock[stock]+=amount
                new_record=pd.Series([self.balance,'buy',stock,amount,price,date,previous_balance,commission],
                                 index=['Balance','Action','Stock','Amount','Price','Date','Previous_Balance','Commission'])
                self.stock_history=self.stock_history.append(new_record,ignore_index=True)
                return True
            else:
                return False
                print('Current balance is insufficient for buying %d of %s at %f' % (amount,stock,price))
        else:
            if self.balance>=amount*price+5:
                previous_balance=self.balance
                self.balance=self.balance-amount*price-5
                commission=5
                if stock not in self.stock.keys():
                    self.stock[stock]=amount
                else:
                    self.stock[stock]+=amount
                new_record=pd.Series([self.balance,'buy',stock,amount,price,date,previous_balance,commission],
                                 index=['Balance','Action','Stock','Amount','Price','Date','Previous_Balance','Commission'])
                self.stock_history=self.stock_history.append(new_record,ignore_index=True)
                return True
            else:
                print('Current balance is insufficient for buying %d of %s at %f' % (amount,stock,price))

    def sell(self,stock,amount,price,date=datetime.now()):
        '''
        Sell given amount of a stock from Chinese stock market at given price and date

        Args:
            stock: the listed name or code of the stock in the market, for example 'APPL' stands for 'Apple company in US market'
            amount: the amount of share of one stock for selling
            price: the price of the stock sold
            date: the date the sell operation is executed; if date parameter not passed, use datetime.now()

        Return:
            return True if stock sold successfully, otherwise return False
        '''
        ##check if there is stock in account for selling
        if stock not in self.stock.keys():
            print('No %s in the account' % stock)
        else:
            if self.stock[stock]>=amount:
                if amount*price>20000:
                    previous_balance=self.balance
                    self.balance=self.balance+amount*price-amount*price*0.00025
                    commission=amount*price*0.00025
                    self.stock[stock]-=amount
                    new_record=pd.Series([self.balance,'sell',stock,amount,price,date,previous_balance,commission],
                                     index=['Balance','Action','Stock','Amount','Price','Date','Previous_Balance','Commission'])
                    self.stock_history=self.stock_history.append(new_record,ignore_index=True)
                    return True
                else:
                    previous_balance=self.balance
                    self.balance=self.balance+amount*price-5
                    commission=5
                    self.stock[stock]-=amount
                    new_record=pd.Series([self.balance,'sell',stock,amount,price,date,previous_balance,commission],
                                     index=['Balance','Action','Stock','Amount','Price','Date','Previous_Balance','Commission'])
                    self.stock_history=self.stock_history.append(new_record,ignore_index=True)
                    return True
            else:
                return False
                print('Current balance is insufficient for selling %d of %s at %f' % (amount,stock,price))
