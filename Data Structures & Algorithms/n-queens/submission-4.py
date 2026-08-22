class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(visited_rows, visited_cols, current_arr, allList, currentRow):
            if currentRow == n:
                str_sol = []
                for i in range(len(current_arr)):
                    str_sol.append("".join(current_arr[i]))
                allList.append(str_sol)
                return
            if currentRow in visited_rows:
                return
            for i in range(n):
                if i in visited_cols:
                    continue
                isDiag = False
                for j in range(len(visited_cols)):
                    if abs(j - currentRow) == abs(i - visited_cols[j]):
                        isDiag = True
                        break
                if isDiag:
                    continue
                visited_rows.append(currentRow)
                visited_cols.append(i)
                current_arr[currentRow][i] = "Q"
                backtrack(visited_rows, visited_cols, current_arr, allList, currentRow + 1)
                current_arr[currentRow][i] = "."
                visited_rows.pop()
                visited_cols.pop()
        
        allList = []
        current_arr = [["." for _ in range(n)] for _ in range(n)]
        backtrack([], [], current_arr, allList, 0)
        return allList
