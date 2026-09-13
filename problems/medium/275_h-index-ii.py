from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            # If this paper has at least (n - mid) citations,
            # then there are at least (n - mid) papers with that many citations
            if citations[mid] >= n - mid:
                right = mid
            else:
                left = mid + 1
        return n - left