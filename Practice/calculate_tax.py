item = input("What is your item?\n >")
price = input("What is the price of the item you are buying?\n >")
rate = 0.06875

titem = input("What is your item?\n >")
tprice = input("What is the cost of your item?\n >")
trate = 1.06875

def calculate_total(tprice, trate, titem):
    print(titem)
    print(f"Your total price is ${float(tprice) * (trate)}")

def calculate_tax(item, price, rate):
    print(item)
    print(f"Your tax is ${float(price) * (rate)}")

calculate_tax(item, price, rate)
calculate_total(tprice, trate, titem)