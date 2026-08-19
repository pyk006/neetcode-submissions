class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        final_day = days[-1]
        def dp(day):
            if day in memo:
                return memo[day]
            if day > final_day:
                return 0
            
            if day not in days:
                memo[day] = dp(day + 1)
                return memo[day]
            
            cost_one = costs[0] + dp(day + 1)
            cost_seven = costs[1] + dp(day + 7)
            cost_thirty = costs[2] + dp(day + 30)

            memo[day] = min(cost_one, cost_seven, cost_thirty)
            return memo[day]
        
        return dp(days[0])