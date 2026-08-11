class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid:
            return 0
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] != "1":
                return
            if grid[i][j] == "1":
                grid[i][j] = "visited"
            
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        grid_row, grid_col = len(grid), len(grid[0])
        for i in range(grid_row):
            for j in range(grid_col):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count