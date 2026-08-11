class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                return nums[i]
            
            res = nums[i] + max(dp(i + 2), dp(i + 3))
            memo[i] = res
            return memo[i]
        return max(dp(0), dp(1))