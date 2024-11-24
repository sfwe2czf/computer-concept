# import math
# from collections import deque

def print_matrix(mat):
    for i in range(len(mat)):
        print("LEVEL ", i)
        for j in range(len(mat[0])):
            for k in range(len(mat[0][0])):
                print(f'{mat[i][j][k]:>3}', end=' ')
            print()


def propagation(mat, src):
    """
    Do not modify function name, parameters and return value
    Write your code below
    """
    mat[src[2]][src[1]][src[0]] = 0

    z = src[2]
    y = src[1]
    x = src[0]

    if x < len(mat[0][0]) - 1:
        if mat[z][y][x + 1] == 0 and not (x+1 == src[0] and y == src[1] and z == src[2]):
            mat[z][y][x + 1] = 1
    if x > 0:
        if mat[z][y][x - 1] == 0 and not (x-1 == src[0] and y == src[1] and z == src[2]):
            mat[z][y][x - 1] = 1
    if y < len(mat[0]) - 1:
        if mat[z][y + 1][x] == 0 and not (x == src[0] and y+1 == src[1] and z == src[2]):
            mat[z][y + 1][x] = 1
    if y > 0:
        if mat[z][y - 1][x] == 0 and not (x == src[0] and y-1 == src[1] and z == src[2]):
            mat[z][y - 1][x] = 1
    if z < len(mat):
        if mat[z + 1][y][x] == 0 and not (x == src[0] and y == src[1] and z+1 == src[2]):
            mat[z + 1][y][x] = 1
    if z > 0:
        if mat[z - 1][y][x] == 0 and not (x == src[0] and y == src[1] and z-1 == src[2]):
            mat[z - 1][y][x] = 1

    for i in range(1, len(mat[0][0])+len(mat[0])+len(mat)+1):
        for z in range(0, len(mat)):
            for y in range(0, len(mat[0])):
                for x in range(0, len(mat[0][0])):
                    if mat[z][y][x] == i:
                        if x < len(mat[0][0])-1:
                            if mat[z][y][x+1] == 0 and not(x+1 == src[0] and y == src[1] and z == src[2]):
                                mat[z][y][x+1] = i+1
                        if x > 0:
                            if mat[z][y][x - 1] == 0 and not(x-1 == src[0] and y == src[1] and z == src[2]):
                                mat[z][y][x-1] = i+1
                        if y < len(mat[0])-1:
                            if mat[z][y+1][x] == 0 and not(x == src[0] and y+1 == src[1] and z == src[2]):
                                mat[z][y+1][x] = i+1
                        if y > 0:
                            if mat[z][y-1][x] == 0 and not(x == src[0] and y-1 == src[1] and z == src[2]):
                                mat[z][y-1][x] = i+1
                        if z < len(mat)-1:
                            if mat[z+1][y][x] == 0 and not(x == src[0] and y == src[1] and z+1 == src[2]):
                                mat[z+1][y][x] = i+1
                        if z > 0:
                            if mat[z-1][y][x] == 0 and not(x == src[0] and y == src[1] and z-1 == src[2]):
                                mat[z-1][y][x] = i+1

    return mat


if __name__ == "__main__":
    # Example
    # mat 5x5x3
    mat = [[[ 0, -1, -1,  0,  0],[ 0,  0,  0,  0, -1],[ 0, -1,  0,  0, -1],[ 0, -1, -1,  0,  0],[ 0, -1,  0, -1,  0]],[[ 0,  0,  0, -1, -1],[ 0, -1,  0,  0, -1],[ 0, -1,  0,  0,  0],[-1, -1,  0, -1,  0],[ 0,  0, -1,  0,  0]], [[-1, -1, -1,  0,  0],[ 0, -1, -1, -1, -1],[-1,  0,  0,  0,  0],[-1, -1, -1,  0, -1],[ 0,  0,  0,  0, -1]]]

    print("Original matrix ")
    print_matrix(mat)
    print("\n Propagated matrix")
    # start point (0, 0, 0)
    mat = propagation(mat, (2, 2, 1))
    print_matrix(mat)
    print(mat)
    """
    Layer 0
      0   1   2   3   4 
      1   2   3   4   5 
      2   3   4   5   6 
      3   4   5   6   7 
      4   5   6   7   8 
    Layer 1
      1   2   3   4   5 
      2   3   4   5   6 
      3   4   5   6   7 
      4   5   6   7   8 
      5   6   7   8   9 
    Layer 2
      2   3   4   5   6 
      3   4   5   6   7 
      4   5   6   7   8 
      5   6   7   8   9 
      6   7   8   9  10 
    """

