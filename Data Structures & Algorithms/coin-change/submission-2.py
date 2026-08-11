class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(curr):
            if curr in memo:
                return memo[curr]
            if curr > amount:
                return float('inf')
            if curr == amount:
                return 0
            
            min_coins = float('inf')

            for coin in coins:
                res = dp(curr + coin)
                min_coins = min(min_coins, res + 1)
            memo[curr] = min_coins
            return memo[curr]
        min_val = dp(0)
        return min_val if min_val != float('inf') else -1
