class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        duplicates = set()
        for right in range(len(s)):
            while s[right] in duplicates:
                duplicates.remove(s[left])
                left+= 1
            
            longest = max(longest, right - left + 1)
            duplicates.add(s[right])
        
        return longest
                