class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_arr = [0 for _ in range(26)]
        for i in range(len(s)):
            char_arr[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            if char_arr[ord(t[i]) - ord('a')] == 0:
                return False
            char_arr[ord(t[i]) - ord('a')] -= 1
        return all(x == 0 for x in char_arr)
