#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:47:47 2020

@author: nenad
"""

"""
Problem URL: https://practice.geeksforgeeks.org/contest-problem/sort-strings-lexicographically-according-to-given-sequence-of-characters/1/
Problem description: 
    Given a string of lower case letters alphabets representing alphabetical order in an alien language. Sort the given list of words lexicographically according to that order.
Words will contain only those letters which are the in the alphabets string.



"""
        
from string import ascii_lowercase      
def sort_by_order(words, alphabets):
    # we take subsequence of length len(alphabets) from string of natural order of alphabet
    chars = ascii_lowercase[:len(alphabets)]
    # we map chars - e.g. q->a, w->b, e->c, r->d, t->e, y->f
    char_map = {alphabets[i]:chars[i] for i in range(len(alphabets))}
    words_map = {}
    new_words = []
    for word in words:
        # we map words based on char_map
        new_word = "".join([char_map[c] for c in word])
        new_words.append(new_word)
        words_map[new_word] = word
    # sort mapped words
    new_words.sort()
    # arrange input array based on order of mapped array
    for i in range(len(new_words)):
        words[i] = words_map[new_words[i]]
        
    return words
    
alphabets = "qwerty"
words = "we qwer erer qw errr".split()
print(sort_by_order(words, alphabets))
