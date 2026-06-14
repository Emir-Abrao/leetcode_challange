from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        
        def backtrack(index, path, value, last):
            if index == len(num):
                if value == target:
                    result.append(path)
                return
            
            for i in range(index, len(num)):
                # Extract current number
                curr_str = num[index:i+1]
                
                # Skip numbers with leading zeros (except "0" itself)
                if len(curr_str) > 1 and curr_str[0] == '0':
                    break
                
                curr_num = int(curr_str)
                
                if index == 0:
                    # First number, no operator before it
                    backtrack(i + 1, curr_str, curr_num, curr_num)
                else:
                    # Try addition
                    backtrack(i + 1, path + '+' + curr_str, value + curr_num, curr_num)
                    
                    # Try subtraction
                    backtrack(i + 1, path + '-' + curr_str, value - curr_num, -curr_num)
                    
                    # Try multiplication
                    # Remove the last operand from value, then add last * curr_num
                    backtrack(i + 1, path + '*' + curr_str, value - last + last * curr_num, last * curr_num)
        
        backtrack(0, "", 0, 0)
        return result