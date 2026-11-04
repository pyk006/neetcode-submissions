class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_arr = [0 for _ in range(128)]
        best = 0
        left = 0
        for right in range(len(s)):
            while char_arr[ord(s[right])] > 0:
                char_arr[ord(s[left])] -= 1
                left += 1
            char_arr[ord(s[right])] += 1
            best = max(best, right - left + 1)
        return best