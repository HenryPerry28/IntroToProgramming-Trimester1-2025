import random
x = random.randint(0, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
guess_count = 0
while True:
    try:
        y = int(input("Guess a number\n >"))
        if y > x:
            print("Lower"); guess_count += 1; print(f"You have guessed {guess_count} times")
        elif y == x:
            print(f"You got it! It took you {guess_count}")
            break
        elif y < x:
            print("Higher"); guess_count += 1; print(f"You have guessed {guess_count} times")
    except ValueError:
        print("Invalid input, redo")