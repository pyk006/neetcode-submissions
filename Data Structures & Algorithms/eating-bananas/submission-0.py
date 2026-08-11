class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        best = float('inf')
        while start < end:
            mid = (start + end) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
            
            if hours <= h:
                best = min(mid, best)
                end = mid
            else:
                start = mid + 1
        
        return max(piles) if best == float('inf') else best