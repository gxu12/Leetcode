#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 00:12:02 2020

@author: xuguiming
"""

# 切绳子

# 1. 长度为3
import math

class Solution:
    def cuttingRope(self,n:int) -> int:
        if n <= 3:
            return n - 1
        a,b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3,a))
        if b == 1:
            return int(math.pow(3,a-1)*4)
        return int(math.pow(3,a)*2)
    
    