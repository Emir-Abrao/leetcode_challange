class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        # Create combined string: s + "#" + reverse(s)
        combined = s + "#" + s[::-1]
        
        # Build KMP table (failure function)
        n = len(combined)
        lps = [0] * n
        
        j = 0
        for i in range(1, n):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            
            if combined[i] == combined[j]:
                j += 1
                lps[i] = j
            else:
                lps[i] = 0
        
        # lps[-1] gives us the length of longest palindrome prefix
        palindrome_len = lps[-1]
        
        # Add reverse of the non-palindrome suffix to the front
        suffix = s[palindrome_len:]
        return suffix[::-1] + s