from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        
        curr = l1
        while curr:
            stack1.append(curr.val)
            curr = curr.next
        
        curr = l2
        while curr:
            stack2.append(curr.val)
            curr = curr.next
        
        carry = 0
        result = None
        
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            new_node = ListNode(digit)
            new_node.next = result
            result = new_node
        
        return result