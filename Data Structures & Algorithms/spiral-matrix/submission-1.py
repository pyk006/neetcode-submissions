class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiraled = []
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                spiraled.append(matrix[top][i])
            
            for i in range(top + 1, bottom + 1):
                spiraled.append(matrix[i][right])
            
            if top != bottom:
                for i in range(right - 1, left - 1, -1):
                    spiraled.append(matrix[bottom][i])
            if right != left:
                for i in range(bottom - 1, top, -1):
                    spiraled.append(matrix[i][left])
            top += 1
            left += 1
            bottom -= 1
            right -= 1
        return spiraled