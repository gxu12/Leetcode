#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 00:55:01 2020

@author: xuguiming
"""


# 根据前序以及中序 推出二叉树

# 1. 递归

def buildTree(preorder,inorder):
    if len(preorder) == 0:
        return None
    ind = inorder.index(preorder[0])
    root = TreeNode(preorder[0])
    
    #ind表示左子树有多少个元素，所以这里是从1到ind+1
    left = buildTree(preorder[1:ind+1],inorder[:ind])
    right = buildTree(preorder[ind+1:],inorder[ind+1:])
    root.left = left
    root.right = right
    return root


# 2. 分治思想

from typing import List

class Solution:
    def __init__(self):
        self.preorder = None
        self.reverses = None
        
    def buildTree(self,preorder,inorder):
        pre_size = len(preorder)
        in_size = len(inorder)
        if pre_size != in_size:
            return None
        
        self.preorder = preorder
        self.reverses = dict()
        for i in range(in_size):
            self.reverses[inorder[i]] = i
        return self.__build_tree(0,pre_size-1，0，in_size-1)
    
    def __build_tree(self,pre_left,pre_right,in_left,in_right):
        if pre_left > pre_right or in_left > in_right:
            return None
        
        pivot = self.preorder[pre_left]
        root = TreeNode(pivot)
        pivot_index = self.reverses[pivot]
        root.left = self.__build_tree(pre_left + 1, pivot_index - in_left + pre_left,
                                      in_left, pivot_index - 1)
        root.right = self.__build_tree(pivot_index - in_left + pre_left + 1，
                                       pivot_index + 1, in_right)
        
        
        
        
        
        
        
        
        
        
        
        
        
