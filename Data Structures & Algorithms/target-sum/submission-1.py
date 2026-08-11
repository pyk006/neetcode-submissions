class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(index, curr):
            if (index, curr) in memo:
                return memo[(index,curr)]
            if index == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0
            res = dp(index + 1, curr + nums[index]) + dp(index + 1, curr - nums[index])
            memo[(index, curr)] = res
            return memo[(index, curr)]
        
        return dp(0,0)