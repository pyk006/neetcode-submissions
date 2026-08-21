class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = []
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or i > 0 and nums[i] != nums[i - 1]:
                start = i + 1
                end = len(nums) - 1
                complement = 0 - nums[i]

                while start < end:
                    if nums[start] + nums[end] == complement:
                        triples.append([nums[start], nums[end], nums[i]])

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
        
        return triples