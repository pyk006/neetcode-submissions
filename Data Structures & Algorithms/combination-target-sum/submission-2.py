class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(current, current_list, all_list, index):
            if current > target:
                return
            if current == target:
                all_list.append(current_list.copy())
                return
            
            for i in range(index, len(nums)):
                current_list.append(nums[i])
                backtrack(current + nums[i], current_list, all_list, i)
                current_list.pop()
        
        all_list = []
        backtrack(0, [], all_list, 0)
        return all_list