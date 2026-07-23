class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        
        # seen[i] = (count_s1, count_s2) when we finish processing and index_s2 is at position i
        seen = {}
        count_s1 = 0  # number of s1's we've gone through
        count_s2 = 0  # number of s2's we've completed
        index_s2 = 0  # current position in s2 we're trying to match
        
        while count_s1 < n1:
            # Check if we've seen this s2 starting position before (at the start of processing s1)
            if count_s1 > 0 and index_s2 in seen:
                # We found a cycle
                prev_count_s1, prev_count_s2 = seen[index_s2]
                
                # Length of the cycle in terms of s1's and s2's
                cycle_len_s1 = count_s1 - prev_count_s1
                cycle_len_s2 = count_s2 - prev_count_s2
                
                # How many complete cycles can we fit in the remaining s1's?
                remaining_s1 = n1 - count_s1
                complete_cycles = remaining_s1 // cycle_len_s1
                
                # Fast forward
                count_s1 += complete_cycles * cycle_len_s1
                count_s2 += complete_cycles * cycle_len_s2
                
                # Clear seen to continue with remaining iterations
                seen.clear()
                
                if count_s1 >= n1:
                    break
            
            # Record current state before processing
            if index_s2 not in seen:
                seen[index_s2] = (count_s1, count_s2)
            
            # Try to match one complete s1
            for char in s1:
                if char == s2[index_s2]:
                    index_s2 += 1
                    if index_s2 == len(s2):
                        # Completed one s2
                        count_s2 += 1
                        index_s2 = 0
            
            count_s1 += 1
        
        # How many str2's can we form?
        # We have count_s2 s2's, and each str2 needs n2 s2's
        return count_s2 // n2