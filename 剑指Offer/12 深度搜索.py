#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:08:21 2020

@author: xuguiming
"""


def exist(board,list,word):
    def dfs(i,j,k):
        # 行或列节点越界
        if not 0 <= i < len(board)or not 0 <= j < len(board[0]) \
        or board[i][j] != word[k]: # 当前矩阵与目标字符不同 
            return False
        # 全部匹配完成
        if k == len(word) - 1:
            return True
        tmp, board[i][j] = board[i][j], '/'
        res = dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs[i,j+1,k+1] or dfs[i,j-1,k+1]
        board[i][j] = tmp
        return res
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i,j,0):
                return True
    return False

exist()