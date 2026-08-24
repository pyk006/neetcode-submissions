class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        products = 1
        for i in range(len(nums)):
            arr.append(products)
            products *= nums[i]
        
        products = 1
        for i in reversed(range(len(nums))):
            arr[i] *= products
            products *= nums[i]
        
        return arr