class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(allList, current, current_sum, start):
            if current_sum > target:
                return
            if current_sum == target:
                allList.append(current.copy())
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                backtrack(allList, current, current_sum + candidates[i], i + 1)
                current.pop()
        
        allList = []
        backtrack(allList, [], 0, 0)
        return allList