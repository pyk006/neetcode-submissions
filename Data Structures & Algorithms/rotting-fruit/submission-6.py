class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_queue = deque()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_queue.append((i, j, 0))
        max_time = 0
        while rotten_queue:
            current_i, current_j, current_time = rotten_queue.popleft()
            neighbors = [(current_i + 1, current_j), (current_i - 1, current_j), (current_i, current_j + 1), (current_i, current_j - 1)]
            for neighbor in neighbors:
                if neighbor[0] <= len(grid) - 1 and neighbor[0] >= 0 and neighbor[1] <= len(grid[0]) - 1 and neighbor[1] >= 0:
                    if grid[neighbor[0]][neighbor[1]] == 1:
                        row = neighbor[0]
                        col = neighbor[1]
                        grid[row][col] = 2
                        rotten_queue.append((row, col, current_time + 1))
                        max_time = max(max_time, current_time + 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return max_time if 1 not in grid else -1
