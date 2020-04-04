#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:25:22 2020

@author: nenad
"""

"""
Problem URL: https://practice.geeksforgeeks.org/contest-problem/count-triplets/1/
    
Problem description:
Given a sorted linked list of distinct nodes (no two nodes have the same data) and an integer X. Count distinct triplets in the list that sum up to given integer X.

Input:The first line of input contains an integer T denoting number of test cases. For each test case, there are two lines of input. First line contains two integers size of linked list( N ) and the value X . Next line contains reversely sorted N integers.

Output:For each test case, print the count of triplets with given sum X .

Your Task:You have to complete the function countTriplets() which takes head pointer of sorted linked list and given value X as parameters and returns count of triplets.

"""

class Node:
    def __init__(self,x):
        self.val=x
        self.nxt=None

# Time: O(n^2), space: O(1)
def countTriplets(head,x):
    node = head
    uniqueEls = {}
    els = []
    count = 0
    i = 0
    while node:
        val = node.val
        # create map and list of these elements
        els.append(val)
        uniqueEls[val] = i
        i += 1
        node = node.nxt
    # there is less than 3 elements
    if len(els) < 3:
        return 0
    
    for i in range(len(els)):
        val = els[i]
        # violation
        if val >= x:
            continue
        for j in range(i+1, len(els)):
            sum = val + els[j]
            # violation
            if sum >= x:
                continue
            # search for third element
            index = uniqueEls.get(x-sum, -1)
            # for uniqueness - check if it's index is greater than second element's index 
            if index > j:
                #print(els[i], els[j], x-sum)
                count += 1
                
    return count
                

# Test 1
l1 = Node(9)
l2 = Node(8)
l3 = Node(6)
l4 = Node(5)
l5 = Node(4)
l6 = Node(2)
l7 = Node(1)
l1.nxt = l2
l2.nxt = l3
l3.nxt = l4
l4.nxt = l5
l5.nxt = l6
l6.nxt = l7
print(countTriplets(l1, 17))
print(countTriplets(l1, 15))

