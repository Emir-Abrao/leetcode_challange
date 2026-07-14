from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_val = min(nums)
        return sum(num - min_val for num in nums)