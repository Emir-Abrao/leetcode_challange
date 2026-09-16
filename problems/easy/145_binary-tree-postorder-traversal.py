from __future__ import annotations
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        last_visited = None
        
        while root or stack:
            # Go as left as possible
            while root:
                stack.append(root)
                root = root.left
            
            # Peek at the top of stack
            top = stack[-1]
            
            # If right child exists and not visited yet, go right
            if top.right and last_visited != top.right:
                root = top.right
            else:
                # Visit the node
                result.append(top.val)
                last_visited = stack.pop()
        
        return result