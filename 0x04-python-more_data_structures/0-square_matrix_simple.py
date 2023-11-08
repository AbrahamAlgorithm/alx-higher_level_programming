#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0 or matrix is None:
        return (None)
    new_matrix = []
    for each in matrix:
        new_matrix.append([x ** 2 for x in each])
    return (new_matrix)
