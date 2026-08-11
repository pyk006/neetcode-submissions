class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()

        for i in range(len(nums)):
            if nums[i] not in unique_nums:
                unique_nums.add(nums[i])
            else:
                return True;
        return False;