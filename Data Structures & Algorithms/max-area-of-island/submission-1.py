class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_count = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
                return 0
            if grid[i][j] != 1:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = "visited"
                current_count = 1

            current_count += dfs(i - 1, j)
            current_count += dfs(i + 1, j)
            current_count += dfs(i, j - 1)
            current_count += dfs(i, j + 1)
            return current_count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_count = max(max_count, dfs(i, j))
        
        return max_count