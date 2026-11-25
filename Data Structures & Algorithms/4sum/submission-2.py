class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        allSols = []
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                for j in range(i + 1, len(nums)):
                    if j == i + 1 or (j > i + 1 and nums[j] != nums[j - 1]):
                        complement = target - nums[i] - nums[j]
                        start = j + 1
                        end = len(nums) - 1
                        while start < end:
                            if nums[start] + nums[end] == complement:
                                allSols.append([nums[i], nums[j], nums[start], nums[end]])
                                while start < end and nums[start] == nums[start + 1]:
                                    start += 1
                                while start < end and nums[end] == nums[end - 1]:
                                    end -= 1
                                start += 1
                                end -= 1
                            elif nums[start] + nums[end] > complement:
                                end -= 1
                            else:
                                start += 1
        
        return allSols