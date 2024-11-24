"""
Programming assignment # 1
- Problem 4: Print calendar
"""
def main():
    """ implement here """
    month = int(input("Month: "))
    while month != -1:
        if month == -1:
            break
        elif month == 2:
            leap_year = input("Leap year? ")
            if leap_year == "YES":
                day = 29
            else:
                day = 28
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day = 30
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day = 31
        sday = input("Start day: ")
        print("SUN MON TUE WED THU FRI SAT")
        if sday == "SUN":
            for i in range(1, day+1):
                if i%7 == 0 or i == day:
                    ok = "\n"
                else:
                    ok = ""
                print(f"{i:>3d} ", end=ok)
        elif sday == "MON":
            print("    ", end="")
            for i in range(1, day+1):
                if i%7 == 6 or i == day:
                    ok = "\n"
                else:
                    ok = ""
                print(f"{i:>3d} ", end=ok)
        elif sday == "TUE":
            print("        ", end="")
            for i in range(1, day+1):
                if i%7 == 5 or i == day:
                    ok = "\n"
                else:
                    ok = ""
                print(f"{i:>3d} ", end=ok)
        elif sday == "WED":
            print("            ", end="")
            for i in range(1, day+1):
                if i%7 == 4 or i == day:
                    ok = "\n"
                else:
                    ok = ""
                print(f"{i:>3d} ", end=ok)
        elif sday == "THU":
            print("                ", end="")
            for i in range(1, day+1):
                if i%7 == 3 or i == day:
                    ok = "\n"
                else:
                    ok = ""
                print(f"{i:>3d} ", end=ok)
        elif sday == "FRI":
            print("                    ", end="")
            for i in range(1, day+1):
                if i%7 == 2 or i == day:
                    ok = "\n"
                else:
                    ok = ""
                print(f"{i:>3d} ", end=ok)
        elif sday == "SAT":
            print("                        ", end="")
            for i in range(1, day+1):
                if i%7 == 1 or i == day:
                    ok = "\n"
                else:
                    ok = ""
                print(f"{i:>3d} ", end=ok)
        month = int(input("Month: "))
    """ do not touch below code """


if __name__ == "__main__":
    main()

