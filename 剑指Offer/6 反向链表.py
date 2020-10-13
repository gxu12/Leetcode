#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 00:42:51 2020

@author: xuguiming
"""


# 打印出反转的链表

# 1. 反转

def reversePrint(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res[::-1]

O(n), O(n)

# 2. 递归
    
def reversePrint(head):
    if not head:
        return 
    return reversePrint(head.next) + [head.val]

O(n), O(n)

# 3. 堆栈（先进后出）

def reversePrint(self,head):
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    res = []
    while stack:
        res.append(stack.pop())
    return res

O(n), O(n)