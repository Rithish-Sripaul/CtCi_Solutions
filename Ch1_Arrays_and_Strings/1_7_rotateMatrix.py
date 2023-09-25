"""
1_7: Rotate Matrix: 
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

"""
The easiest way to do this is to implement the rotation in layers
We perform a circular rotation on each layer, moving the top edge to the right edge, the right edge
to the bottom edge, the bottom edge to the left edge, and the left edge to the top edge.
"""
def rotateMatrix(matrix):
    
    if (len(matrix) == 0 or len(matrix) != len(matrix[0])): return False

    n = len(matrix)
    
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            top = matrix[first][i]

            # bottom left -> top left
            matrix[first][i] = matrix[last - offset][first]
            
            # bottom right -> bottom left
            matrix[last - offset][first] = matrix[last][last - offset]

            # top right -> bottom right
            matrix[last][last - offset] = matrix[i][last]

            matrix[i][last] = top
    return matrix

matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
print(rotateMatrix(matrix))



def rotateMatrix_neetcode(matrix):
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            topLeft = matrix[top][l + i]

            # move bottom left to top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # move bottom right to bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move top right to bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            matrix[top + i][r] = topLeft
        l += 1
        r -= 1
    return matrix

matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
print(rotateMatrix_neetcode(matrix))