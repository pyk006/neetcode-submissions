class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_reached = [[False] * len(heights[0]) for _ in range(len(heights))]
        atlantic_reached = [[False] * len(heights[0]) for _ in range(len(heights))]
        def dfs(i, j, reached_l, prev):
            if i < 0 or j < 0 or i > len(heights) - 1 or j > len(heights[0]) - 1:
                return
            if reached_l[i][j]:
                return
            if heights[i][j] < prev:
                return
            if heights[i][j] >= prev:
                reached_l[i][j] = True
            
            dfs(i - 1, j, reached_l, heights[i][j])
            dfs(i + 1, j, reached_l, heights[i][j])
            dfs(i, j - 1, reached_l, heights[i][j])
            dfs(i, j + 1, reached_l, heights[i][j])
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    dfs(i, j, pacific_reached, float('-inf'))
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    dfs(i, j, atlantic_reached, float('-inf'))
        res = []
        for i in range(len(pacific_reached)):
            for j in range(len(pacific_reached[0])):
                if pacific_reached[i][j] and atlantic_reached[i][j]:
                    res.append([i, j])
        
        return res
