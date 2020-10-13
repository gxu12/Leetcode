#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:28:18 2020

@author: xuguiming
"""


# 二进制求1的个数

class Solution:
    def hammingWeight(self,n:int) -> int:
        res = 0
        while n :
            res += n & 1
            n >>= 1
        return res
    

# n&(n-1)
        
class Solution:
    def hammingWeight(self,n:int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
