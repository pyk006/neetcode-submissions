class Solution:
    def checkValidString(self, s: str) -> bool:
        total = 0
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '*':
                total += 1
            else:
                total -= 1
            
            if total < 0:
                return False
        
        total = 0

        for i in reversed(range(len(s))):
            if s[i] == ')' or s[i] == '*':
                total += 1
            else:
                total -= 1
            
            if total < 0:
                return False
        
        return True