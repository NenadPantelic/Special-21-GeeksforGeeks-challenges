#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:31:57 2020

@author: nenad
"""


def compress(s):
    # length of longest substring
      maxLen = 0
      i = 0
      n = len(s)
      # start index of stream
      startIndex = 0
      compressed = []
      # positions positions in string
      positions = {}
      substr = ""
      while i < n:
          # check if char is already seen
          position = positions.get(s[i], None)
          # if not present - just go further
          if position is not None:
              # occurence of the current character is from this window
              if position >= startIndex:
                  # stream length is difference between current position(i) and starting position of that stream (window)
                  #maxLen = max(maxLen, i - startIndex)
                  if s[position:position+len(substr)] == s[i:i+len(substr)]:
                      i += len(substr)
                      compressed.append("*")
                  # start from the position+1 where we previously find this char
                  startIndex = i
                  substr = ""
          else:
              substr += s[i]
              compressed.append(s[i])
              i += 1
    
          # update char position - insert new one, or update the existing one
          if i < n:
              positions[s[i]] = i
          
      # if string ending makes non-repeating stream
      #maxLen = max(maxLen, i - startIndex)   
      return "".join(compressed)
  
s = "ababcababcd"
print(compress(s))