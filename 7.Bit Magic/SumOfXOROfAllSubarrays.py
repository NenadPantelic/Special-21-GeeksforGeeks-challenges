#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:39:26 2020

@author: nenad
"""
"""
https://cs.stackexchange.com/questions/18194/algorithm-to-add-sum-of-every-possible-xor-sum-sub-array
"""
# all subsequences
def sum_of_XOR(arr,n):
    res = arr[0]
    for i in range(1,n):
        res = res | arr[i]
    
    return res * 2 ** (n-1)

#print(sum_of_XOR([1,2,3], 3))
#print(sum_of_XOR([3, 8, 13], 3))

def sum_of_XOR(arr,n):
    prefix_masks = []
    mask = 0 
    for i in range(n):
        mask = mask ^ arr[i]
        prefix_masks.append(mask)
    sum  = 0
    # O(n^2)
    for i in range(n):
        for j in range(i,n):
            if i != 0: 
                sum += prefix_masks[j] ^ prefix_masks[i-1]
            else: 
                sum += prefix_masks[j]
    return sum


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

def sum_of_XOR(arr,n):
    for i in range(1,n):
        arr[i] ^= arr[i-1]
    ret=0
    p = 1
    maxx = len(bin(max(arr))[2:])

    for i in range(maxx+1):
        c = 0
        for j in range(n):
            if (arr[j] & p):
                c+=1
                
        ret+=c*(n-c+1)*p
        p *= 2
        # p <<= 1
    return ret
    
 

  
arr = [3, 8, 13] 
n = len(arr) 
print(sum_of_XOR(arr, n)) 

# s = 1080 + (1080^1660) + (1080^1660^2080) + 1660 + (1660^2080) + 2080 + (1080^2080)
# print(s)