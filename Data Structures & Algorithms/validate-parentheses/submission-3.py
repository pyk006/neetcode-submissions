class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2:
            return False;
        for single_char in s:
            if single_char == '(':
                stack.append('(')
            elif single_char == '[':
                stack.append('[')
            elif single_char == '{':
                stack.append('{')
            elif single_char == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif single_char == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            elif single_char == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False
        
        return len(stack) == 0