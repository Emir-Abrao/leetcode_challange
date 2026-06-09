from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False
        
        m, n = len(board), len(board[0])
        
        def dfs(i, j, k):
            if k == len(word):
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'
            
            found = (dfs(i + 1, j, k + 1) or 
                    dfs(i - 1, j, k + 1) or 
                    dfs(i, j + 1, k + 1) or 
                    dfs(i, j - 1, k + 1))
            
            board[i][j] = temp
            
            return found
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False