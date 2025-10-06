def full_name(name1, name2):
    print(f"{name1}, {name2}")

def area_calculator(length, width):
    print(length * width)

def word_smash(word1, word2):
    print(str(word1) + str(word2))

def echo(string, integer):
    print(integer*(string))

def happy_birthday(name_happy):
    print(f"Happy birth day to you. Happy Birthday to you, Happy birth day dear {name_happy}, happy birthday to you.")

name_first = input("First name\n >")
name_last = input("Last name\n >")

length = 2

words_choice1 = input("First word\n >")
words_choice2 = input("Second word\n >")

full_name(name_first, name_last)

area_calculator(8, 7)
area_calculator(18, 13)

word_smash(words_choice1, words_choice2)

echo("hello", 5)

happy_birthday("Henry")