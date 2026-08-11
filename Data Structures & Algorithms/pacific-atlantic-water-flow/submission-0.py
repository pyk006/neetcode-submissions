class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        oceans_reached = [[[False, False] for _ in range(len(heights[0]))] for _ in range(len(heights))]
        all_good = []
        def dfs(i, j, oceans_reached, index):
            if i < 0 or j < 0 or i > len(heights) - 1 or j > len(heights[0]) - 1:
                return
            if oceans_reached[i][j][index]:
                return
            oceans_reached[i][j][index] = True
            if i + 1 <= len(heights) - 1:
                if heights[i + 1][j] >= heights[i][j]:
                    dfs(i + 1, j, oceans_reached, index)
            if i - 1 >= 0:
                if heights[i - 1][j] >= heights[i][j]:
                    dfs(i - 1, j, oceans_reached, index) 
            if j + 1 <= len(heights[0]) - 1:
                if heights[i][j + 1] >= heights[i][j]:
                    dfs(i, j + 1, oceans_reached, index)
            if j - 1 >= 0:
                if heights[i][j - 1] >= heights[i][j]:
                    dfs(i, j - 1, oceans_reached, index)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    dfs(i, j, oceans_reached, 0)  
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    dfs(i, j, oceans_reached, 1) 
        
        for i in range(len(oceans_reached)):
            for j in range(len(oceans_reached[0])):
                if oceans_reached[i][j] == [True,True]:
                    all_good.append([i, j])
        
        return all_good