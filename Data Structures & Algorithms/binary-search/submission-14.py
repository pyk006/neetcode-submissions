class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if start <= end and nums[mid] > target:
                end -= 1
            elif start <= end and nums[mid] < target:
                start += 1
        
        return -1