class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        rowTrack = [0 for _ in range(row)]
        colTrack = [0 for _ in range(col)]

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowTrack[i] = -1
                    colTrack[j] = -1
        
        for i in range(row):
            for j in range(col):
                if rowTrack[i] == -1 or colTrack[j] == -1:
                    matrix[i][j] = 0