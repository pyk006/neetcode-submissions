class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parans = []
        self.backtrack(n, 0, 0, "", parans)
        return parans
    

    def backtrack(self, n: int, open_p: int, close: int, curr: str, parans: List[str]):
        if len(curr) == n * 2:
            parans.append(curr)
        
        if open_p < n:
            self.backtrack(n, open_p + 1, close, curr + "(", parans)
        
        if close < open_p:
            self.backtrack(n, open_p, close + 1, curr + ")", parans)
            