from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        side_length = total // 4
        matchsticks.sort(reverse=True)
        
        if matchsticks[0] > side_length:
            return False
        
        sides = [0] * 4
        
        def backtrack(index):
            if index == len(matchsticks):
                return all(side == side_length for side in sides)
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= side_length:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                
                # Optimization: if this side is empty and we couldn't place the matchstick here,
                # no point trying other empty sides
                if sides[i] == 0:
                    break
            
            return False
        
        return backtrack(0)