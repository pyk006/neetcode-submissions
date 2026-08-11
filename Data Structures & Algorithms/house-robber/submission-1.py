class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(nums) or i < 0:
                return 0
            
            money_robbed = nums[i] + dp(i + 2)
            skip_first = dp(i + 1)
            memo[i] = max(money_robbed, skip_first)
            return memo[i]
        
        return dp(0)
            