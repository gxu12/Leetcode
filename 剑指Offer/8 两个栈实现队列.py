#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 01:41:43 2020

@author: xuguiming
"""


# 根据两个栈实现队列的 appendtail 以及 deletehead

# 1. 

class CQueue:
    def __init__(self):
        self.A, self.B = [], []
    def appendTail(self，value):
        self.A.append(value)
    def deleteHead(self):
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()