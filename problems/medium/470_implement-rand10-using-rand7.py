# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # Generate uniform random in [1, 49]
            num = (rand7() - 1) * 7 + rand7()
            
            # Use [1, 40] -> map to [1, 10]
            if num <= 40:
                return (num - 1) % 10 + 1
            
            # Reject [41, 49], we have 9 numbers
            # Generate uniform random in [1, 63] using rejected sample
            num = (num - 40 - 1) * 7 + rand7()  # [0, 8] * 7 + [1, 7] = [1, 63]
            
            # Use [1, 60] -> map to [1, 10]
            if num <= 60:
                return (num - 1) % 10 + 1
            
            # Reject [61, 63], we have 3 numbers
            # Generate uniform random in [1, 21] using rejected sample
            num = (num - 60 - 1) * 7 + rand7()  # [0, 2] * 7 + [1, 7] = [1, 21]
            
            # Use [1, 20] -> map to [1, 10]
            if num <= 20:
                return (num - 1) % 10 + 1
            
            # Reject [21, 21], only 1 number left, not enough for another optimization
            # Restart the whole process