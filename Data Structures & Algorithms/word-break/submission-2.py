class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True

            for word in wordDict:
                word_l = len(word)
                if i + word_l <= len(s) and s[i: i + word_l] == word:
                    if dp(i + word_l):
                        memo[i] = True
                        return True
                    
            memo[i] = False
            return False
        
        return dp(0)