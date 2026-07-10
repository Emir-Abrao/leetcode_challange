class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        # Convert to 32-bit representation
        a = a & mask
        b = b & mask
        
        while b != 0:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry
        
        # If the result is negative (bit 31 is set), convert back to Python's negative representation
        if a > 0x7FFFFFFF:
            return ~(a ^ mask)
        return a