class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            start = 0
            end = len(matrix[0])
            while start <= end:
                mid = (start + end) // 2
                if mid > len(matrix[0]) - 1:
                    break
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    end -= 1
                else:
                    start += 1
        
        return False