class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_graph = {}
        q = deque()
        visited = set()
        print(visited)
        for i in range(len(edges)):
            node_one = edges[i][0]
            node_two = edges[i][1]

            if node_one not in adj_graph:
                adj_graph[node_one] = []
            
            adj_graph[node_one].append(node_two)

            if node_two not in adj_graph:
                adj_graph[node_two] = []
            
            adj_graph[node_two].append(node_one)

        
        res = 0
        for i in range(n):
            if i not in adj_graph:
                res += 1
                continue
            if i not in visited:
                res += 1
                q.append(i)
                visited.add(i)
                while q:
                    current = q.popleft()
                    neighbors = adj_graph[current]

                    for neighbor in neighbors:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)

        
        return res
            
            