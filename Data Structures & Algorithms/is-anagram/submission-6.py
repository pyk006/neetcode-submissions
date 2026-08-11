class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        if len(s) != len(t):
            return False;
        for i in range(len(s)):
            if s[i] in map_s:
                map_s[s[i]] = map_s[s[i]] + 1
            else:
                map_s[s[i]] = 1
        
        for j in range(len(t)):
            if t[j] in map_t:
                map_t[t[j]] = map_t[t[j]] + 1
            else:
                map_t[t[j]] = 1

        for char in map_s:
            if char not in map_s or char not in map_t or map_s[char] != map_t[char]:
                return False;
        
        return True
                