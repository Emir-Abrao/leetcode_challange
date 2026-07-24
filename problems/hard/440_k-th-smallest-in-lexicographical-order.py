class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix, n):
            """Count numbers with given prefix that are <= n"""
            steps = 0
            first = prefix
            last = prefix
            while first <= n:
                steps += min(n + 1, last + 1) - first
                first *= 10
                last = last * 10 + 9
            return steps
        
        current = 1
        k -= 1  # We start at 1, so we need k-1 more steps
        
        while k > 0:
            steps = count_steps(current, n)
            if steps <= k:
                # Skip this subtree, move to next sibling
                current += 1
                k -= steps
            else:
                # Go deeper into this subtree
                current *= 10
                k -= 1
        
        return current