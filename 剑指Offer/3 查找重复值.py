#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:23:41 2020

@author: xuguiming
"""

# 3.

# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
# 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
# 请找出数组中任意一个重复的数字。

# [2,3,1,0,2,5,3] = [2 or 3]

# Solution 1:

# sort()

def findrepeated(list):
    list.sort()
    start = list[0]
    for i in range(len(list)):
        if start == i :
            return start
        start = list[i]
        
print(findrepeated([2,3,10,2,5,3,2]))

# HashSet

def findrepeated(list):
    dic = set()
    for num in list:
        if num in dic:
            return num
        dic.add(num)
    return -1

print(findrepeated([2,3,10,2,5,3,2]))