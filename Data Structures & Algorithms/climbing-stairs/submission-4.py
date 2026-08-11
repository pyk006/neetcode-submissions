class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(count):
            if count in memo:
                return memo[count]
            if count > n:
                return 0
            if count == n:
                return 1
            
            res = dp(count + 1) + dp(count + 2)
            memo[count] = res
            return memo[count]
        
        return dp(0)