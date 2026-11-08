class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = 0
        left = 0
        right = n - 1
        bottom = n - 1
        arr = [[0 for _ in range(n)] for _ in range(n)]
        counter = 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                arr[top][i] = counter
                counter += 1
            for i in range(top + 1, bottom + 1):
                arr[i][right] = counter
                counter += 1
            if top != bottom:
                for i in range(right - 1, left - 1, -1):
                    arr[bottom][i] = counter
                    counter += 1
            if left != right:
                for i in range(bottom - 1, top, -1):
                    arr[i][left] = counter
                    counter += 1
            top += 1
            left += 1
            bottom -= 1
            right -= 1
        
        return arr