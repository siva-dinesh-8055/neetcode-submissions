class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            row_set = set() 
            for col in range(9):
                if board[row][col] in row_set:
                    return False 

                elif board[row][col] != '.':
                    row_set.add(board[row][col]) 

        for col in range(9):
            col_set = set() 
            for row in range(9):
                if board[row][col] in col_set:
                    return False 

                elif board[row][col] != '.':
                    col_set.add(board[row][col]) 

        box_start_address = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

        for row_start, col_start in box_start_address:
            box_set = set() 
            for row in range(row_start, row_start + 3):
                for col in range(col_start, col_start + 3):
                    if board[row][col] in box_set:
                        return False 

                    elif board[row][col] != '.':
                        box_set.add(board[row][col]) 

        return True 