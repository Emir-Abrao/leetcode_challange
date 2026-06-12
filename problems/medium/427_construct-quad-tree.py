from __future__ import annotations
from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        def is_uniform(r, c, size):
            val = grid[r][c]
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        return False, val
            return True, val
        
        def build(r, c, size):
            uniform, val = is_uniform(r, c, size)
            
            if uniform:
                return Node(val == 1, True, None, None, None, None)
            
            half = size // 2
            topLeft = build(r, c, half)
            topRight = build(r, c + half, half)
            bottomLeft = build(r + half, c, half)
            bottomRight = build(r + half, c + half, half)
            
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return build(0, 0, len(grid))