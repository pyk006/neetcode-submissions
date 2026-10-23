class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        max_time = 0
        while q:
            current_i, current_j, current_t = q.popleft()
            if current_i + 1 < len(grid):
                if grid[current_i + 1][current_j] == 1:
                    q.append((current_i + 1, current_j, current_t + 1))
                    grid[current_i + 1][current_j] = 2
                    max_time = max(current_t + 1, max_time)
            if current_i - 1 >= 0:
                if grid[current_i - 1][current_j] == 1:
                    q.append((current_i - 1, current_j, current_t + 1))
                    grid[current_i - 1][current_j] = 2
                    max_time = max(current_t + 1, max_time)
            if current_j + 1 < len(grid[0]):
                if grid[current_i][current_j + 1] == 1:
                    q.append((current_i, current_j + 1, current_t + 1))
                    grid[current_i][current_j + 1] = 2
                    max_time = max(current_t + 1, max_time)
            if current_j - 1 >= 0:
                if grid[current_i][current_j - 1] == 1:
                    q.append((current_i, current_j - 1, current_t + 1))
                    grid[current_i][current_j - 1] = 2
                    max_time = max(current_t + 1, max_time)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return max_time


