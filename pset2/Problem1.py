# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 12:08:06 2017

Calculates the amount left on a credit card after a year
of making only min payments

@author: Connor
"""


for i in range(12):
    min_payment = monthlyPaymentRate * balance
    unpaid_balance = balance - min_payment
    interest = (annualInterestRate/12.0) * unpaid_balance
    balance = unpaid_balance + interest
    
print("Remaining balance: ", round(balance,2))