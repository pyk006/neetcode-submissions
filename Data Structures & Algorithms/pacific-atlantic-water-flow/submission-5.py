class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        oceans = [[[False, False] for _ in range(len(heights[0]))] for _ in range(len(heights))]
        def dfs(i, j, oceans, index):
            if i < 0 or j < 0 or i > len(heights) - 1 or j > len(heights[0]) - 1:
                return
            if oceans[i][j][index]:
                return
            oceans[i][j][index] = True

            if i - 1 >= 0 and heights[i][j] <= heights[i - 1][j]:
                dfs(i - 1, j, oceans, index)
            if i + 1 < len(heights) and heights[i][j] <= heights[i + 1][j]:
                dfs(i + 1, j, oceans, index)
            if j - 1 >= 0 and heights[i][j] <= heights[i][j - 1]:
                dfs(i, j - 1, oceans, index)
            if j + 1 < len(heights[0]) and heights[i][j] <= heights[i][j + 1]:
                dfs(i, j + 1, oceans, index)
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    dfs(i, j, oceans, 0)
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    dfs(i, j, oceans, 1)
        in_both = []
        for i in range(len(oceans)):
            for j in range(len(oceans[0])):
                if oceans[i][j] == [True, True]:
                    in_both.append([i, j])
        
        return in_both