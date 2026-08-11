class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        strDict = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        if len(digits) == 0:
            return []
        def backtrack(current, index, allList):
            if len(current) > len(digits):
                return
            if len(current) == len(digits):
                allList.append(current)
                return
            
            if index < len(digits):
                currentStr = strDict[digits[index]]
                for i in range(len(currentStr)):
                    backtrack(current + currentStr[i], index + 1, allList)
        
        allList = []
        backtrack("", 0, allList)
        return allList
                
