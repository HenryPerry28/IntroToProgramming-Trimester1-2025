import random

games = ["Hollow Knight", "Avatar Frontiers Of Pandora", "Apex Legends", "Overwatch", "Slay the Spire"]

game_count = 1

x = input("List games one after the in order from best to worst\n> ")
while True:
    if not x in games:
        print("Not in")
        

for i in range(0, 5):
    print(f"Rank {i + 1}: {games[i]}")
y = []



'''for i in games: 
    print(i)
    print(game_count)
    game_count += 1'''
'''
for i in range(0, 100):
    z = (random.randint(-100, 100))
    if z > 0:
        y.append(str(z))
        
print(", ".join(y))
'''

'''
for i in range(10, 0, -1):
    print(i)

x = [10, 9, 123, 1, 9, 8, 7, 5, 5]
total = 0
for i in x:
    total += i    
print(total)
# Be better use this: print(sum(x))

for i in x: print(i*i)

string = input("Enter a string\n> ")
vowels = "aeiou"
vowel_count = 0
for i in string:
    if i in vowels:
        vowel_count += 1
print(vowel_count)

num = int(input("Input a number\n> "))
for i in range(1, 11): print(f"{num} * {i} = {i * (num)}")

names = ["Bob", "James", "Jogn Poep", "Jeremy"]
for name in names:
    print("Salutations {name}")
'''