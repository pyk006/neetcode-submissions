class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(visited_rows, visited_cols, curr, curr_row, all_sol):
            if curr_row == n:
                final_arr = []
                for i in range(len(curr)):
                    final_arr.append("".join(curr[i]))
                print(final_arr)
                all_sol.append(final_arr)
            if curr_row in visited_rows:
                return
            for i in range(n):
                if i in visited_cols:
                    continue
                isDiag = False
                for j in range(len(visited_cols)):
                    if abs(j - curr_row) == abs(i - visited_cols[j]):
                        isDiag = True
                        break
                
                if isDiag:
                    continue
                
                visited_rows.append(curr_row)
                visited_cols.append(i)
                curr[curr_row][i] = "Q"
                backtrack(visited_rows, visited_cols, curr, curr_row + 1, all_sol)
                curr[curr_row][i] = "."
                visited_cols.pop()
                visited_rows.pop()
        
        all_sol = []
        curr = [["."] * n for _ in range(n)]
        backtrack([], [], curr, 0, all_sol)
        return all_sol
                