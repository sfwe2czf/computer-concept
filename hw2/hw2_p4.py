"""
Programming assignment # 2
- Problem # 4: Rotate matrix
"""
def rotate(mat, sx, sy, m, n, direction, iteration):
    """ Implement here """
    partmat = []
    for i in range(sx, sx + m):
        partmat.append([])
        for j in range(sy, sy + n):
            partmat[i].append(mat[i][j])
    if direction == "CCW":
        partlist = []
        for i in range(0, m):
            partlist.append(partmat[i][0])
        for j in range(1, n):
            partlist.append(partmat[m-1][j])
        for i in range(m-2, -1, -1):
            partlist.append(partmat[i][n-1])
        for j in range(n-2, 0, -1):
            partlist.append(partmat[0][j])
        newlist = []
        for i in range(0, len(partlist)):
            newlist.append(0)
        for i in range(0, len(partlist)):
            newlist[(i + iteration % (2*m + 2*n - 4)) % len(newlist)] = partlist[i]
        for i in range(0, m):
            partmat[i][0] = newlist[i]
        for j in range(1, n):
            partmat[m-1][j] = newlist[m-1 + j]
        for i in range(m-2, -1, -1):
            partmat[i][n-1] = newlist[-i + 2*m + n - 3]
        for j in range(n-2, 0, -1):
            partmat[0][j] = newlist[-j + 2*m + 2*n - 4]
    else:
        partlist = []
        for i in range(0, m):
            partlist.append(partmat[i][0])
        for j in range(1, n):
            partlist.append(partmat[m - 1][j])
        for i in range(m - 2, -1, -1):
            partlist.append(partmat[i][n - 1])
        for j in range(n - 2, 0, -1):
            partlist.append(partmat[0][j])
        newlist = []
        for i in range(0, len(partlist)):
            newlist.append(0)
        for i in range(0, len(partlist)):
            newlist[i] = partlist[(i + iteration % (2 * m + 2 * n - 4)) % len(newlist)]
        for i in range(0, m):
            partmat[i][0] = newlist[i]
        for j in range(1, n):
            partmat[m - 1][j] = newlist[m - 1 + j]
        for i in range(m - 2, -1, -1):
            partmat[i][n - 1] = newlist[-i + 2 * m + n - 3]
        for j in range(n - 2, 0, -1):
            partmat[0][j] = newlist[-j + 2 * m + 2 * n - 4]
    for i in range(0, m):
        for j in range(0, n):
            mat[i + sx][j + sy] = partmat[i][j]



    """ Do not modify function parameters and return """
    return mat


def printMatrix(mat):
    for i, row in enumerate(mat):
        for col in mat[i]:
            print(f'{col:>{3}}', end=' ')
        print()


if __name__ == "__main__":
    """ Example """
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    sx, sy = 0, 0
    m, n = 4, 3
    direction = 'CCW'
    iteration = 1
    print("Original matrix: ")
    printMatrix(matrix)
    # Execute rotate function
    rotated_matrix = rotate(matrix, sx, sy, m, n, direction, iteration)
    print("Rotated matrix: ")
    printMatrix(rotated_matrix)

    """
    Original matrix: 
      1   2   3   4 
      5   6   7   8 
      9  10  11  12 
     13  14  15  16 
    Rotated matrix: 
      2   3   7   4 
      1   6  11   8 
      5  10  15  12 
      9  13  14  16 
    """

