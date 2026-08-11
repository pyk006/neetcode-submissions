class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_occurrences = {}
        for i in range(len(s1)):
            s1_occurrences[s1[i]] = s1_occurrences.get(s1[i], 0) + 1
        
        left = 0
        slide_occ = {}
        for right in range(len(s2)):
            if s2[right] in s1_occurrences:
                slide_occ[s2[right]] = slide_occ.get(s2[right], 0) + 1
            if (right - left + 1) > len(s1):
                if s2[left] in slide_occ:
                    slide_occ[s2[left]] -= 1
                left += 1
            if (right - left + 1) == len(s1):
                isGood = True
                for key, value in s1_occurrences.items():
                    if value != slide_occ.get(key, 0):
                        isGood = False
                if isGood:
                    return True
        return False