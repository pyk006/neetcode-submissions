class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(len(board[0]))]
        cols = [[] for _ in range(len(board[0]))]
        boxes = [[] for _ in range(len(board[0]))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].append(board[i][j])
                
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].append(board[i][j])
                
                box = (i // 3) * 3 + (j // 3)

                if board[i][j] in boxes[box]:
                    return False
                else:
                    boxes[box].append(board[i][j])
        
        return True
