
# Trading Account Package

Created by:
•	Huazi Li
•	Weiwei Liu

Trading Account is a python package that allows users to track their transaction records and generate visualization for both balance and stock history. Candlestick may be applied as the primary drawing method.
________________________________________
## Prerequisites

Some Python packages may be imported or installed in advance, in order to run our package successfully.

*	matplotlib
*	pandas
*	plotly
*	plotStock
*	unittest
* datetime

For the plotly package, type the following code to install before import:

conda install -c plotly plotly=4.3.0
________________________________________

## Package components

The structure of the package is as follow:

* package (`trading account`)

    * sub-packge (`account`)
        * module (`cnAccount`)
            * class (`cnAccount`)
                * `__init__` (inherit from `Account`)
                * `buy`
                * `sell`

        * module (`usAccount`)
            * class (`usAccount`)
                * `__init__` (inherit from `Account`)
                * `buy`
                * `sell`

        * module (`Account`)
            * class (`Account`)
                * `__init__`
                * `deposit`
                * `withdrawl`

  * sub-package (`visualization`)
       * module (`plotBalance`)
       * module (`plotStock`)

In the `account` sub package, the `Account` will realize balance, deposit and withdraw functions.  the `cnAccount` will record account activities and transactions happening on the Chinese stock market. And the functions inside the `cnAccount` module include buy and sell stock, deposit and withdraw from the account. Similarly for the `usAccount`.

Visualization is a sub-package which consists of two modules: plotBalance and plotStock.

Note: The overall coverage is 89%. The main reason is that some percentage are lost in the try-exception section.


Please use demo file to preview and test the functionalities of sub-packages.

[![Build Status](https://travis-ci.org/weiwei-liu/Data533-lab4.svg?branch=master)](https://travis-ci.org/weiwei-liu/Data533-lab4)
