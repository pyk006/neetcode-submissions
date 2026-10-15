class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open, close, currentSol, allSol):
            if open == n and close == n:
                allSol.append(currentSol)
            if open < n:
                backtrack(open + 1, close, currentSol + "(", allSol)
            if close < open:
                backtrack(open, close + 1, currentSol + ")", allSol)
        
        allSol = []
        backtrack(0, 0, "", allSol)
        return allSol