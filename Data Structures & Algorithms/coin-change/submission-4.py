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
            
            min_amount = float('infinity')
            for coin in coins:
                res = dp(curr + coin)
                min_amount = min(res + 1, min_amount)
            memo[curr] = min_amount
            return memo[curr]
        
        total = dp(0)
        return -1 if total == float('infinity') else total