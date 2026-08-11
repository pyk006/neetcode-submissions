class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def recurse(curr, coins_used):
            if curr in memo:
                return memo[curr]
            if curr == amount:
                return 0
            if curr > amount:
                return float('inf')
            min_coins = float('inf')
            for i in range(len(coins)):
                res = recurse(curr + coins[i], coins_used + 1)
                min_coins = min(1 + res, min_coins)
            memo[curr] = min_coins
            return memo[curr]
        res = recurse(0,0)
        return res if res != float('inf') else -1