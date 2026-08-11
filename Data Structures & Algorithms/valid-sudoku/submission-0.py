class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_vals = [[] for _ in range(len(board[0]))]
        row_vals = [[] for _ in range(len(board))]
        box_vals = [[] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_vals[i]:
                    return False
                else:
                    row_vals[i].append(board[i][j])
                
                if board[i][j] in col_vals[j]:
                    return False
                else:
                    col_vals[j].append(board[i][j])
                
                current_box_index = (i // 3) * 3 + (j // 3)
                if board[i][j] in box_vals[current_box_index]:
                    return False
                else:
                    box_vals[current_box_index].append(board[i][j])

        return True