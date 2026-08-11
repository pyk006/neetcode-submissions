class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()
        for i in range(len(nums)):
            if nums[i] not in dupes:
                dupes.add(nums[i])
            else:
                return True
        return False