class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = low + (high - low) // 2

            row = mid // cols
            col = mid % cols

            curr = matrix[row][col]
            if curr == target:
                return True
            if curr < target:
                low = mid + 1
            else:
                high = mid - 1
        return False