class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isnumeric():
                stack.append(int(tokens[i]))
            if tokens[i] == "+":
                val_1 = stack.pop()
                val_2 = stack.pop()
                stack.append(val_1 + val_2)
            if tokens[i] == "*":
                val_1 = stack.pop()
                val_2 = stack.pop()
                stack.append(val_1 * val_2)
            if tokens[i] == "-":
                val_1 = stack.pop()
                val_2 = stack.pop()
                stack.append(val_2 - val_1)
            if tokens[i] == "/":
                val_1 = stack.pop()
                val_2 = stack.pop()
                stack.append(int(val_2 / val_1))
        
        return stack[-1]