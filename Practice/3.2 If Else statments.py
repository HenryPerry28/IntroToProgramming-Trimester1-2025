#password = input("Password:\n >")
#pin = input("Password:\n >")
#
#if password == "Redapple25" and pin == "1025":
#    print("Phase 1 passed")
#    q1 = input("What is my first pets name?\n >")
#    q2 = input("What is the species of my first pet?\n >")
#    if q1 == "Zero" and q2 == "Dog" or "dog":
#        print("Phase 2 passed")
#else:
#    print("Access Denied")

def password_return():
    x = input("What is the password?\n >")
    if x == "help":
        print("Yes")
    else:
        print("No")
        password_return()

password_return()