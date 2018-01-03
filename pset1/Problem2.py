# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:14:57 2017

@author: Connor
"""

s = 'azcbobobegghakl'
count = 0
index = 0

for index in range(len(s)):
    if index < len(s) - 2:
        if s[index] == 'b':
            if s[index + 1] == 'o':
                if s[index + 2] == 'b':
                    count += 1
    
print("Number of times bob occurs is: " + str(count))