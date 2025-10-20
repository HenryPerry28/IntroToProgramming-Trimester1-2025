speed = input("What is the speed of the storm?\n >")
try:
    if int(speed) < 74:
        print("Tropical storm")
    elif int(speed) < 96:
        print("Category 1")
    elif int(speed) < 111:
        print("Category 2")
    elif int(speed) < 130:
        print("Category 3")
    elif int(speed) < 157:
        print("Category 4")
    elif int(speed) >= 157:
        print("Category 5")
except:
    print("NO")