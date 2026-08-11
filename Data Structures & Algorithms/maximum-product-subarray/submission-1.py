class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = []
        min_prod = []
        max_prod.append(nums[0])
        min_prod.append(nums[0])
        max_actual = nums[0]
        for i in range(1, len(nums)):
            max_prod.append(max(nums[i], max_prod[i - 1] * nums[i], min_prod[i - 1] * nums[i]))
            min_prod.append(min(nums[i], max_prod[i - 1] * nums[i], min_prod[i - 1] * nums[i]))
            max_actual = max(max_prod[i], max_actual)
        
        return max_actual