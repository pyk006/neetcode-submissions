class MinStack:
    def __init__(self):
        self.min = []
        self.reg_stack = []
    def push(self, val: int) -> None:
        if len(self.min) == 0:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        self.reg_stack.append(val)

    def pop(self) -> None:
        popped = self.reg_stack.pop()
        if popped == self.min[-1]:
            self.min.pop()
    def top(self) -> int:
        return self.reg_stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
