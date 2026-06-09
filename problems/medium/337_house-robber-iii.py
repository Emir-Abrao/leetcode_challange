from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return (0, 0)
            
            left_rob, left_skip = helper(node.left)
            right_rob, right_skip = helper(node.right)
            
            rob_current = node.val + left_skip + right_skip
            skip_current = max(left_rob, left_skip) + max(right_rob, right_skip)
            
            return (rob_current, skip_current)
        
        rob_root, skip_root = helper(root)
        return max(rob_root, skip_root)