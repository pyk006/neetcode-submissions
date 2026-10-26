class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        memo = {}
        def dp(index, curr):
            if (index, curr) in memo:
                return memo[(index, curr)]
            if index > len(nums) - 1:
                return False
            if curr == target:
                return True
            
            memo[(index, curr)] = dp(index + 1, curr + nums[index]) or dp(index + 1, curr)
            return memo[(index, curr)]
        
        return dp(0, 0)
                