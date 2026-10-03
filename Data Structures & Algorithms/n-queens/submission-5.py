class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(currRow, all_sol, currentSol, rows, cols):
            if currRow == n:
                sol = []
                for i in range(len(currentSol)):
                    sol.append("".join(currentSol[i]))
                
                all_sol.append(sol)
                return
            
            if currRow in rows:
                return
            
            for i in range(n):
                if i in cols:
                    continue
                isDiag = False
                for j in range(len(cols)):
                    if abs(i - cols[j]) == abs(currRow - rows[j]):
                        isDiag = True
                        break
                
                if isDiag:
                    continue
                
                rows.append(currRow)
                cols.append(i)
                currentSol[currRow][i] = "Q"
                backtrack(currRow + 1, all_sol, currentSol, rows, cols)
                currentSol[currRow][i] = "."
                rows.pop()
                cols.pop()
        
        all_sol = []
        currentSol = [["." for _  in range(n)] for _ in range(n)]
        backtrack(0, all_sol, currentSol, [], [])
        return all_sol
