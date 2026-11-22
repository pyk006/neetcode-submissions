class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        while start < end:
            mid = (start + end) // 2
            days_req = 1
            cap = 0
            for i in range(len(weights)):
                if weights[i] + cap > mid:
                    days_req += 1
                    cap = weights[i]
                else:
                    cap += weights[i]
            
            if days_req <= days:
                end = mid
            else:
                start = mid + 1
        return start