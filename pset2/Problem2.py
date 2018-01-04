# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 13:15:53 2017

@author: Connor
"""

new_balance = balance
min_payment = 0
unpaid_balance = 0

while(balance > 0):
    min_payment += 10
    balance = new_balance
    
    for i in range(12):
        unpaid_balance = balance - min_payment
        interest = (annualInterestRate/12.0) * unpaid_balance
        balance = unpaid_balance + interest
        
print("Lowest Payment: ", min_payment)
        
    