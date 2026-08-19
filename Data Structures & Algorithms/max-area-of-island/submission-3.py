class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
                return 0
            if grid[i][j] != 1:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = "visited"
                value = 1
            
            value += dfs(i - 1, j)
            value += dfs(i + 1, j)
            value += dfs(i, j - 1)
            value += dfs(i, j + 1)

            return value
        
        largest = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    value = dfs(i, j)
                    largest = max(value, largest)
        
        return largest