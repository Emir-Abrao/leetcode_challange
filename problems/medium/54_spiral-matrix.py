class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        if not matrix:
            return result
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # traverse right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # traverse down
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                # traverse left
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            if left <= right:
                # traverse up
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result