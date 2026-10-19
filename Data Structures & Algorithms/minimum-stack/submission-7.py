class MinStack:

    def __init__(self):
        self.min_stack = []
        self.reg_stack = []

    def push(self, val: int) -> None:
        self.reg_stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)
                

    def pop(self) -> None:
        popped = self.reg_stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.reg_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
