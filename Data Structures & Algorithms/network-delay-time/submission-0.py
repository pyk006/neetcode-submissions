class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_graph = {}
        cost_arr = [float('infinity')] * (n + 1)
        cost_arr[k] = 0
        for i in range(len(times)):
            source_node = times[i][0]
            target_node = times[i][1]
            cost = times[i][2]

            if source_node not in adj_graph:
                adj_graph[source_node] = []
            adj_graph[source_node].append((cost, target_node))
        
        prio_q = []

        heapq.heappush(prio_q, (0, k))
        while prio_q:
            curr_time, curr_node = heapq.heappop(prio_q)

            if curr_time > cost_arr[curr_node]:
                continue
            if curr_node in adj_graph:
                neighbors = adj_graph[curr_node]
                for neighbor in neighbors:
                    next_cost = curr_time + neighbor[0]
                    if next_cost < cost_arr[neighbor[1]]:
                        cost_arr[neighbor[1]] = next_cost
                        heapq.heappush(prio_q, (next_cost, neighbor[1]))
        if max(cost_arr[1:]) == float('infinity'):
            return -1
        return max(cost_arr[1:])
