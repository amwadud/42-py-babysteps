def ft_water_reminder():
    age = int(input("Days since last watering: "))
    if age > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
