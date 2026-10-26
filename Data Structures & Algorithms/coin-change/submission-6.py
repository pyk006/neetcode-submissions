class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(curr):
            if curr in memo:
                return memo[curr]
            if curr == amount:
                return 0
            if curr > amount:
                return float('infinity')
            res = float('infinity')
            for i in range(len(coins)):
                res = min(1 + dp(curr + coins[i]), res)
            memo[curr] = res
            return memo[curr]
        total = dp(0)
        return -1 if total == float('infinity') else total