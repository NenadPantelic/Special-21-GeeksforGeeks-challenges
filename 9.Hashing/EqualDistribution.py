#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:30:53 2020

@author: nenad
"""
"""
Problem URL: https://practice.geeksforgeeks.org/contest-problem/equal-distribution/1/
Problem descirption: Nancy has N boxes which contains some chocolates. She wants to distribute maximum number of chocolates equally among her K friends by selecting a consecutive sequence of boxes . Help Nancy in finding the maximum number of chocolates she can give to each of her friend.
Note: She cannot cut a chocolate into pieces, and every friend should receive equal number of chocolates
"""
# Time: O(n), space: O(n)
def maxNumOfChocolates(arr, n, k): 
    remainderMap = {}
    maxSum = 0
    cumsum = []
    sum = 0
    # cumsum array
    for i in range(n):
        sum += arr[i]
        cumsum.append(sum)
        
    # very important
    # if (sum[i] % k) == (sum[j] % k), 
    # where sum[i] = sum(arr[0]+..+arr[i]) and sum[j] = sum(arr[0]+..+arr[j])
    # and ‘i’ is less than ‘j’, then sum(arr[i+1]+..+arr[j]) must be divisible by k.
    # Condition **   
    # x mod p = a
    # (x + d) mod p = a
    # then d mod p = 0
    for i in range(n):
        rem = cumsum[i] % k
        if rem == 0:
            maxSum = max(maxSum, cumsum[i])
        if rem not in remainderMap:
            remainderMap[rem] = i
        # follows from condition **
        diff = cumsum[i] - cumsum[remainderMap[rem]]
        maxSum = max(maxSum, diff)
    return maxSum // k

# Test 1
arr = [2, 7, 6, 1, 4, 5]
n = 6
k = 3
print(maxNumOfChocolates(arr, n, k))
    
    
    
    
    