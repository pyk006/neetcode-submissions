class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(curr):
            if curr in memo:
                return memo[curr]
            if curr == len(nums) - 1:
                return nums[curr]
            if curr > len(nums) - 1:
                return 0
            
            memo[curr] = nums[curr] + max(dp(curr + 2), dp(curr + 3))
            return memo[curr]
        
        return max(dp(0), dp(1))