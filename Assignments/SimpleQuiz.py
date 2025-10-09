q1 = input("What is the speed of an unladen swallow (in mph)?\n >") #29mph
q2 = input("How old was was George Boole when he died?\n >") #49
q3 = input("What is the sum of 999 and 999?\n >") #1998
q4 = input("What is the one number that is neither composite nor prime?\n >") #1
q5 = input("What is the definition of tomfoolery?\n >") #foolsih of silly behavior
q6 = input("What is the definition of bamboozle") #fool or cheat (someone)
q7 = input("What is the best color?\n >") #Dark forest green
q8 = input("What is the hex code for dark forest green?\n >") #228b22
q9 = input("Are you going to die?\n >") #no
q0 = input("Howold is my cat\n >") #7

score = 0

if q1.lower == "29mph" or "29 mph":
    print("Question 1 correct")
    score = score + 1
else:
    print("Question 1 wrong")

if q2.lower == "49" or "49 years":
    print("Question 2 correct")
    score = score + 1
else:
    print("Question 2 wrong")

if q3.lower == "1998":
    print("Question 3 correct")
    score = score + 1
else:
    print("Question 3 wrong")

if q4.lower == "1":
    print("Question 4 correct")
    score = score + 1
else:
    print("Question 4 wrong")
    
if q5.lower == "foolsih or silly behavior":
    print("Question 5 correct")
    score = score + 1
else:
    print("Question 5 wrong")

if q6.lower == "fool or cheat (someone)":
    print("Question 6 correct")
    score = score + 1
else:
    print("Question 6 wrong")

if q7.lower == "dark forest green":
    print("Question 7 correct")
    score = score + 1
else:
    print("Question 7 wrong")

if q8.lower == "228b22":
    print("Question 7 correct")
    score = score + 1
else:
    print("Question 7 wrong")

if q9.lower == "no":
    print("Question 7 correct")
    score = score + 1
else:
    print("Question 7 wrong")

if q0.lower == "7" or "7 years":
    print("Question 7 correct")
    score = score + 1
else:
    print("Question 7 wrong")

print(score) 
