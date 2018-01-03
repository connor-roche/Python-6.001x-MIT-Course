# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:38:06 2017

@author: Connor
"""

s = 'azcbobobegghakl'
stored_string = ""
result = ""
counter = 0
place = 0

for index in range(len(s)):
    if index < (len(s) - 1):
        place = index + 1
        counter = 0
        stored_string = s[index]
        while(ord(s[place]) >= ord(s[place - 1])):
            stored_string += s[place]
            if place < len(s) - 1:
                place += 1
            else: 
                break    
        if len(stored_string) > len(result):
            result = stored_string
        
print("Longest substring in alphabetical order is: " + result)