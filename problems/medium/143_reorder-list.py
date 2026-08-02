from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Find the middle of the linked list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list into two halves
        second = slow.next
        slow.next = None
        
        # Reverse the second half
        prev = None
        curr = second
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        second = prev
        
        # Merge the two halves
        first = head
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2