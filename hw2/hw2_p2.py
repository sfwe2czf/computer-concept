"""
Programming assignment # 2
- Problem # 2: Find area of polygon
"""

def get_polygon_area(polygon_coord):
    """ Implement here """
    x = 0
    y = 1
    polygon_area = 0
    for i in range(2, len(polygon_coord)-1):
        if i % 2 == 0:
            polygon_area += (polygon_coord[i][y] - polygon_coord[0][y]) * (polygon_coord[i][x]-polygon_coord[0][x])
        else:
            polygon_area -= (polygon_coord[i][y] - polygon_coord[0][y]) * (polygon_coord[i][x]-polygon_coord[0][x])




    """ Do not modify function parameters and return """
    return polygon_area


if __name__ == "__main__":
    # example 1
    polygon_coord = [[0, 0], [0, 4], [6, 4], [6, 0]]
    # example 2
    # polygon_coord = [[0, 0], [0, 4], [3, 4], [3, 2], [6, 2], [6, 0]]
    # example 3
    '''
    polygon_coord = [[0, 1], [0, 6], [5, 6], [5, 3], [2, 3], [2, 4],
                    [4, 4], [4, 5], [1, 5], [1, 2], [2, 2], [2, 1],
                    [6, 1], [6, 5], [7, 5], [7, 0], [1, 0], [1, 1]]
    '''

    # print input
    print("polygon coordinates:", polygon_coord)
    polygon_area = get_polygon_area(polygon_coord)

    # print output
    print("polygon area:", polygon_area)
