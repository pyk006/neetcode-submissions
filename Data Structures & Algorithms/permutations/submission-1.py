class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(visited, current, allPerms):
            if len(current) == len(nums):
                allPerms.append(current.copy())
                return
            for i in range(len(nums)):
                if not visited[i]:
                    current.append(nums[i])
                    visited[i] = True
                    backtrack(visited, current, allPerms)
                    current.pop()
                    visited[i] = False
        
        allPerms = []
        visited = [False for _ in range(len(nums))]
        backtrack(visited, [], allPerms)
        return allPerms