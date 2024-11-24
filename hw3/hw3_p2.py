import math

def make_room(room, name):
    """
    Do not modify function name, parameters and return value
    Write your code below
    """
    # mat = [[[]]] <-- 3d matrix
    mat = []
    for i in range(room[name]['size'][2]):
        mat.append([])
        for j in range(room[name]['size'][1]):
            mat[i].append([])
            for k in range(room[name]['size'][0]):
                mat[i][j].append(0)
    for i in range(len(room[name]['obs'])):
        if room[name]['obs'][i]:
            for j in room[name]['obs'][i]:
                for k in range(math.floor(j[3]), math.ceil(j[1])):
                    for l in range(math.floor(j[0]), math.ceil(j[2])):
                        mat[i][k][l] = -1

    return mat


if __name__=="__main__":

    room = {'ROOM614': {'size': [5, 5, 3],
                        'src': [0, 1, 0],
                        'dest': [3, 4, 2],
                        'obs': [[[3.2, 3.7, 4.5, 1.0]], [], [[3.1, 0.6, 4.9, 0.2], [0.0, 4.1, 1.5, 2.0]]]},
            'ROOM653-3': {'size': [10, 15, 4],
                          'src': [9, 14, 3],
                          'dest': [3, 4, 0],
                          'obs': [[], [[3.2, 3.7, 4.5, 1.0]], [], [[3.1, 0.6, 4.9, 0.2], [0.0, 4.1, 1.5, 2.0]]]}
            }
    room_name = 'ROOM614'

    mat = make_room(room, room_name)