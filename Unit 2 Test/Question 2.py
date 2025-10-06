#Create a function called add_three that takes three parameters. Outside the function, use three input statements that ask for one integer each. Run add_three using those integers. add_three should print the sum of those integers.


def add_three(x, y, z):
    print(f"Sum: {int(x) + int(y) + int(z)}")

trate = input("First number: \n >")
tprice = input("Second number:\n >")
num3 = input("Third number:\n >")

add_three(trate, tprice, num3)
  
  
