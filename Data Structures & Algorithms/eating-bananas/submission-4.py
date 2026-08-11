class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        best = float('infinity')

        while start < end:
            mid = (start + end) // 2

            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i] / mid)
            
            if count <= h:
                best = min(best, mid)
                end = mid
            else:
                start = mid + 1
        
        return max(piles) if best == float('infinity') else best
