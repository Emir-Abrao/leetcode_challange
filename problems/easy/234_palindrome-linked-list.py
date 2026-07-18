from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Find middle of the list using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Compare first half and reversed second half
        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True