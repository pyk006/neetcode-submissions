class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(current_sum, current, allList, start):
            if current_sum > target:
                return
            if current_sum == target:
                allList.append(current.copy())
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(current_sum + nums[i], current, allList, i)
                current.pop()
        
        allList = []
        backtrack(0, [], allList, 0)
        return allList