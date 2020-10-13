#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:47:36 2020

@author: xuguiming
"""

# 机器人遍历二维空间，坐标数位之和不得大于k

def sums(x):
    s = 0
    while x != 0:
        s += x % 10
        x  = x//10
    return s

print(sums(98))

# 深度优先遍历

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si+sj or (i,j) in visited:
                return 0
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
        visited = set()
        return dfs(0,0,0,0)
    
solution = Solution()
print(solution.movingCount(12,12,9))

# 广度优先遍历

class Solution:
    def movingCount(self, m:int, n:int, k:int) -> int:
        queue, visited = [(0,0,0,0)],set()
        while queue:
            i , j, si, sj = queue.pop(0)
            if i >= m or j >= n or k < si+sj or (i,j) in visited:
                continue
            visited.add((i,j))
            queue.append((i+1, j , si + 1 if (i+1)%10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)

O(MN)
