class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeats = set()
        left = 0
        best = 0
        for right in range(len(s)):
            while s[right] in repeats:
                repeats.remove(s[left])
                left += 1
            repeats.add(s[right])
            best = max(right - left + 1, best)
        return best
