from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        def backtrack(start, path):
            if len(path) >= 2:
                result.add(tuple(path))
            
            for i in range(start, len(nums)):
                if not path or nums[i] >= path[-1]:
                    backtrack(i + 1, path + [nums[i]])
        
        backtrack(0, [])
        return [list(seq) for seq in result]