class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(current, allSolutions, currentRow, visited_rows, visited_cols):
            if currentRow == n:
                solution = []
                for i in range(len(current)):
                    solution.append("".join(current[i]))
                allSolutions.append(solution)
                return
            if currentRow in visited_rows:
                return
            for i in range(n):
                isDiagonal = False
                if i in visited_cols:
                    continue
                for j in range(len(visited_rows)):
                    if abs(currentRow - visited_rows[j]) == abs(i - visited_cols[j]):
                        isDiagonal = True
                        break
                if isDiagonal:
                    continue
                current[currentRow][i] = "Q"
                visited_rows.append(currentRow)
                visited_cols.append(i)
                backtrack(current, allSolutions, currentRow + 1, visited_rows, visited_cols)
                visited_rows.pop()
                visited_cols.pop()
                current[currentRow][i] = "."
        
        allSolutions = []
        current = [["."] * n for _ in range(n)]
        visited_rows = []
        visited_cols = []
        backtrack(current, allSolutions, 0, visited_rows, visited_cols)
        return allSolutions