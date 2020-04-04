#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:47:23 2020

@author: nenad
"""

"""
Problem URL: https://practice.geeksforgeeks.org/contest-problem/add-a-digit/1/
Problem description: Given a linked list which represents an integer number where each node is a digit of the represented integer. The task is to add a given digit N to the represented integer.

"""

class Node:
    def __init__(self,x):
        self.val=x
        self.nxt=None
        
# Time: O(n), space: O(n)        
def add_to_list(head,n):
    # code here
    nodes_map = {}
    node = head
    i = 0
    while node:
        nodes_map[i] = node.val
        node = node.nxt
        i += 1
    length = i
    remainder = 0
    new_head = None
    for i in range(length - 1, -1, -1):
        val = n
        if i < length-1:
            val = 0
        curr_val = nodes_map[i]
        sum = curr_val + val + remainder
        nodes_map[i] = sum % 10
        remainder = sum // 10
    if remainder:
        new_head = Node(remainder)
        
    node = head
    i = 0
    while node:
        node.val = nodes_map[i]
        node = node.nxt
        i += 1
    if new_head:
        new_head.nxt = head
        head = new_head
        #return new_head
    return head
        
    
    
def print_list(head):
    node = head
    while node:
        print(node.val, end=" ")
        node = node.nxt
        
        
# Test 1
l1 = Node(9)
l2 = Node(0)
l3 = Node(1)
l1.nxt = l2
l2.nxt = l3
new_h = add_to_list(l1, 8)
print_list(new_h)
# Test 2
l4 = Node(9)
l5 = Node(9)
l6 = Node(2)
l4.nxt = l5
l5.nxt = l6
print()
new_h = add_to_list(l4, 9)
print_list(new_h)
print()


# Test 1
l1 = Node(9)
l2 = Node(9)
l3 = Node(9)
l4 = Node(9)
l5 = Node(9)
l6 = Node(9)
l7 = Node(9)
l8 = Node(9)
l9 = Node(9)
l1.nxt = l2
l2.nxt = l3
l3.nxt = l4
l4.nxt = l5
l5.nxt = l6
l6.nxt = l7
l7.nxt = l8
l8.nxt = l9
new_h = add_to_list(l1, 1)
print_list(new_h)
print()


