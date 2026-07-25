from typing import List
import random
import bisect

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        total = 0
        
        for rect in rects:
            a, b, x, y = rect
            # Number of integer points in this rectangle (inclusive)
            num_points = (x - a + 1) * (y - b + 1)
            total += num_points
            self.weights.append(total)
    
    def pick(self) -> List[int]:
        # Pick a random number between 1 and total number of points
        target = random.randint(1, self.weights[-1])
        
        # Binary search to find which rectangle this point belongs to
        idx = bisect.bisect_left(self.weights, target)
        if idx < len(self.weights) and self.weights[idx] < target:
            idx += 1
        
        # Get the rectangle
        a, b, x, y = self.rects[idx]
        
        # Find the offset within this rectangle
        prev_weight = self.weights[idx - 1] if idx > 0 else 0
        offset = target - prev_weight - 1
        
        # Calculate width and height
        width = x - a + 1
        
        # Convert offset to coordinates
        dx = offset % width
        dy = offset // width
        
        return [a + dx, b + dy]