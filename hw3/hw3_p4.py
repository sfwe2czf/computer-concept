# import math
from collections import deque

def adjacent(mat, point):
    list = []

    L = len(mat)
    N = len(mat[0])
    M = len(mat[0][0])

    x = point[0]
    y = point[1]
    z = point[2]
    i = mat[z][y][x]

    if x+1 <= M-1:
        if mat[z][y][x+1] == i-1:
            list.append((x+1, y, z))
    if x-1 >= 0:
        if mat[z][y][x-1] == i-1:
            list.append((x-1, y, z))
    if y+1 <= N-1:
        if mat[z][y+1][x] == i-1:
            list.append((x, y+1, z))
    if y-1 >= 0:
        if mat[z][y-1][x] == i-1:
            list.append((x, y-1, z))
    if z+1 <= L-1:
        if mat[z+1][y][x] == i-1:
            list.append((x, y, z+1))
    if z-1 >= 0:
        if mat[z-1][y][x] == i-1:
            list.append((x, y, z-1))
    return list

def backtracking(mat, src, dest):
    """
        Do not modify function name, parameters and return value
        Write your code below
    """
    path_list = []
    k = mat[dest[2]][dest[1]][dest[0]]
    makinglist = []
    makinglist.append([])
    makinglist[0].append(adjacent(mat, dest))
    for i in range(0, k-1):
        makinglist.append([])
        for j in makinglist[i]:
            for l in range(0, len(j)):
                makinglist[i + 1].append(adjacent(mat, j[l]))

    for j in range(len(makinglist[-1])):
        lb = [dest]
        for i in range(0, k):
            p = j % len(makinglist[i])
            q = j % len(makinglist[i][p])
            lb.append(makinglist[i][p][q])
        path_list.append(lb)


    return path_list


if __name__ == "__main__":
    # mat 5x5x3 (sample)
    mat = [[[0, 1, 2, 3, 4],
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 4, 5, 6, 7],
            [4, 5, 6, 7, 8]],
           [[1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 4, 5, 6, 7],
            [4, 5, 6, 7, 8],
            [5, 6, 7, 8, 9]],
           [[2, 3, 4, 5, 6],
            [3, 4, 5, 6, 7],
            [4, 5, 6, 7, 8],
            [5, 6, 7, 8, 9],
            [6, 7, 8, 9, 10]]]

    # start point (0, 0, 0), end point (4, 4, 2)
    path = backtracking(mat, (0, 0, 0), (4, 4, 2))
    print(path)
