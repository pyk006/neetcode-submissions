class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, i, allSols):
            if len(curr) == k:
                allSols.append(curr.copy())
            
            if i > n:
                return
            for j in range(i, n + 1):
                curr.append(j)
                backtrack(curr, j + 1, allSols)
                curr.pop()
        
        allSols = []
        backtrack([], 1, allSols)
        return allSols