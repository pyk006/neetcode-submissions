class Solution:
    def canJump(self, nums: List[int]) -> bool:
        best = 0
        for i in range(len(nums)):
            if i > best:
                return False
            best = max(best, nums[i] + i)
            if best >= len(nums) - 1:
                return True