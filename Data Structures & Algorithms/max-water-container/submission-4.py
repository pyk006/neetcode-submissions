class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        best = 0
        while start < end:
            val = min(heights[start], heights[end]) * (end - start)
            best = max(best, val)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return best