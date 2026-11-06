class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)//2):
            matrix[i],matrix[len(matrix)-1-i] = matrix[len(matrix)-1-i],matrix[i]
        i = 0
        while i < len(matrix):
            j = i+1
            while j < len(matrix):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                j += 1
            i += 1
        
