class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        
        if target == 0:
            return True
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return target % gcd(x, y) == 0