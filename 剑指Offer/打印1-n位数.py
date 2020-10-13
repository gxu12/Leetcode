#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:15:44 2020

@author: xuguiming
"""

class Solution:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x,begin0):
            if x == n: # 终止条件：已固定完所有位
                s = ''.join(num)
                if s:
                    res.append(int(s)) # 拼接 num 并添加至 res 尾部
                return
            for i in range(10): # 遍历 0 - 9
                if begin0 and i != 0:
                    begin0 = False
                if not begin0:
                    num[x] = str(i) # 固定第 x 位为 i
                dfs(x + 1, begin0) # 开启固定第 x + 1 位
        begin0 = True
        num = [''] * n # 起始数字定义为 n 个 0 组成的字符列表
        res = [] # 数字字符串列表
        dfs(0,begin0) # 开启全排列递归
        return res  # 拼接所有数字字符串，使用逗号隔开，并返回
    
print(Solution().printNumbers(2))