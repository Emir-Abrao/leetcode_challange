from __future__ import annotations
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.preorder_idx = 0
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            self.preorder_idx += 1
            
            inorder_idx = inorder_map[root_val]
            
            root.left = build(left, inorder_idx - 1)
            root.right = build(inorder_idx + 1, right)
            
            return root
        
        return build(0, len(inorder) - 1)