class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                val = board[row][col]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
    
        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
    
        for sub_box_row in range(0, 9, 3):
            for sub_box_col in range(0, 9, 3):
                seen = set()
                for row in range(sub_box_row, sub_box_row+3):
                    for col in range(sub_box_col, sub_box_col+3):
                        val = board[row][col]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)
        return True
