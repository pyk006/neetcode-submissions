class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(permutation, permutations, visited):
            if len(permutation) == len(nums):
                permutations.append(permutation.copy())
                return
            for i in range(len(nums)):
                if not visited[i]:
                    permutation.append(nums[i])
                    visited[i] = True
                    backtrack(permutation, permutations, visited)
                    permutation.remove(nums[i])
                    visited[i] = False
        
        permutations = []
        visited = [False] * len(nums)
        backtrack([], permutations, visited)
        return permutations