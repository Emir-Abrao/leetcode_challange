from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(float('-inf'))
        current = head
        
        while current:
            next_node = current.next
            
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            current.next = prev.next
            prev.next = current
            
            current = next_node
        
        return dummy.next