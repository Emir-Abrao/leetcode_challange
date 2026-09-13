from typing import List
from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort by width ascending, and for equal width by height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Extract heights
        heights = [h for _, h in envelopes]
        
        # Compute LIS of heights
        tails = []
        for h in heights:
            idx = bisect_left(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h
        
        return len(tails)