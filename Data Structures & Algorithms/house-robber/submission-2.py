class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(index):
            if index in memo:
                return memo[index]
            if index >= len(nums) or index < 0:
                return 0


            res = nums[index] + dp(index + 2)
            skip = dp(index + 1)
            memo[index] = max(res, skip)
            return memo[index]
        
        return dp(0)