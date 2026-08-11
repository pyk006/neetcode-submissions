class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, subset, allSubsets):
            if i == len(nums):
                allSubsets.append(subset.copy())
                return
            if i <= len(nums) - 1:
                subset.append(nums[i])
                backtrack(i + 1, subset, allSubsets)
                subset.remove(nums[i])
                backtrack(i + 1, subset, allSubsets)
        allSubsets = []
        backtrack(0, [], allSubsets)
        return allSubsets