class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1: end]
        best = ""
        for i in range(len(s)):
            odd = helper(i, i)
            even = helper(i, i + 1)

            if len(odd) > len(best):
                best = odd
            if len(even) > len(best):
                best = even
        
        return best