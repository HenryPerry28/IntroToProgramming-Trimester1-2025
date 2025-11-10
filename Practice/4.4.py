import random

'''for i in range(21):
    if i == 15:
        print(i)
        break
    print(i)

for i in range(31):
    if i % 2 == 0:
        continue
    print(i)

for i in range(30):
    #Feature will print range(30) * 20,000 times, then reprint only the number 30
    pass

for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i)'''

x = [random.randint(-10, 10) for i in range(11)]
total = 0
for i in x:
    if i <= 0:
        break
    total += i
print(f"Total is: {total}")