class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        best_l = float('infinity')
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                best_l = min(right - left + 1, best_l)
                curr_sum -= nums[left]
                left += 1
        return 0 if best_l == float('infinity') else best_l