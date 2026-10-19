class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        oceans_reached = [[[False, False] for _ in range(len(heights[0]))] for _ in range(len(heights))]
        def dfs(i, j, index):
            if i < 0 or j < 0 or i > len(heights) - 1 or j > len(heights[0]) - 1:
                return
            if oceans_reached[i][j][index]:
                return
            oceans_reached[i][j][index] = True
            if i - 1 >= 0 and heights[i][j] <= heights[i - 1][j]:
                dfs(i - 1, j, index)
            if j - 1 >= 0 and heights[i][j] <= heights[i][j - 1]:
                dfs(i, j - 1, index)
            if i + 1 <= len(heights) - 1 and heights[i][j] <= heights[i + 1][j]:
                dfs(i + 1, j, index)
            if j + 1 <= len(heights[0]) - 1 and heights[i][j] <= heights[i][j + 1]:
                dfs(i, j + 1, index)
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    dfs(i, j, 0)
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    dfs(i, j, 1)
        
        all_sol = []
        for i in range(len(oceans_reached)):
            for j in range(len(oceans_reached[0])):
                if oceans_reached[i][j] == [True, True]:
                    all_sol.append([i, j])
        
        return all_sol