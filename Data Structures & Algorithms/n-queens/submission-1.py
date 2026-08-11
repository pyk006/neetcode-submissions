class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(rows, cols, allSolutions, current, currentRow):
            if currentRow == n:
                final_arr = []
                for i in range(len(current)):
                    joined = "".join(current[i])
                    final_arr.append(joined)
                allSolutions.append(final_arr)
                return
            if currentRow in rows:
                return
            for i in range(n):
                if i in cols:
                    continue
                isDiag = False
                for j in range(len(rows)):
                    if abs(rows[j] - currentRow) == abs(cols[j] - i):
                        isDiag = True
                        break
                
                if isDiag:
                    continue
                
                rows.append(currentRow)
                cols.append(i)
                current[currentRow][i] = "Q"
                backtrack(rows, cols, allSolutions, current, currentRow + 1)
                current[currentRow][i] = "."
                rows.pop()
                cols.pop()

        allSolutions = []
        current = [["."] * n for _ in range(n)]
        print(current)
        backtrack([], [], allSolutions, current, 0)
        return allSolutions