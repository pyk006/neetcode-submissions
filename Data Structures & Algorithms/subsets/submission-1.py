class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current, allSubsets):
            allSubsets.append(current.copy())

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current, allSubsets)
                current.pop()
        
        allSubsets = []
        backtrack(0, [], allSubsets)
        return allSubsets