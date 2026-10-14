class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        best = []
        current_max = []
        for right in range(len(nums)):
            while current_max and nums[current_max[-1]] <= nums[right]:
                current_max.pop()
            current_max.append(right)
            
            if (right - left + 1) == k:
                if current_max[0] < left:
                    current_max.pop(0)
                best.append(nums[current_max[0]])
                left += 1
        return best