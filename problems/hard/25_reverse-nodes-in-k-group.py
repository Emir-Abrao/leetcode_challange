from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            kth_node = self.getKthNode(prev_group_end, k)
            if not kth_node:
                break
            
            next_group_start = kth_node.next
            
            prev, curr = kth_node.next, prev_group_end.next
            while curr != next_group_start:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prev_group_end.next
            prev_group_end.next = kth_node
            prev_group_end = temp
        
        return dummy.next
    
    def getKthNode(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr