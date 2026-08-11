class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxv = -1
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    maxv = max(maxv, (j - i) - 1)
        
        return maxv

