from __future__ import annotations
import math

class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        # Start from the square root and move downwards
        for w in range(int(math.isqrt(area)), 0, -1):
            if area % w == 0:
                l = area // w
                return [l, w]
        # Should never reach here because area >= 1 divides by 1
        return [area, 1]