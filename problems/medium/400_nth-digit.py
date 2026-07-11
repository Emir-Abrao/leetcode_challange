class Solution:
    def findNthDigit(self, n: int) -> int:
        # Find which group of numbers the nth digit belongs to
        # 1-digit numbers: 1-9 (9 numbers, 9 digits)
        # 2-digit numbers: 10-99 (90 numbers, 180 digits)
        # 3-digit numbers: 100-999 (900 numbers, 2700 digits)
        # etc.
        
        digit_length = 1
        count = 9
        start = 1
        
        # Find the range where the nth digit falls
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10
        
        # Find the actual number that contains the nth digit
        # n is now relative to the current range
        num = start + (n - 1) // digit_length
        
        # Find which digit within that number
        digit_index = (n - 1) % digit_length
        
        return int(str(num)[digit_index])