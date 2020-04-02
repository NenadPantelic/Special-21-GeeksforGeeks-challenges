#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:56:38 2020

@author: nenad
"""
"""
Problem URL: https://practice.geeksforgeeks.org/contest-problem/check-tree-traversal/1/

"""
# O(n^2)
def checktree(preorder, inorder, postorder, length): 
    # all arrays are examined already
    if length <= 0:
        return True
   
    # if all arrays have one element to examine
    if length == 1:
        #if len(preorder) and len(inorder) and len(postorder):
        return preorder[0] == inorder[0] == postorder[0]
        #return False
    inord_ind = None
    for i in range(len(inorder)):
        if inorder[i] == preorder[0]:
            inord_ind = i
            break
    # trees are different
    if inord_ind is None:
        return False 
    if preorder[0] != postorder[length-1]:
         return False
    # check preorder[0]'s left subtree
    # first element already examined
    left_subtree = checktree(preorder[1:], inorder, postorder, inord_ind)
    # check preorder[0]'s right subtree
    right_subtree = checktree(preorder[inord_ind+1:], inorder[inord_ind+1:], \
                              postorder[inord_ind:], length-inord_ind-1)
    return left_subtree and right_subtree
        
# Test 1
preorder = [1, 2, 4, 5, 3]
inorder = [4, 2, 5, 1, 3]
postorder = [4, 5, 2, 3, 1]
print(checktree(preorder, inorder, postorder, len(preorder)))


# Test 2

preorder = [1, 5, 4, 2, 3]
inorder = [4, 2, 5, 1, 3]
postorder = [4, 1, 2, 3, 5]
print(checktree(preorder, inorder, postorder, len(preorder)))