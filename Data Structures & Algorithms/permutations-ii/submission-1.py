class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(curr, allSols, visited):
            if len(curr) == len(nums):
                allSols.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                if visited[i]:
                    continue
                curr.append(nums[i])
                visited[i] = True
                backtrack(curr, allSols, visited)
                visited[i] = False
                curr.pop()
        
        allSols = []
        visited = [False for _ in range(len(nums))]
        backtrack([], allSols, visited)
        return allSols