class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        best = []
        t_dict = {}
        s_dict = {}
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1
        good = 0
        for right in range(len(s)):
            if s[right] not in s_dict:
                s_dict[s[right]] = 1
            else:
                s_dict[s[right]] += 1
            
            if s[right] in t_dict:
                if t_dict[s[right]] == s_dict[s[right]]:
                    good += 1
            
            isGood = good == len(t_dict)
            
            while isGood and left <= right:
                if len(best) == 0 or (right - left + 1) < len(best):
                    best = s[left: right + 1]
                popped_val = s[left]
                left += 1
                if s_dict[popped_val] > 1:
                    s_dict[popped_val] -= 1
                else:
                    del s_dict[popped_val]
                
                if popped_val in t_dict:
                    if s_dict.get(popped_val, 0) < t_dict[popped_val]:
                        good -= 1
                isGood = good == len(t_dict)
        return "" if len(best) == 0 else "".join(best)
            