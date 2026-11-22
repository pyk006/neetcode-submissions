class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        while start < end:
            mid = (start + end) // 2

            cap = 0

            for i in range(len(piles)):
                cap += math.ceil(piles[i] / mid)
            
            if cap <= h:
                end = mid
            else:
                start = mid + 1
        
        return start