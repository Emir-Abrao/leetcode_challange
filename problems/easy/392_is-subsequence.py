class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        
        s_idx = 0
        
        for char in t:
            if char == s[s_idx]:
                s_idx += 1
                if s_idx == len(s):
                    return True
        
        return False