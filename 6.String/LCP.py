#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:05:15 2020

@author: nenad
"""


def LCP(arr,n):
    prefix = []
    lens = [len(a) for a in arr]
    minLen= min(lens)
    for i in range(minLen):
        prefStr = "".join([arr[j][i] for j in range(n)])
        if prefStr.count(arr[0][i]) == n:
            prefix.append(arr[0][i])
        else:
            break
    if len(prefix) == 0:
        return "-1"
    return "".join(prefix)

# Test 1
arr = ["apple", "ape", "application"]
print(LCP(arr, 3))

# Test 2
arr = "geeksforgeeks geeks geek geezer".split()
print(LCP(arr,4))

# Test 2
arr = "geeksforgeeks sgeeks ageek cgeezer".split()
print(LCP(arr,4))