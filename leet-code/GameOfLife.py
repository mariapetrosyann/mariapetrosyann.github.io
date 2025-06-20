class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        new_board = [[0 for _ in range(n)] for _ in range(m)]
    
        for i in range(m):
            for j in range(n):
                neighbors = 0
                for row_dir, col_dir in directions:
                    n_row, n_col = i+row_dir, j+col_dir
                    if 0 <= n_row < m and 0 <= n_col < n:
                        neighbors += board[n_row][n_col]
                if board[i][j] == 1:
                    if neighbors in (2,3):
                        new_board[i][j] = 1
                else:
                    if neighbors == 3:
                        new_board[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j]=new_board[i][j]
        
