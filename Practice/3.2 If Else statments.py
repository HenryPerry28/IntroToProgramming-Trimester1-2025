def calculate_total(tprice, trate, titem):
    print(titem)
    print(f"Your total price is ${float(tprice) * (trate)}")

def calculate_tax(item, price, rate):
    print(item)
    print(f"Your tax is ${float(price) * (rate)}")

password = input("Password:\n >")
pin = input("Password:\n >")
def password_wall ():
    if password == "Redapple25" and pin == "2025":
        print("Phase 1 passed")
        q1 = input("What is my first pets name?\n >")
        q2 = input("What is the species of my first pet?\n >")
        if q1 == "Zero" and q2 == "Dog" or "dog":
            print("Phase 2 passed")
            q3 = input("What is the name of my favorite pet\n >")
            q4 = input("How old is my favorite pet\n >")
            if q3 == "Zen" and q4 == "7" or "7 years"
                print("ACCESS GRANTED")
                global enterance_key = 1
            else:
                print("ACCESS DENIED")
                global enterance_key = 2
        else: 
            print("ACCESS DENIED")
            global enterance_key = 2
    else:
    print("ACCESS DENIED")
    global enterance_key = 2

password_wall():

if enterance_key == 1
    print("CALCULATOR; TAX; NOTES; SORTERS")
    place = input("What would you like to access?\n >")
    
    if place == "CALCULATOR"
        calculator(x, y):
    if place == "TAX"
        type2 = input("Do you want TOTAL or just the price of TAX?\n >")
            if type2 = "TOTAL"
                titem = input("What is your item?\n >")
                tprice = input("What is the cost of your item?\n >")
                trate = 1.06875
                
                calculate_total(tprice, trate, titem)
            if type2 == "TAX"
                item = input("What is your item?\n >")
                price = input("What is the price of the item you are buying?\n >")
                rate = 0.06875
                calculate_tax(item, price, rate)
