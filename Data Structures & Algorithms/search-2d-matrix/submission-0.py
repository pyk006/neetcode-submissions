class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            start = 0
            end = len(matrix[0]) - 1

            while start <= end:
                mid = (start + end) // 2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] < target:
                    start += 1
                if matrix[i][mid] > target:
                    end -= 1
        
        return False