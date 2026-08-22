class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(visited_rows, visited_cols, currentRow, curr_arr, allList):
            if currentRow == n:
                res = []
                for i in range(len(curr_arr)):
                    res.append("".join(curr_arr[i]))
                allList.append(res)
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
                curr_arr[currentRow][i] = "Q"
                backtrack(visited_rows, visited_cols, currentRow + 1, curr_arr, allList)
                visited_rows.pop()
                visited_cols.pop()
                curr_arr[currentRow][i] = "."
            
        allList = []
        curr_arr = [["." for _ in range(n)] for _ in range(n)]
        backtrack([], [], 0, curr_arr, allList)
        return len(allList)