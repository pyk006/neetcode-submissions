class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3
        dicti = {}
        arr = []
        for i in range(len(nums)):
            dicti[nums[i]] = dicti.get(nums[i], 0) + 1
        
        for key, value in dicti.items():
            if value > target:
                arr.append(key)
        
        return arr