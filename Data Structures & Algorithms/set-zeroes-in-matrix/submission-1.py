class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = []
        zero_columns = []
        for i in range (len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_columns.append(j)
                    # i is top, i is bottom
                    # j is left, j is right
        for i in zero_rows:
            for index in range(len(matrix[0])):
                matrix[i][index] = 0
        
        for i in zero_columns:
            for index in range(len(matrix)):
                matrix[index][i] = 0

        print(matrix)