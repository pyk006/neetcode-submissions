class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def recurse(curr):
            if curr in memo:
                return memo[curr]
            if curr > n:
                return 0
            if curr == n:
                return 1
            
            memo[curr] = recurse(curr + 1) + recurse(curr + 2)
            return memo[curr]
        
        return recurse(0)