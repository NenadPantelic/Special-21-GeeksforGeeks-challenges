#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:02:30 2020

@author: nenad
"""


"""
Problem URL: https://practice.geeksforgeeks.org/contest-problem/perfect-pair-sum/1/

"""
from collections import defaultdict

def digitSum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum
def PerfectMatch(arr, n): 
    # map of digit sum and values which digits sum is that value
    digitSumMap = defaultdict(list)
    # for every value, calc digit sum
    for val in arr:
        digitSumMap[digitSum(val)].append(val)
    # default value
    maxSum = -1
    for sum in digitSumMap:
        values = digitSumMap[sum] 
        # only for those lists that are longer than 1 (have at least one pair)
        if len(values) > 1:
            # sort these numbers
            values.sort()
            # take two of them with the greatest value
            maxSum = max(maxSum, values[-1] + values[-2] )
    return maxSum

# Test 1
arr = [55,23,32,46,88]
print(PerfectMatch(arr,5))
    