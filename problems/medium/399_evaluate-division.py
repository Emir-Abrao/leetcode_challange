from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value
        
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            
            if start == end:
                return 1.0
            
            queue = deque([(start, 1.0)])
            visited = {start}
            
            while queue:
                node, product = queue.popleft()
                
                if node == end:
                    return product
                
                for neighbor, value in graph[node].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, product * value))
            
            return -1.0
        
        return [bfs(start, end) for start, end in queries]