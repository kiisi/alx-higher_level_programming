#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            matrix[i][j] = (matrix[i][j]) * (matrix[i][j])
    return matrix
