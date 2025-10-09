file_name_exclusive = input("New file name:\n >")
content_exclusive = "This content is for an exclusively new file."

def multi_add():
    total = 0 
    while TRUE
        user_input = input("Enter numbers you want to add, with only spaces in between. Enter 'done' when done: ")
        if user_input.lower == "done"
            break
        try: 
            number = float(user_input)
            total += number
        except ValuError:
            print("Invalid input, type a valid number or 'done'.")
    print(f"The sum is {total}.")

def subtract():
    total = 0 
    while TRUE
        user_input = input("Enter numbers you want to subtract, with only spaces in between. Enter 'done' when done: ")
        if user_input.lower == "done"
            break
        try: 
            number = float(user_input)
            total -= number
        except ValuError:
            print("Invalid input, type a valid number or 'done'.")
    print(f"The difference is {total}.")

def multiply (x, y):
    total = 0 
    while TRUE
        user_input = input("Enter numbers you want to multiply, with only spaces in between. Enter 'done' when done: ")
        if user_input.lower == "done"
            break
        try: 
            number = float(user_input)
            total *= number
        except ValuError:
            print("Invalid input, type a valid number or 'done'.")
    print(f"The product is {total}.")

def divide(x, y):
    total = 0 
    while TRUE
        user_input = input("Enter numbers you want to divide, with only spaces in between. Enter 'done' when done: ")
        if user_input.lower == "done"
            break
        try: 
            number = float(user_input)
            total /= number
        except ValuError:
            print("Invalid input, type a valid number or 'done'.")
    print(f"The dividend is {total}")

def modulus(x, y):
    print(x % y)

def floordivide
    print(x // y)

def exponent(x, y):
    print(x**y)

def calculate_total(tprice, trate, titem):
    print(titem)
    print(f"Your total price is ${float(tprice) * (trate)}")

def calculate_tax(item, price, rate):
    print(item)
    print(f"Your tax is ${float(price) * (rate)}")

def calculator():
    calc_choice = input("Choose operation: ADDITION; SUBTRACTION; MULTIPLICATION; DIVISION; EXPONENTS; MODULUS; FLOOR DIVIDE\n >")
    num1_calc = float(input("x value\n >"))
    num2_calc = float(input("y value\n >"))
    if calc_choice == "ADDITION":
        add(num1_calc, num2_calc)
    if calc_choice == "SUBTRACTION":
        subtract(num1_calc, num2_calc)
    if calc_choice == "MULTIPLICATION":
        multiply(num1_calc, num2_calc)
    if calc_choice == "DIVISION":
        divide(num1_calc, num2_calc)
    if calc_choice == "EXPONENTS":
        exponent(num1_calc, num2_calc)
    if calc_choice == "MODULUS"
        floordivide(num1_calc, num2_calc):

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
    print("CALCULATOR; TAX; NOTES; SORT_LIST")
    place = input("What would you like to access?\n >")
    
    if place == "CALCULATOR"
        calculator():
        exit = input("Would you like to exit(YES or NO)?\n >")
        if exit == "YES"
        else:
            print("CALCULATOR; TAX; NOTES; SORTERS")
            place = input("What would you like to access?\n >")
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
        exit = input("Would you like to exit(YES or NO)?\n >")
        if exit == "YES"
        else:
            print("CALCULATOR; TAX; NOTES; SORTERS")
            place = input("What would you like to access?\n >")

    if place == "NOTES"
        file_name = "new_file.txt"
        content = "This is the content of the new file.\nIt includes multiple lines."
        with open(file_name, 'w') as f:
            f.write(content)
        print(f"File '{file_name}' created and content written successfully.")

        exit = input("Would you like to exit(YES or NO)?\n >")
        if exit == "YES"
        else:
            print("CALCULATOR; TAX; NOTES; SORTERS")
            place = input("What would you like to access?\n >")
    if place == "SORT_LIST"
        
        exit = input("Would you like to exit(YES or NO)?\n >")
        if exit == "YES"
        else:
            print("CALCULATOR; TAX; NOTES; SORTERS")
            place = input("What would you like to access?\n >")
