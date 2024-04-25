#!/usr/bin/python3

"""
This module provides a function to rotate a 2D matrix 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    :param matrix: The 2D matrix to be rotated.
    :type matrix: List[List[int]]
    """
    n = len(matrix)
    
    # Traverse each layer of the matrix
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        
        # Iterate over each element in the current layer
        for i in range(first, last):
            # Store the current element in a temporary variable
            temp = matrix[first][i]

            # Move values from right to top
            matrix[first][i] = matrix[n - 1 - i][first]

            # Move values from bottom to right
            matrix[n - 1 - i][first] = matrix[last][n - 1 - i]

            # Move values from left to bottom
            matrix[last][n - 1 - i] = matrix[i][last]

            # Move values from temp to left
            matrix[i][last] = temp
