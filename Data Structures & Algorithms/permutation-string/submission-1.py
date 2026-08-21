class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        occ_count = [0 for _ in range(26)]
        original = [0 for _ in range(26)]
        curr_subarray = []
        for i in range(len(s1)):
            original[ord(s1[i]) - ord('a')] += 1
        left = 0
        for right in range(len(s2)):
            curr_char = s2[right]
            curr_subarray.append(curr_char)
            occ_count[ord(curr_char) - ord('a')] += 1
            if occ_count == original:
                return True
            if len(curr_subarray) == len(s1):
                left_char = ord(s2[left]) - ord('a')
                occ_count[left_char] -= 1
                curr_subarray.remove(s2[left])
                left += 1
        return False