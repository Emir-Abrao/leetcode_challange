from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total = 0
        
        for i in range(len(timeSeries) - 1):
            # Add the minimum of duration or gap between attacks
            total += min(duration, timeSeries[i + 1] - timeSeries[i])
        
        # Add the duration of the last attack
        total += duration
        
        return total