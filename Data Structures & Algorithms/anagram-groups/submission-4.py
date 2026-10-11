class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dict = {}
        for i in range(len(strs)):
            occ_arr = [0 for _ in range(26)]
            for char in strs[i]:
                occ_arr[ord('a') - ord(char)] += 1

            occ_arr_tuple = tuple(occ_arr)
            if occ_arr_tuple in char_dict:
                char_dict[occ_arr_tuple].append(strs[i])
            else:
                char_dict[occ_arr_tuple] = []
                char_dict[occ_arr_tuple].append(strs[i])
        
        return list(char_dict.values())