class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            char_count = [0] * 26
            for char in strs[i]:
                char_count[ord(char) - ord('a')] += 1
            
            char_count_key = tuple(char_count)
            if char_count_key not in groups:
                groups[char_count_key] = []
            groups[char_count_key].append(strs[i])

        all_sublist = list(groups.values())
        return all_sublist