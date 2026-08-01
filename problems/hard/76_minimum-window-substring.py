class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Count characters needed from t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        required = len(t_count)
        formed = 0
        
        # Current window character counts
        window_count = {}
        
        # Result: (window_length, left, right)
        result = float('inf'), 0, 0
        
        left = 0
        
        for right in range(len(s)):
            # Add character from right to window
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # Check if this character satisfies the requirement
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Try to contract the window
            while left <= right and formed == required:
                char = s[left]
                
                # Update result if this window is smaller
                if right - left + 1 < result[0]:
                    result = (right - left + 1, left, right)
                
                # Remove character from left
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                left += 1
        
        return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]