from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        rightmost_set_bit = xor_all & (-xor_all)
        
        a = 0
        b = 0
        for num in nums:
            if num & rightmost_set_bit:
                a ^= num
            else:
                b ^= num
        
        return [a, b]