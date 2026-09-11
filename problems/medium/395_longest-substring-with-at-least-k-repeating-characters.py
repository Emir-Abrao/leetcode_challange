from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        freq = Counter(s)
        for ch, cnt in freq.items():
            if cnt < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(ch))
        return len(s)