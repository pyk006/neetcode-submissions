class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        while queue:
            (r, c) = queue.popleft()
            neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for neighbor in neighbors:
                if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] <= len(grid) - 1 and neighbor[1] <= len(grid[0]) - 1:
                    if grid[neighbor[0]][neighbor[1]] == -1:
                        continue
                    if grid[neighbor[0]][neighbor[1]] == 2147483647:
                        nr = neighbor[0]
                        nc = neighbor[1]
                        grid[nr][nc] = grid[r][c] + 1
                        queue.append((nr, nc))    