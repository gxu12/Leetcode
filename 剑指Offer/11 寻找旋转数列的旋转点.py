#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:35:56 2020

@author: xuguiming
"""


def minArray(numbers):
        if not numbers:
            return None
        if len(numbers) == 1:
            return numbers[0]
        else:
            start = 0
            while numbers[start+1] > numbers[start]:
                start += 1
                if start == len(numbers) - 1:
                    return numbers[0]
            return numbers[start+1]
        
minArray([1,3,5])

# 二分法

def minArray(numbers):
    i,j = 0, len(numbers) - 1
    while i < j:
        m = (i+j) // 2
        if numbers[m] > numbers[j]:
            i = m + 1
        elif numbers[m] < numbers[j]:
            j = m 
        else:
            j -= 1
    return numbers[i]

print(minArray([3,4,5,6,7,1,2]))