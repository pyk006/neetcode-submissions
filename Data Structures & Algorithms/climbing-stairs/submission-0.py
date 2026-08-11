class Solution:
    def climbStairs(self, n: int) -> int:
        
        curr = 0
        count = [0]
        def helper(curr):
            if curr > n:
                return
            if curr == n:
                count[0] += 1
                return
            helper(curr + 1)
            helper(curr + 2)
        
        helper(0)
        
        return count[0]