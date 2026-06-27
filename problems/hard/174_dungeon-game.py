from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # dp[i][j] represents the minimum health needed when entering cell (i, j)
        # to reach the princess
        dp = [[float('inf')] * n for _ in range(m)]
        
        # Start from bottom-right corner (where princess is)
        # At the last cell, we need at least 1 HP after taking the dungeon value
        # So if dungeon[m-1][n-1] = -5, we need 1 - (-5) = 6 HP before entering
        # If dungeon[m-1][n-1] = 10, we need 1 - 10 = -9, but minimum is 1
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        
        # Fill last column (can only come from below, but there's nothing below)
        for i in range(m-2, -1, -1):
            # Health needed at (i, n-1) = health needed at (i+1, n-1) - dungeon[i][n-1]
            # But must be at least 1
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        
        # Fill last row (can only come from right, but there's nothing to the right)
        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
        
        # Fill the rest of the table from bottom-right to top-left
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                # We can go either right or down
                # Choose the path that requires minimum health
                min_health_on_exit = min(dp[i+1][j], dp[i][j+1])
                # Health needed before entering this cell
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
        
        return dp[0][0]