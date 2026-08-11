class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def helper(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1:end]
        
        for i in range(len(s)):
            odd = helper(i, i)
            even = helper(i, i + 1)

            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        
        return res
