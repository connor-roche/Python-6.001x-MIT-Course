# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:06:28 2017

@author: Connor
"""
s = 'azcbobobegghakl'
count = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or \
    char == 'o' or char == 'u':
        count += 1
    
print("Number of vowels: " + str(count))