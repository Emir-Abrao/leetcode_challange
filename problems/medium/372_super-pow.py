from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        
        def powmod(base, exp, mod):
            result = 1
            base = base % mod
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                exp = exp >> 1
                base = (base * base) % mod
            return result
        
        # Use the property: a^(xy) = (a^x)^y
        # We can process b digit by digit from left to right
        # If b = [d1, d2, d3], then b = d1*100 + d2*10 + d3
        # a^b = a^(d1*100 + d2*10 + d3) = (a^(d1*100))^1 * (a^(d2*10))^1 * (a^d3)
        # More generally: a^(10*x + y) = (a^x)^10 * a^y
        
        result = 1
        for digit in b:
            # result = result^10 * a^digit
            result = powmod(result, 10, MOD) * powmod(a, digit, MOD) % MOD
        
        return result