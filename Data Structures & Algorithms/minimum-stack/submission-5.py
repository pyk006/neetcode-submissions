class MinStack:

    def __init__(self):
        self.min_stack = []
        self.reg_stack = []
    def push(self, val: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
                self.min_stack.append(val)
        self.reg_stack.append(val)

    def pop(self) -> None:
        popped = self.reg_stack.pop()
        if self.min_stack[-1] == popped:
            self.min_stack.pop()

    def top(self) -> int:
        return self.reg_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
     
