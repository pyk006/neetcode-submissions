class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        curr = 1;
        for i in range(len(nums)):
            output.append(curr)
            curr *= nums[i]
        curr_right = 1;
        start = len(nums) - 1
        while start >= 0:
            output[start] *= curr_right
            curr_right *= nums[start]
            start-= 1;
        return output
