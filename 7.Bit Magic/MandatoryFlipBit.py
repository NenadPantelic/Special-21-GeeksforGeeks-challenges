#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:57:43 2020

@author: nenad
"""


def flipBit(n): 
    # Your code goes here
    binary = bin(n)[2:]
    ones = []
    i = 0
    #print(binary)
    while i < len(binary):
        #one_flag = False
        #appended = False
        if binary[i] == "1":
            #one_flag = True
            start = i
            i += 1
            while i < len(binary) and binary[i] == "1":
                i += 1
            ones.append((start,i-1))
            #appended = True
        else:
            i += 1
    #print(ones)
    if len(ones) == 0:
        return 1
    if len(ones) == 1:
        return ones[0][1] - ones[0][0] + 2
    max_len = 0
    for i in range(len(ones)-1):
        curr, next = ones[i], ones[i+1]
        max_len = max(max_len,curr[1]-curr[0] + 2)
        if curr[1] + 2 == next[0]:
            max_len = max(max_len,next[1]-curr[0]+1)
    #if ones[-1][1] == len(binary)-1:
    #max_len = max(max_len, ones[0][1] - ones[0][0] + 2)
    max_len = max(max_len, ones[-1][1] - ones[-1][0] + 2)
            
    return max_len
    
# Test 1
n = 1775
print(flipBit(1775))

# Test 2
n = 31
print(flipBit(31))

# Test 3
n = 31
print(flipBit(0))

print(flipBit(19))        
    