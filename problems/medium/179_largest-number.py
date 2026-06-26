from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        nums_str = [str(num) for num in nums]
        nums_str.sort(key=cmp_to_key(compare))
        result = ''.join(nums_str)
        
        if result[0] == '0':
            return '0'
        
        return result