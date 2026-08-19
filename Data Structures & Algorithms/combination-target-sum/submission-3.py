class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(all_list, current_list, current_sum, start):
            if current_sum > target:
                return
            if current_sum == target:
                all_list.append(current_list.copy())
                return
            
            for i in range(start, len(nums)):
                current_list.append(nums[i])
                backtrack(all_list, current_list, current_sum + nums[i], i)
                current_list.pop()
        
        all_list = []
        backtrack(all_list, [], 0, 0)
        return all_list