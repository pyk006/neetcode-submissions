class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, allList, curr, total):
            if total > target:
                return
            if total == target:
                allList.append(curr.copy())
            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i, allList, curr, total + nums[i])
                curr.remove(nums[i])
        
        allList = []
        backtrack(0, allList, [], 0)
        return allList

                