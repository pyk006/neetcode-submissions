class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        best = float('infinity')
        while start < end:
            mid = (start + end) // 2

            cap = 0
            days_need = 1
            for i in range(len(weights)):
                if cap + weights[i] > mid:
                    days_need += 1
                    cap = weights[i]
                else:
                    cap += weights[i]
            
            if days_need <= days:
                best = min(best, mid)
                end = mid
            else:
                start = mid + 1
        
        return start