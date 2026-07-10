class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        
        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        # Work with absolute values
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # Integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        if remainder == 0:
            return "".join(result)
        
        # Decimal part
        result.append(".")
        remainder_map = {}
        
        while remainder != 0:
            if remainder in remainder_map:
                # Found repeating cycle
                start_pos = remainder_map[remainder]
                result.insert(start_pos, "(")
                result.append(")")
                break
            
            # Record position where this remainder's digit starts
            remainder_map[remainder] = len(result)
            
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(result)