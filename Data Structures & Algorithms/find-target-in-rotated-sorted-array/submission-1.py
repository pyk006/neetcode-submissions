class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[end]:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                    continue
                else:
                    end = mid
            if nums[mid] > nums[end]:
                if target <= nums[mid] and target >= nums[start]:
                    end = mid
                    continue
                else:
                    start = mid + 1
        return start if nums[start] == target else -1