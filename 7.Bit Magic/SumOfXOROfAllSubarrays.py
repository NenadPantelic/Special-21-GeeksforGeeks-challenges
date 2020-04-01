#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:39:26 2020

@author: nenad
"""
"""
https://cs.stackexchange.com/questions/18194/algorithm-to-add-sum-of-every-possible-xor-sum-sub-array
https://math.stackexchange.com/questions/712487/finding-xor-of-all-subsets
https://www.geeksforgeeks.org/sum-of-xor-of-all-subarrays/

"""
# all subsequences
def sum_of_XOR(arr,n):
    res = arr[0]
    for i in range(1,n):
        res = res | arr[i]
    
    return res * 2 ** (n-1)


def sum_of_XOR(arr,n):
    prefix_masks = []
    mask = 0 
    for i in range(n):
        mask = mask ^ arr[i]
        prefix_masks.append(mask)
    sum  = 0
    #print(prefix_masks)
    for i in range(n):
        for j in range(i,n):
            if i != 0: 
                sum += prefix_masks[j] ^ prefix_masks[i-1]
            else: 
                sum += prefix_masks[j]
    return sum

# Python3 program to find the Sum of 
# XOR of all subarray of the array 
  
# Function to calculate the Sum of XOR 
# of all subarrays 

from math import ceil
def sum_of_XOR(arr, n): 
    sum = 0
    mul = 1
    maxx = len(bin(max(arr))[2:])
    for i in range(maxx+1): 
  
        counter = counter_odd = 0
        for j in range(n): 
            if ((arr[j] & (1 << i)) > 0): 
                counter = 1-counter
            if (counter): 
                 counter_odd += 1
        for j in range(n): 
            sum += (mul * counter_odd) 
            # check ith bit in arr[j]
            if ((arr[j] & (1 << i)) > 0): 
                counter_odd = (n - j - counter_odd) 
          
        mul *= 2
      
    return sum


def findXorSum(arr, n): 
      
    # variable to store the final Sum 
    Sum = 0
  
    # multiplier 
    mul = 1
  
    for i in range(30): 
  
        # variable to store number of sub-arrays  
        # with odd number of elements with ith  
        # bits starting from the first element  
        # to the end of the array 
        c_odd = 0
  
        # variable to check the status of the  
        # odd-even count while calculating c_odd 
        odd = 0
  
        # loop to calculate initial 
        # value of c_odd 
        counter = 0
        for j in range(n): 
            if ((arr[j] & (1 << i)) > 0): 
                odd = (~odd) 
                counter += 1
            #print(odd)
            if (odd):
                #print(odd)
                #print("USAO DVA")
                c_odd += 1
        print(ceil(counter/2))
        print(c_odd)
        break
          
        # loop to iterate through all the  
        # elements of the array and update Sum 
        for j in range(n): 
            Sum += (mul * c_odd) 
  
            if ((arr[j] & (1 << i)) > 0): 
                c_odd = (n - j - c_odd) 
  
        # updating the multiplier 
        mul *= 2
      
    # returning the Sum 
    return Sum
  
# Driver Code 
arr = [3, 8, 13] 
  
n = len(arr) 
  
print(findXorSum(arr, n)) 
  
# Driver Code 
arr = [3, 8, 13] 
  
n = len(arr) 
  
print(sum_of_XOR(arr, n)) 
  
# This code is contributed by Mohit Kumar 


# # # Test 1
# arr = [3,8, 13]
# print(sum_of_XOR(arr, 3))
# # # Test 1
# arr = [1080,1660, 2080]
# print(sum_of_XOR(arr, 3))

# s = 1080 + (1080^1660) + (1080^1660^2080) + 1660 + (1660^2080) + 2080 + (1080^2080)
# print(s)