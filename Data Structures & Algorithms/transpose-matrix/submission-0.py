import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # matrix1 = matrix
        r = len(matrix)
        c = len(matrix[0])
        
        matrix1 = [[0]*r for _ in range(c)]
        # matrix1 = [[0 *r for _ in range(r)] for _ in range(c)]
        # matrix1= np.zeros((c,r), dtype = int)
        # print(matrix1)
        
        for row in range(c):
            for col in range(r):
                matrix1[row][col] = matrix[col][row]
        # print(matrix1)
        return matrix1



       