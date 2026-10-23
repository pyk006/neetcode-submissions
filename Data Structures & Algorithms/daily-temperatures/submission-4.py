class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            if len(stack) > 0:
                while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                    peek = temperatures[stack[-1]]
                    temperatures[stack[-1]] = i - stack[-1]
                    stack.pop()
            stack.append(i)
        
        while len(stack) != 0:
            temperatures[stack[-1]] = 0
            stack.pop()
        
        return temperatures
