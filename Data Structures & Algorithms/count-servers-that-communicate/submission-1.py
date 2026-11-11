class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count = 0
        rows = [0 for _ in range(len(grid))]
        cols = [0 for _ in range(len(grid[0]))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    count += 1
        
        return count