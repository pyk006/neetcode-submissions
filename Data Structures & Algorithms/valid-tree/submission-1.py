class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj_list = {}
        for i in range(len(edges)):
            if edges[i][0] in adj_list:
                adj_list[edges[i][0]].append(edges[i][1])
            else:
                adj_list[edges[i][0]] = []
                adj_list[edges[i][0]].append(edges[i][1])
            if edges[i][1] in adj_list:
                adj_list[edges[i][1]].append(edges[i][0])
            else:
                adj_list[edges[i][1]] = []
                adj_list[edges[i][1]].append(edges[i][0])
        
        visited = []
        q = deque()
        q.append(0)
        visited.append(0)
        while q:
            curr = q.popleft()
            neighbors = []
            if curr in adj_list:
                neighbors = adj_list[curr]

            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                visited.append(neighbor)
                q.append(neighbor)
        return len(visited) == n