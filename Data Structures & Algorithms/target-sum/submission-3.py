class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(curr, index):
            if (curr, index) in memo:
                return memo[(curr, index)]
            if index == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0
            
            res = dp(curr + nums[index], index + 1) + dp(curr - nums[index], index + 1)
            memo[(curr, index)] = res
            return res
        
        return dp(0, 0)
            