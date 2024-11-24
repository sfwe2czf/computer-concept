from hw3_p1 import *
from hw3_p2 import *
from hw3_p3 import *
from hw3_p4 import *


if __name__ == "__main__":
    """ 문제 설명을 읽고 hw3_p1, hw3_p2, hw3_p3, hw_p4를 완성하세요. """
    input_file = "C:/Users/user/Desktop/컴개실/과제/Assignment #3/room_escape.txt"

    # TODO 1 (hw3_p1.py): parse_room_escape(dir)
    room = parse_room_escape(input_file)

    # TODO 2 (hw3_p2.py): make_room(room, name)
    name = 'ROOM614'
    matrix = make_room(room, name)

    # TODO 3 (hw3_p3.py): propagation(mat, src)
    start = tuple(room[name]['src'])
    matrix = propagation(matrix, start)

    # TODO 4 (hw3_p4.py): backtracking(mat, src, dest)
    end = tuple(room[name]['dest'])
    paths = backtracking(matrix, start, end)
