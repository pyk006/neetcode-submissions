class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        num_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backtrack(curr, combos, index):
            if len(curr) == len(digits):
                combos.append(curr)
                return
            if index < len(digits):
                for i in range(len(num_dict[digits[index]])):
                    backtrack(curr + num_dict[digits[index]][i], combos, index + 1)
        combos = []
        backtrack("", combos, 0)
        return combos