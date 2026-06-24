from __future__ import annotations
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(in_left, in_right):
            if in_left > in_right:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            root_idx = inorder_map[root_val]
            
            root.right = build(root_idx + 1, in_right)
            root.left = build(in_left, root_idx - 1)
            
            return root
        
        return build(0, len(inorder) - 1)