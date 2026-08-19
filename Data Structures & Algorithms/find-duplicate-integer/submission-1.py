class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupes = set()

        for num in nums:
            if num not in dupes:
                dupes.add(num)
            else:
                return num
        return -1