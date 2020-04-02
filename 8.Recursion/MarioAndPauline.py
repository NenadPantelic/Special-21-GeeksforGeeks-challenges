#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:48:01 2020

@author: nenad
"""


"""
Problem URL:https://practice.geeksforgeeks.org/contest-problem/mario-pauline/1/

"""

def isSafe(x, y, x1,y1):
    # if current position is in range - lower than x and y coord of target position
    return x >= 1 and x <= x1 and y >= 1 and y <= y1
        

def isPossible(sx, sy, dx, dy):
    res = gridMove(sx,sy,dx,dy)
    return res

    
    
    
def gridMove(x,y,x1,y1):
    # if we reached the final position
    if x == x1 and y == y1:
        return True 
    
    
    if isSafe(x,y,x1,y1):
        # go right
        res1 = gridMove(x+y, y, x1,y1)
        if res1:
            return res1
        # go up
        res2 = gridMove(x, x+y, x1,y1)
        if res2:
            return res2
        return False
    
print(isPossible(3, 2, 5, 7))    
print(isPossible(1, 2, 3, 4))