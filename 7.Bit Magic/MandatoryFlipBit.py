#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:57:43 2020

@author: nenad
"""
"""
Problem URL: https://practice.geeksforgeeks.org/contest-problem/mandatory-flip-bit/1/


"""
# Time: O(n)
def flipBit(n): 
    # convert number to binary string
    binary = bin(n)[2:]
    ones = []
    i = 0
    while i < len(binary):
        # 1's stream starts
        if binary[i] == "1":
            start = i
            i += 1
            # until stream of 1's is active
            while i < len(binary) and binary[i] == "1":
                i += 1
            # stream finishes - we reached 0
            # append bound of 1's stream [start, end]
            ones.append((start,i-1))
        else:
            i += 1
    # every bit is 0 - longest stream with one flip is 1
    if len(ones) == 0:
        return 1
    # only one stream - length(stream) + 1 e.g. [3,5] -> (3,4,5) -> length([3,5]) + 1 = 4
    if len(ones) == 1:
        return ones[0][1] - ones[0][0] + 2
    max_len = 0
    for i in range(len(ones)-1):
        # get two consecutive stream 
        curr, next = ones[i], ones[i+1]
        # update maxlen if length of this stream is greatest
        max_len = max(max_len,curr[1]-curr[0] + 2)
        # if we can concat streams with one bit flip 
        if curr[1] + 2 == next[0]:
            max_len = max(max_len,next[1]-curr[0]+1)
    # check last stream
    max_len = max(max_len, ones[-1][1] - ones[-1][0] + 2)
            
    return max_len
    
# Test 1
print(flipBit(1775))

# Test 2
print(flipBit(31))

# Test 3
print(flipBit(0))
# Test 4
print(flipBit(19))        
    