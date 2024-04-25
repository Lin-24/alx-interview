#!/usr/bin/python3
"""
Module for rotating a 2D matrix in-place by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The 2D matrix to rotate.
    """
    for i in range(int(len(matrix) / 2)):
        for j in range(i, (len(matrix) - i - 1)):
            x = (len(matrix) - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[(len(matrix) - i - 1)][x]
            matrix[(len(matrix) - i - 1)][x] = matrix[j][(len(matrix) - i - 1)]
            matrix[j][(len(matrix) - i - 1)] = tmp
