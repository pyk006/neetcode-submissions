class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(curr, index):
            if (curr, index) in memo:
                return memo[(curr, index)]
            if curr == amount:
                return 1
            if curr > amount or index == len(coins):
                return 0
            
            res = dp(curr, index + 1) + dp(curr + coins[index], index)
            memo[(curr, index)] = res
            return res
        
        return dp(0, 0)
