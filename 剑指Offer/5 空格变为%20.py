#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 00:21:09 2020

@author: xuguiming
"""



# 使用循环

def replaceSpace(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            s[i] = '%20'
    return ''.join(s)

# 时间，空间 O(n),O(n）

# append
    
def replaceSpace(s):
    if s:
        res = []
        for i in range(len(s)):
            if s[i] == ' ':
                res.append('%20')
            else:
                res += s[i]
        return ''.join(res)
    return None

print(replaceSpace('My name is Ming'))
