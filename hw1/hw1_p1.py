"""
Programming assignment # 1
- Problem 1: Plant watering
"""
def main():

    day = int(input("Passed days? "))
    num_cactus = int(input("Cactus watered time? "))
    num_tulip = int(input("Tulip watered time? "))

    """ implement here """
    if day <= 0:
        print("Wrong input")
    else:
        watering_plant = "None"
        Cactus_condition = "Healthy"
        Tulip_condition = "Healthy"
        if day%30==0:
            watering_plant = "Cactus, Tulip"
            if day//10-1<num_cactus:
                Cactus_condition = "Damp"
            elif day//10-1>num_cactus:
                Cactus_condition = "Dry"
            if day//3-1<num_tulip:
                Tulip_condition = "Damp"
            elif day//3-1>num_tulip:
                Tulip_condition = "Dry"
        elif day%10==0:
            watering_plant = "Cactus"
            if day // 10 - 1 < num_cactus:
                Cactus_condition = "Damp"
            elif day // 10 - 1 > num_cactus:
                Cactus_condition = "Dry"
            if day // 3 < num_tulip:
                Tulip_condition = "Damp"
            elif day // 3 > num_tulip:
                Tulip_condition = "Dry"
        elif day%3==0:
            watering_plant = "Cactus"
            if day // 10 < num_cactus:
                Cactus_condition = "Damp"
            elif day // 10 > num_cactus:
                Cactus_condition = "Dry"
            if day // 3-1 < num_tulip:
                Tulip_condition = "Damp"
            elif day // 3-1 > num_tulip:
                Tulip_condition = "Dry"
        else:
            if day // 10 < num_cactus:
                Cactus_condition = "Damp"
            elif day // 10 > num_cactus:
                Cactus_condition = "Dry"
            if day // 3 < num_tulip:
                Tulip_condition = "Damp"
            elif day // 3 > num_tulip:
                Tulip_condition = "Dry"
        print(f"Today watering plant? {watering_plant:s}")
        print(f"Cactus condition? {Cactus_condition:s}")
        print(f"Tulip condition? {Tulip_condition:s}")


    """ do not touch below code """


if __name__ == "__main__":
    main()

