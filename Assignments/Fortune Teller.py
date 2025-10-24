import random
def tellfortune():
     print("I will tell your fortune with only number, enter all as an integer, except the magical multiplier")
     q1 = input("What is your favorite number\n >")
     q2 = input("What is your age?\n >")
     q3 = input("What is the age of your pet, if none, put 0\n >")
     q4 = input("What is your unlucky integer\n >")
     q5 = input("Choose a magical multiplier\n >")
     global seed
     try:
        seed = int(q1 + q2 + q3 + q4) * float(q5)

        f0 = "You will own 20 cats."
        f1 = "You will live in a basement forever."
        f2 = "Your mother will perish tommorrow"
        f3 = "You will have a leg taken in a car crash."
        f4 = "You have no determinable future, you are unreadable"
        f5 = "You will have a standard American life."
        f6 = "You will move to Jamaica."
        f7 = "You die."
        f8 = "You will become the god of time."
        f9 = "You will invent time travel."

        random.seed(seed)
        randomchoice = (f0, f1, f2, f3, f4, f5, f6, f7, f8, f9)
        print(random.choice(randomchoice))
     except:
         print("Wrong")
         tellfortune()

tellfortune()