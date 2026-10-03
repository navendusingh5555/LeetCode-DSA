class Solution:
    def markInfinity(self, matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])

        for i in range(0, r):
            if matrix[i][col] != 0:
                matrix[i][col] = float("inf")
        
        for j in range(0, c):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")

    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        for i in range(0, row):
            for j in range(0, col):
                if matrix[i][j] == 0:
                    self.markInfinity(matrix, i, j)
        
        for i in range(0, row):
            for j in range(0, col):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0