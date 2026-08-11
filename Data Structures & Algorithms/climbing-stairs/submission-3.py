class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(curr):
            if curr in memo:
                return memo[curr]
            if curr > n:
                return 0
            if curr == n:
                return 1
            
            res = dp(curr + 1) + dp(curr + 2)

            memo[curr] = res

            return memo[curr]
        
        return dp(0)