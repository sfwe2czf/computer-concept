def parse_room_escape(dir):
    """
    Do not modify function name, parameters and return value
    Write your code below
    """
    f = open(dir, "r")

    room_list = []
    iss = False
    isd = False

    for line in f:
        if "ROOM" == line[0:4]:
            room_list.append([line.strip()[5:], {'size': [0, 0, 0], 'src': [0], 'dest': [0], 'obs': []}])
        elif "  LEVEL" == line[0:7]:
            for i in range(0, len(room_list)):
                if room_list[i][1]['size'][0] == 0:
                    room_list[i][1]['size'][2] = int(line.strip().split(" ")[1])
                    break
        elif "  SIZE" == line[0:6]:
            for i in range(0, len(room_list)):
                if room_list[i][1]['size'][0] == 0:
                    room_list[i][1]['size'][0] = int(line.strip().split(" ")[1])
                    room_list[i][1]['size'][1] = int(line.strip().split(" ")[3])
                    break
        if iss:
            for i in range(0, len(room_list)):
                if room_list[i][1]['src'] == [0]:
                    room_list[i][1]['src'] = [int(line.strip().split(" ")[1]), int(line.strip().split(" ")[2])]
                    room_list[i][1]['src'].append(int(line.strip().split(" ")[0][5])-1)
                    break
            iss = False
        if "  SRC" == line[0:5]:
            iss = True
        if isd:
            for i in range(0, len(room_list)):
                if room_list[i][1]['dest'] == [0]:
                    room_list[i][1]['dest'] = [int(line.strip().split(" ")[1]), int(line.strip().split(" ")[2])]
                    room_list[i][1]['dest'].append(int(line.strip().split(" ")[0][5])-1)
                    break
            isd = False
        if "  DEST" == line[0:6]:
            isd = True
    for i in range(0, len(room_list)):
        for j in range(0, room_list[i][1]['size'][2]):
            room_list[i][1]['obs'].append([])

    f.close()

    g = open(dir, "r")
    for i in range(0, len(room_list)):
        l = g.readline()
        while l != "  OBS\n":
            l = g.readline()
        l = g.readline()
        while "LEVEL" in l and "END" not in l:
            m = g.readline()
            while "LEVEL" not in m and "END" not in m:
                room_list[i][1]['obs'][int(l.strip().split(" ")[0][5])-1].append([float(m.strip().split(" ")[0]), float(m.strip().split(" ")[1]), float(m.strip().split(" ")[2]), float(m.strip().split(" ")[3])])
                m = g.readline()
            if "LEVEL" in m:
                l = m
            else:
                l = g.readline()

    room = dict(room_list)
    g.close()

    return room


if __name__ == "__main__":

    dir = "C:/Users/user/Desktop/컴개실/과제/Assignment #3/room_escape.txt"

    room = parse_room_escape(dir)

    for i in room:
        print(i, room[i])

















