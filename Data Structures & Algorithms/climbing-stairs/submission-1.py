class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(curr):
            if curr in memo:
                return memo[curr]
            if curr > n:
                return 0
            if curr == n:
                return 1
            memo[curr] = helper(curr + 1) + helper(curr + 2)
            return memo[curr]
        return helper(0)
        