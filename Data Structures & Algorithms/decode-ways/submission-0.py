class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            memo[i] = 0
            if i + 1 <= len(s):
                memo[i] += dp(i + 1)
            if i + 2 <= len(s) and int(s[i:i+2]) <= 26:
                memo[i] += dp(i + 2)
        
            return memo[i]

        return dp(0)