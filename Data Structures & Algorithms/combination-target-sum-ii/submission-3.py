class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(current_sum, current_arr, allCombos, start):
            if current_sum > target:
                return
            if current_sum == target:
                allCombos.append(current_arr.copy())
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current_arr.append(candidates[i])
                backtrack(current_sum + candidates[i], current_arr, allCombos, i + 1)
                current_arr.pop()
        
        allCombos = []
        backtrack(0, [], allCombos, 0)
        return allCombos