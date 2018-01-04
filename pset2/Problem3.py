# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:05:17 2017

@author: Connor
"""
#initalize variables
orig_balance = balance
monthly_interest = annualInterestRate / 12.0
unpaid_balance = 0
lower_bound = balance / 12.0
upper_bound = (balance * (1+ monthly_interest)**12) / 12.0
epsilon = 0.02
    
#finds the min payment to pay off the entire balance plus interest in one year
while abs(balance) > epsilon:
    min_payment = (upper_bound + lower_bound) / 2
    balance = orig_balance
    
    for i in range(12):
        unpaid_balance = balance - min_payment
        interest = (annualInterestRate/12.0) * unpaid_balance
        balance = unpaid_balance + interest

    #changes the bounds accordingly
    if balance > epsilon:
        lower_bound = min_payment
    elif balance < epsilon:
        upper_bound = min_payment
    else:
        break
        
print("Lowest Payment: ", round(min_payment, 2))
        