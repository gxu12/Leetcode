#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:30:54 2020

@author: xuguiming
"""


#在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

'''
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
'''

# 找规律

list_ = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30],
  [22, 30, 40, 50, 60]
]

def numberin2Darray(matrix,target):
    if not matrix:
        return False
    m,n = len(matrix), len(matrix[0])
    row, col = m-1, 0
    while row >= 0 and col < n:
        if matrix[row][col] < target:
            col += 1
        elif matrix[row][col] > target:
            row -= 1
        else:
            return True
    return False

print(numberin2Darray(list_, 60))

# 二分法

class Solution:
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix) - 1 if vertical else len(matrix[0]) - 1 # 垂直搜索：hi = 行数 - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if vertical:  # 垂直搜索
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else: 
                    return True
            else:   # 水平搜索
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True

        return False
    
    def findNumberin2DArray(self,matrix,target):
        if not matrix:
            return False
        for i in range(min(len(matrix),len(matrix[0]))):
            vertical_found = self.binary_search(matrix,target,i,True)
            horizontal_found = self.binary_search(matrix,target,i,False)
            if vertical_found or horizontal_found:
                return True
        return False

Solution = Solution()
print(Solution.findNumberin2DArray(list_, 25))

# 右上角开始

def findNumberin2DArray(matrix,target):
    n = len(matrix)
    row, col = 0, len(matrix[0])-1
    while row <= len(matrix) and col >= 0 :
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return True
    return False

print(findNumberin2DArray(list_, 17))
            


    