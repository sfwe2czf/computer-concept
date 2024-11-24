"""
Programming assignment # 1
- Problem 2: Find a bounding box
"""
def main():
    n = int(input("Enter size of coordinate plane : "))
    x1, y1 = input("Enter first point (x1, y1) : ").split(",")
    x2, y2 = input("Enter second point (x2, y2) : ").split(",")
    x3, y3 = input("Enter third point (x3, y3): ").split(",")

    x1, y1, x2, y2, x3, y3 = int(x1), int(y1), int(x2), int(y2), int(x3), int(y3)

    """ implement here """
    a = " *"
    b = " X"
    c = " O"
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    while x_min < x1 and x_min < x2 and x_min < x3:
        x_min += 1
    while y_min < y1 and y_min < y2 and y_min < y3:
        y_min += 1
    while x_max < x1 or x_max < x2 or x_max < x3:
        x_max += 1
    while y_max < y1 or y_max < y2 or y_max < y3:
        y_max += 1
    area = (x_max - x_min) * (y_max - y_min)
    for i in range(1, x_min):
        print(a*n)
    for i in range(x_min, x_min+1):
        for j in range(1, y_min):
            print(a, end="")
        for j in range(y_min, y_max+1):
            if (i == x1 and j == y1) or (i == x2 and j == y2) or (i == x3 and j == y3):
                print(b, end="")
            else:
                print(c, end="")
        for j in range(y_max+1, n+1):
            print(a, end="")
    print("")
    for i in range(x_min+1, x_max):
        for j in range(1, y_min):
            print(a, end="")
        for j in range(y_min, y_min +1):
            if (i == x1 and j == y1) or (i == x2 and j == y2) or (i == x3 and j == y3):
                print(b, end="")
            else:
                print(c, end="")
        for j in range(y_min+1, y_max):
            if (i == x1 and j == y1) or (i == x2 and j == y2) or (i == x3 and j == y3):
                print(b, end="")
            else:
                print(a, end="")
        for j in range(y_max, y_max+1):
            if (i == x1 and j == y1) or (i == x2 and j == y2) or (i == x3 and j == y3):
                print(b, end="")
            else:
                print(c, end="")
        for j in range(y_max+1, n+1):
            print(a, end="")
        print("")
    for i in range(x_max, x_max+1):
        for j in range(1, y_min):
            print(a, end="")
        for j in range(y_min, y_max+1):
            if (i == x1 and j == y1) or (i == x2 and j == y2) or (i == x3 and j == y3):
                print(b, end="")
            else:
                print(c, end="")
        for j in range(y_max+1, n+1):
            print(a, end="")
    print("")
    for i in range(x_max+1, n+1):
        print(a*n)
    print(f"Area of bounding box is {area:d}")
    """ do not touch below code """


if __name__ == "__main__":
    main()
