class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive numbers
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        quotient = 0
        while dvd >= dvs:
            temp = dvs
            multiple = 1
            while dvd >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dvd -= temp
            quotient += multiple
        
        return -quotient if negative else quotient