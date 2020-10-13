#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:02:17 2020

@author: xuguiming
"""

# 动态规划
def Fibonacci(n):
    start = 0
    first = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n):
            start, first = first, start+first
        return start % 1000000007
    
    
print(Fibonacci(45))

# 递归

def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (Fibonacci(n-1)+Fibonacci(n-2)) % 1000000007

print(Fibonacci(5))

# 记忆法递归

def Fibonacci(n):
    records = [-1 for i in range(n+1)]
    if n == 0:
        return 1
    if n == 1:
        return 1
    if records[n] == -1:
        records[n] = Fibonacci(n-1) + Fibonacci(n-2)
    return records[n]

print(Fibonacci(7))