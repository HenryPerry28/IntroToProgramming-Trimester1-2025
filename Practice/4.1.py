'''
groccery_list = ["Apple", "Banana", "Milk", "Eggs", "Juice"]

store = [
#--------------------------------------------------------------#
    [
    [
    ["Bread", "Bagel", "Cereal", "Pasta", "Rice"],
    ["Chips", "Chocolate Bar", "Gummy Bears", "Gold Fish", "Pretzels"],
    ],
    [
    ["Apple", "Banana", "Coconut", "Lime", "Strawberry"], 
    ["Milk", "Yogurt", "Cheese", "Butter", "Ice Cream"],
    ],
    ],

    [
    [
    ["Clorox Wipes", "Window Cleaner", "Dish Soap", "Bleach", "Detergent"],
    ["Toothpaste", "Ibuprofen", "Melotonin", "Cleanex", "Fish Oils"],
    ],
    [
    ["Fizzy Water", "Soda", "Water", "Energy Drink", "Flavoured Water"], 
    ["Brussel Sprouts", "Kale", "Brocolli", "Carrots", "Spinach"],
    ],
    ],
]

print(store[1][0][0][2])

print(store[1])
'''

fav_fruit = ["Strawberry", "Blueberry", "Orange", "Mango", "Blackberry"]

print(fav_fruit)

print(fav_fruit[0]); print(fav_fruit[-1])

x = input("Add a fruit to your favorite fruit list\n> ").title()
fav_fruit.append(x)
print(fav_fruit)

while True:
    y = input("Remove a fruit from you favorite fruit list\n>")
    if not y in fav_fruit:
        print("Choose a fruit in the list")
        continue
    else:
        fav_fruit.remove(y)
        print(fav_fruit)
        break

fav_fruit.sort()

for item in fav_fruit:
    print(item)

y = fav_fruit.count("Strawberry")
print(y)

for _ in fav_fruit: print(a)