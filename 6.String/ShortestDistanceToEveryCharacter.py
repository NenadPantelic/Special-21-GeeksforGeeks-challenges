#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:07:07 2020

@author: nenad
"""





def shortestDistance(S, X): 
    # Your code goes here
    positions = []
    for i in range(len(S)):
        if S[i] == X:
            positions.append(i)
            
    q1 = q2 = None
    distances = []            
    for i in range(len(S)):
        if S[i] == X:
            distances.append(0)
            if not q1:
                    q1 = positions[0]
            if not q2:
                if len(positions) > 1:
                    q2 = positions[1]
            if q1 and q2:
                dist1 = abs(q1 - i)
                dist2 = abs(q2- i)
                if dist2 <= dist1:
                    positions.remove(q1)
                    q1 = q2 = None   

        elif len(positions) < 2:
            distances.append(abs(positions[0]-i))
            
        else:
            if not q1:
                q1 = positions[0]
            if not q2:
                q2 = positions[1]
            
            dist1 = abs(q1 - i)
            dist2 = abs(q2- i)
            if dist2 <= dist1:
                positions.remove(q1)
                q1 = q2 = None
                distances.append(dist2)
            else:
                distances.append(dist1)
    return distances
# Test 1
s1 = "geeksforgeeks"
X = "e"
print(shortestDistance(s1,X))


# Test 2
s1 = "helloworld"
X = "o"
print(shortestDistance(s1,X))

# Test 3
s1 = "abbbabbbabbb"
X = "a"
print(shortestDistance(s1,X))
print(shortestDistance(s1,"b"))
        