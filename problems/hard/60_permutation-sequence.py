class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1]
        for i in range(1, n):
            factorials.append(factorials[-1] * i)
        
        numbers = list(range(1, n + 1))
        result = []
        
        k -= 1
        
        for i in range(n - 1, -1, -1):
            if i > 0:
                index = k // factorials[i]
                k %= factorials[i]
            else:
                index = 0
            
            result.append(str(numbers[index]))
            numbers.pop(index)
        
        return ''.join(result)