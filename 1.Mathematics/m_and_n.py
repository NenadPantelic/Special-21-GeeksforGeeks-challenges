#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:36:24 2020

@author: nenad
"""


"""

Problem descritpion:  Given two positive integers M and N, after adding M and N if number 
of digits in M+N and N are same return N otherwise return M+N.

Problem link: https://practice.geeksforgeeks.org/contest-problem/m-and-n5047/0/


"""
from math import log, ceil
def add_m_and_n(m,n):
    sum  = m + n
    # ceil(log(val,10)) - returns approx number of digits in number val
    if ceil(log(sum, 10)) == ceil(log(n,10)):
        return n
    else:
        return sum
    
# Test 1
m = 44
n = 22
print(add_m_and_n(m,n))

# Test 1
m = 99
n = 12
print(add_m_and_n(m,n))
    