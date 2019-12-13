from datetime import datetime
import pandas as pd

class Account():
    def __init__(self,balance):
        '''
        Initialize the account with the balance provided.

        Args:
            balance: the initial amount of money in the account.

        Return:
            No return value. Create a balance and an account_history attributes for the account instance.
        '''
        self.balance=balance
        #create data frame to record the transaction log of the money and stock activity
        self.account_history=pd.DataFrame(columns=['Balance','Action','Amount','Date','Previous_Balance'])

    def withdraw(self,amount,date=datetime.now()):  ##if date parameter not passed, use datetime.now()
        '''
        Withdraw given amount of money at given date

        Args:
            amount: the amount of money for withdraw, the amount can't be over the current Balance
            date: the date the withdraw is executed; if date parameter not passed, use datetime.now()

        Return:
            return True if money withdrawed from the account, otherwise return False
        '''
        if self.balance>=amount:
            previous_balance=self.balance
            self.balance=self.balance-amount
            new_record=pd.Series([self.balance,'withdraw',amount,date,previous_balance],
                                 index=['Balance','Action','Amount','Date','Previous_Balance'])
            self.account_history=self.account_history.append(new_record,ignore_index=True)
            return True
        else:
            print('Current balance is insufficient for withdraw %d' % amount)
            return False

    def deposit(self,amount,date=datetime.now()):
        '''
        Deposit given amount of money at given date

        Args:
            amount: the amount of money for deposit, the amount can't be negative.
            date: the date the deposit is executed; if date parameter not passed, use datetime.now()

        Return:
            return True if money deposit from the account, otherwise return False
        '''
        if amount<0:
            print('negative amount is not allowed to deposit')
            return False
        else:
            previous_balance=self.balance
            self.balance=self.balance+amount
            new_record=pd.Series([self.balance,'deposit',amount,date,previous_balance],
                                     index=['Balance','Action','Amount','Date','Previous_Balance'])
            self.account_history=self.account_history.append(new_record,ignore_index=True)
            return True
