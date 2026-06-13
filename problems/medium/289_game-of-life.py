from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        # Use state encoding to track transitions in-place:
        # 0 -> 0: stays 0
        # 1 -> 1: stays 1
        # 1 -> 0: encode as 2 (was alive, now dead)
        # 0 -> 1: encode as 3 (was dead, now alive)
        
        def count_live_neighbors(i, j):
            count = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        # Count as live if original state was 1 (value is 1 or 2)
                        if board[ni][nj] == 1 or board[ni][nj] == 2:
                            count += 1
            return count
        
        # First pass: determine next state and encode
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                
                if board[i][j] == 1:  # Currently alive
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # Dies
                    # else stays 1 (lives on)
                else:  # Currently dead
                    if live_neighbors == 3:
                        board[i][j] = 3  # Becomes alive
                    # else stays 0 (stays dead)
        
        # Second pass: decode to final state
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1