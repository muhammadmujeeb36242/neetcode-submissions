class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> List[List[int]]:
        i = 0
        indices = []
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                if matrix[i][j] == 0:
                    indices.append([i,j])
                j += 1
            i += 1
        for x in indices:
            for i in range(len(matrix)):
                matrix[i][x[1]] = 0
            for i in range(len(matrix[0])):
                matrix[x[0]][i] = 0