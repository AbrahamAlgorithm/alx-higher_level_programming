#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print elements in a list of lists in matrix form

    Args:
        matrix: the element that contain list of list

    Returns:
        NULL
    """
    if len(matrix) == 0 or matrix is None:
        return (None)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]), end=' ')
