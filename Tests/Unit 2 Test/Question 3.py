#Create a function called data_three that takes zero parameters. Inside of the function create three input statements that ask for a word, an integer, and a float. Add the integer and the float and then concatenate that sum with the word, then print.

def data_three():
    x = input("Word\n >")
    y = input("Integer\n >")
    z = input("Float\n >")
    t = (f" {float(y) + float(z)}")
    print(f"{(str(t))+x}")

data_three()