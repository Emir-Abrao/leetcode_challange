from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        total_sum = sum(nums)
        
        # Calculate F(0)
        f = sum(i * nums[i] for i in range(n))
        
        max_f = f
        
        # Calculate F(1), F(2), ..., F(n-1)
        for k in range(1, n):
            # When rotating from k-1 to k, the element at index (n-k) moves to front
            # F(k) = F(k-1) + total_sum - n * nums[n-k]
            f = f + total_sum - n * nums[n - k]
            max_f = max(max_f, f)
        
        return max_f