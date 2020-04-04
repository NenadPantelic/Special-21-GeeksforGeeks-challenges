#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:55:58 2020

@author: nenad
"""

"""
Problem URL: https://practice.geeksforgeeks.org/contest-problem/rotate-clockwise/1/
Problem description: 
"""
''' 
Definition for singly linked list 
'''
class Node:
    def __init__(self,x):
        self.val=x
        self.nxt=None

# Time: O(n), space: O(1)
def rotate(head,k):
    # Your code goes here
    node = head
    length = 0
    prev_node = None
    # determine length of LL
    while node:
        length += 1
        prev_node = node
        node = node.nxt
    tail = prev_node
    i = 0
    prev_node = None
    node = head
    while node:
        # search for new head's position
        if (i + k) % length == 0:
            break
        i += 1
        prev_node = node
        node = node.nxt
    new_head = node
    # terminate list if new trail is different than old tail (case when k is multiplication of length of list)
    if prev_node:
        prev_node.nxt = None
    # connect new tail with old head
    if i != 0:
        tail.nxt = head
    return new_head

def print_list(head):
    node = head
    while node:
        print(node.val, end=" ")
        node = node.nxt

# # Test 1
l1 = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l5 = Node(5)
l1.nxt = l2
l2.nxt = l3
l3.nxt = l4
l4.nxt = l5

new_head = rotate(l1, 2)
print_list(new_head)


# Test 2
l1 = Node(7)
l2 = Node(9)
l3 = Node(11)
l4 = Node(13)
l5 = Node(3)
l6 = Node(5)
l1.nxt = l2
l2.nxt = l3
l3.nxt = l4
l4.nxt = l5
l5.nxt = l6

new_head = rotate(l1, 12)
print_list(new_head)


    
    

