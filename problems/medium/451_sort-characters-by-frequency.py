class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        
        freq = Counter(s)
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        result = []
        for char, count in sorted_chars:
            result.append(char * count)
        
        return ''.join(result)