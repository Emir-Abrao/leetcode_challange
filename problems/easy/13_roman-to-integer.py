class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        n = len(s)
        
        for i in range(n):
            current_val = roman_values[s[i]]
            
            if i < n - 1 and current_val < roman_values[s[i + 1]]:
                result -= current_val
            else:
                result += current_val
        
        return result