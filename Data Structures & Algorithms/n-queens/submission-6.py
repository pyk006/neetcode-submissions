class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(currRow, rows, cols, all_sols, curr_sol):
            if currRow == n:
                sol = []
                for i in range(len(curr_sol)):
                    sol.append("".join(curr_sol[i]))
                
                all_sols.append(sol)
            
            if currRow in rows:
                return
            
            for i in range(n):
                if i in cols:
                    continue
                isDiag = False
                for j in range(len(cols)):
                    if abs(rows[j] - currRow) == abs(cols[j] - i):
                        isDiag = True
                        break
                
                if isDiag:
                    continue
                
                rows.append(currRow)
                cols.append(i)
                curr_sol[currRow][i] = "Q"
                backtrack(currRow + 1, rows, cols, all_sols, curr_sol)
                rows.pop()
                cols.pop()
                curr_sol[currRow][i] = "."
            
        all_sols = []
        curr_sol = [["." for _ in range(n)] for _ in range(n)]
        print(curr_sol)
        backtrack(0, [], [], all_sols, curr_sol)
        return all_sols