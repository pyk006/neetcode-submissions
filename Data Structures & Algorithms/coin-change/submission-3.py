class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(total):
            if total in memo:
                return memo[total]
            if total == amount:
                return 0
            if total > amount:
                return float('inf')
            min_coins = float('inf')
            for coin in coins:
                res = dp(total + coin)
                min_coins = min(res + 1, min_coins)
            memo[total] = min_coins
            return memo[total]
        min_val = dp(0)
        return min_val if min_val != float('inf') else -1