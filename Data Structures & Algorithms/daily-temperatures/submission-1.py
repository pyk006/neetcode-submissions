class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        temps = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            while len(temp_stack) > 0 and temperatures[i] > temperatures[temp_stack[-1]]:
                temps[temp_stack[-1]] = i - temp_stack[-1]
                temp_stack.pop()
            temp_stack.append(i)
            
        return temps