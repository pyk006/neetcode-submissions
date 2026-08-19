class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '*':
                count += 1
            else:
                count -= 1
            
            if count < 0:
                return False

        
        count = 0
        for i in reversed(range(len(s))):
            if s[i] == ')' or s[i] == '*':
                count += 1
            else:
                count -= 1
            
            if count < 0:
                return False
        return True