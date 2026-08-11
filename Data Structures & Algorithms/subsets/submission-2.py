class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current, allList):
            allList.append(current.copy())
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current, allList)
                current.pop()
        
        allList = []
        backtrack(0, [], allList)
        return allList
                