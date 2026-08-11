class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(curr, i, j, visited):
            if curr == word:
                return True
            if len(curr) < len(word):
                if i + 1 < len(board) and (i + 1, j) not in visited:
                    visited.add((i + 1, j))
                    if backtrack(curr + board[i + 1][j], i + 1, j, visited):
                        return True
                    visited.remove((i + 1, j))
                if i - 1 >= 0  and (i - 1, j) not in visited:
                    visited.add((i - 1, j))
                    if backtrack(curr + board[i - 1][j], i - 1, j, visited):
                        return True
                    visited.remove((i - 1, j))
                if j + 1 < len(board[0]) and (i, j + 1) not in visited:
                    visited.add((i, j + 1))
                    if backtrack(curr + board[i][j + 1], i, j + 1, visited):
                        return True
                    visited.remove((i, j + 1))
                if j - 1 >= 0 and (i, j - 1) not in visited:
                    visited.add((i, j - 1))
                    if backtrack(curr + board[i][j - 1], i, j - 1, visited):
                        return True
                    visited.remove((i, j - 1))
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    result = backtrack(board[i][j], i, j, visited)
                    if result:
                        return True
        return False