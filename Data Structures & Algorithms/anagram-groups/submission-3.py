class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            char_arr = [0 for _ in range(26)]
            for char in strs[i]:
                char_arr[ord(char) - ord('a')] += 1
            char_arr_tuple = tuple(char_arr)
            if char_arr_tuple not in groups:
                groups[char_arr_tuple] = []
            groups[char_arr_tuple].append(strs[i])
        
        
        return list(groups.values())
