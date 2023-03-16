#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    A function that computes all the square
    values of all integers in the matrix
    """
    new_matrix = []
    for col in matrix:
        result = [x**2 for x in col]
        new_matrix.append(result)
    return new_matrix
