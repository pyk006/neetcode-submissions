class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
                return 0
            if grid[i][j] != 1:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = -1
                count = 1
                count += dfs(i - 1, j)
                count += dfs(i + 1, j)
                count += dfs(i, j - 1)
                count += dfs(i, j + 1)
                return count
        max_len = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_len = max(max_len, dfs(i, j))
        
        return max_len