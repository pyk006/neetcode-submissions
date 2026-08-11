class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(index, curr):
            if (curr, index) in memo:
                return memo[(curr, index)]
            if curr == amount:
                return 1
            if curr > amount or index == len(coins):
                return 0
            
            res = dp(index, curr + coins[index]) + dp(index + 1, curr)
            memo[(curr, index)] = res
            return memo[(curr, index)]
        
        return dp(0, 0)