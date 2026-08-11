class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occurrences = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            occurrences[s[right]] = occurrences.get(s[right], 0) + 1
            char, max_freq = max(occurrences.items(), key=lambda x: x[1])
            while (right - left + 1) - max_freq > k:
                occurrences[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        
        return max_length