class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp(i, nums, memo):
            if i in memo:
                return memo[i]
            if i > len(nums) - 1:
                return 0
            if i == len(nums) - 1:
                return nums[i]
            
            memo[i] = max(nums[i] + dp(i + 2, nums, memo), dp(i + 1, nums, memo))
            return memo[i]

        num_skip_first = nums[1:]
        num_skip_last = nums[:len(nums) - 1]
        memo = {}
        memo_2 = {}
        return max(dp(0, num_skip_first, memo), dp(0, num_skip_last, memo_2))