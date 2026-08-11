class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i >= len(cost):
                return 0
            if i == len(cost) - 1:
                return cost[i]
            
            res = cost[i] + min(dp(i + 1), dp(i + 2))
            memo[i] = res
            return memo[i]
        
        return min(dp(0), dp(1))