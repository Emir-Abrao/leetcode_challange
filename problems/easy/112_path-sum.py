from __future__ import annotations

from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # Leaf: no children
        if not root.left and not root.right:
            return root.val == targetSum
        # Node with only a right child: it can be a valid endpoint, but also continue searching
        if not root.left:
            return (root.val == targetSum) or self.hasPathSum(root.right, targetSum - root.val)
        # Node with only a left child: not a leaf, continue searching
        if not root.right:
            return self.hasPathSum(root.left, targetSum - root.val)
        # Node with both children
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)