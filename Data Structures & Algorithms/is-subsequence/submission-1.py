class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        count = 0
        for i in range(len(t)):
            if j <= len(s) - 1 and t[i] == s[j]:
                count += 1
                j += 1
        
        return count == len(s)