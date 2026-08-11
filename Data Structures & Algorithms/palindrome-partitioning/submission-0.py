class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(start, allList, currentArr):
            if start == len(s):
                allList.append(currentArr.copy())
            for i in range(start, len(s)):
                sub = s[start:i+1]
                begin = 0
                end = len(sub) - 1
                isPalindrome = True
                while begin < end:
                    if sub[begin] != sub[end]:
                        isPalindrome = False
                        break
                    begin += 1
                    end -= 1
                if isPalindrome:
                    currentArr.append(sub)
                    backtrack(i + 1, allList, currentArr)
                    currentArr.pop()
        
        allList = []
        backtrack(0, allList, [])
        return allList