class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_con = 0

        while start < end:
            max_con = max(max_con, (end - start) * min(heights[start], heights[end]))

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return max_con