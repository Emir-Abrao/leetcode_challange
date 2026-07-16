from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            
            mid = len(arr) // 2
            left, count_left = merge_sort(arr[:mid])
            right, count_right = merge_sort(arr[mid:])
            
            count = count_left + count_right
            
            j = k = 0
            for left_val in left:
                while j < len(right) and right[j] - left_val < lower:
                    j += 1
                while k < len(right) and right[k] - left_val <= upper:
                    k += 1
                count += k - j
            
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            return merged, count
        
        _, result = merge_sort(prefix_sums)
        return result