"""
Programming assignment # 2
- Problem # 3: Find pattern
"""
import random

def make_matrix():
    """
    Use random.randrange(1,4) to make random integer value in range (1, 4)
    """
    matrix = []
    """ implement here """
    for i in range(0, 5):
        matrix.append([])
        for j in range(0, 5):
            matrix[i].append(1)
    for i in range(0, 5):
        for j in range(0, 5):
            matrix[i][j] = random.randrange(1, 4)

    return matrix

def print_matrix(matrix):
    """ implement here """
    for i in range(-1, -6, -1):
        for j in range(0, 5):
            print(matrix[i][j], end=" ")
        print("")

def update_matrix(matrix):
    """ implement here """
    bench = []
    kind = 0
    """up type"""
    for i in range(0, 4):
        for j in range(1, 4):
            if matrix[i][j] == matrix[i+1][j] and matrix[i][j] == matrix[i][j+1] and matrix[i][j] == matrix[i][j-1]:
                kind = 2
                bench.append([i, j, kind])
    """down type"""
    for i in range(1, 5):
        for j in range(1, 4):
            if matrix[i][j] == matrix[i-1][j] and matrix[i][j] == matrix[i][j+1] and matrix[i][j] == matrix[i][j-1]:
                kind = 3
                bench.append([i, j, kind])
    """right type"""
    for i in range(1, 4):
        for j in range(0, 4):
            if matrix[i][j] == matrix[i+1][j] and matrix[i][j] == matrix[i][j+1] and matrix[i][j] == matrix[i-1][j]:
                kind = 4
                bench.append([i, j, kind])
    """left type"""
    for i in range(1, 4):
        for j in range(1, 5):
            if matrix[i][j] == matrix[i+1][j] and matrix[i][j] == matrix[i][j-1] and matrix[i][j] == matrix[i-1][j]:
                kind = 5
                bench.append([i, j, kind])
    """5 type"""
    for i in range(1, 4):
        for j in range(1, 4):
            if matrix[i][j] == matrix[i+1][j] and matrix[i][j] == matrix[i][j+1] and matrix[i][j] == matrix[i][j-1] and matrix[i][j] == matrix[i-1][j]:
                kind = 1
                bench.append([i, j, kind])
    bench.sort()
    if len(bench) == 0:
        center_point = ()
        print("Nothing updated")
    else:
        answer = bench[0]
        center_point = (answer[1], answer[0])
        x = answer[0]
        y = answer[1]
        print("Center point is ({}, {})".format(center_point[0], center_point[1]))
        if answer[2] == 1:
            for i in range(x, 4):
                matrix[i][y-1] = matrix[i+1][y-1]
            matrix[4][y-1] = 0
            for i in range(x, 4):
                matrix[i][y+1] = matrix[i+1][y+1]
            matrix[4][y+1] = 0
            for i in range(x-1, 5):
                if i+3 < 5:
                    matrix[i][y] = matrix[i+3][y]
                else:
                    matrix[i][y] = 0
        elif answer[2] == 2:
            for i in range(x, 4):
                matrix[i][y-1] = matrix[i+1][y-1]
            matrix[4][y-1] = 0
            for i in range(x, 4):
                matrix[i][y+1] = matrix[i+1][y+1]
            matrix[4][y+1] = 0
            for i in range(x, 5):
                if i+2 < 5:
                    matrix[i][y] = matrix[i+2][y]
                else:
                    matrix[i][y] = 0
        elif answer[2] == 3:
            for i in range(x, 4):
                matrix[i][y-1] = matrix[i+1][y-1]
            matrix[4][y-1] = 0
            for i in range(x, 4):
                matrix[i][y+1] = matrix[i+1][y+1]
            matrix[4][y+1] = 0
            for i in range(x-1, 5):
                if i+2 < 5:
                    matrix[i][y] = matrix[i+2][y]
                else:
                    matrix[i][y] = 0
        elif answer[2] == 4:
            for i in range(x, 4):
                matrix[i][y+1] = matrix[i+1][y+1]
            matrix[4][y+1] = 0
            for i in range(x-1, 5):
                if i+3 < 5:
                    matrix[i][y] = matrix[i+3][y]
                else:
                    matrix[i][y] = 0
        elif answer[2] == 5:
            for i in range(x, 4):
                matrix[i][y-1] = matrix[i+1][y-1]
            matrix[4][y-1] = 0
            for i in range(x-1, 5):
                if i+3 < 5:
                    matrix[i][y] = matrix[i+3][y]
                else:
                    matrix[i][y] = 0
    # return format

    return center_point

def main():

    """ do not touch below code """
    matrix = make_matrix()
    print_matrix(matrix)
    center = update_matrix(matrix)
    print("Update finished!")
    print_matrix(matrix)

if __name__ == "__main__":
    main()
