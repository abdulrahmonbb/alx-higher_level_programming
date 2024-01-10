#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = [[elem**2 for elem in row] for row in matrix]
    return squared_matrix
