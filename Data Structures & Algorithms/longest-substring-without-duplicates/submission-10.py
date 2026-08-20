class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best_length = 0
        char_set = set()
        left = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            best_length = max(best_length, right - left + 1)
        return best_length
