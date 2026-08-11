class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_counter = [0] * 26
        anagram_map = {}
        grouped_list = []
        for i in range(len(strs)):
            char_counter = [0] * 26
            for char in strs[i]:
                char_counter[ord(char) - ord('a')] += 1
            key = tuple(char_counter)
            if key not in anagram_map:
                anagram_map[key] = []
                anagram_map[key].append(strs[i])
            else:
                anagram_map[key].append(strs[i])
        for grouped in anagram_map:
            grouped_list.append(anagram_map[grouped])
        return grouped_list

 