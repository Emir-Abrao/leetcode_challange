from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add virtual balloons with value 1 at both ends
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] represents max coins we can get by bursting balloons between i and j (exclusive)
        dp = [[0] * n for _ in range(n)]
        
        # Length of the interval (exclusive of boundaries)
        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                # Try bursting each balloon k as the LAST balloon in range (left, right)
                for k in range(left + 1, right):
                    # When k is the last balloon to burst in (left, right),
                    # left and right are still there, so we get nums[left] * nums[k] * nums[right]
                    coins = nums[left] * nums[k] * nums[right]
                    coins += dp[left][k] + dp[k][right]
                    dp[left][right] = max(dp[left][right], coins)
        
        return dp[0][n - 1]