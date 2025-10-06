def add(x, y):
    print(x + y)

def subtract(x, y):
    print(x - y)

def multiply (x, y):
    print(x * y)

def divide(x, y):
    print(x / y)

def exponent(x, y):
    print(x**y)

x = float(input("x value\n >"))
y = float(input("y value\n >"))

choice = input("Choose operation: Addition, Subtraction, Multiplication, Division, Exponents\n >")

if choice == "Addition":
    add(x, y)
if choice == "Subtraction":
    subtract(x, y)
if choice == "Multiplication":
    multiply(x, y)
if choice == "Division":
    divide(x, y)
if choice == "Exponents":
    exponent(x, y)