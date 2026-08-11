class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    if board[i][j] == "O":
                        q = deque()
                        q.append((i, j))
                        board[i][j] = "good"
                        while q:
                            current_i, current_j = q.popleft()
                            neighs = []
                            if current_i + 1 < len(board):
                                neighs.append((current_i + 1, current_j))
                            if current_i - 1 >= 0:
                                neighs.append((current_i - 1, current_j))
                            if current_j + 1 < len(board[0]):
                                neighs.append((current_i, current_j + 1))
                            if current_j - 1 >= 0:
                                neighs.append((current_i, current_j - 1))
                            for neighbor in neighs:
                                if board[neighbor[0]][neighbor[1]] == "O":
                                    board[neighbor[0]][neighbor[1]] = "good"
                                    q.append((neighbor[0], neighbor[1]))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "good":
                    board[i][j] = "O"
                    continue
                if board[i][j] == "O":
                    board[i][j] = "X"

        
