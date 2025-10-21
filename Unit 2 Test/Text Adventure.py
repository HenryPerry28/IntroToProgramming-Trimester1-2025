import random

print("You will be going on an adventure, you will have a choice of certain paths to take, to choose the path, enter the number related to the choice.")



def stat_calc():
    x = [(random.randint(1, 6)), (random.randint(1, 6)), (random.randint(1, 6)), (random.randint(1, 6))]
    y = min(x)
    x.remove (y)
    z = sum(x)
    print(z)


def str_mod_calc():
    global str_mod
    if str_stat == 1:
        str_mod = -5
    elif str_stat == 2 or str_stat == 3:
        str_mod = -4
    elif str_stat == 4 or str_stat == 5:
        str_mod = -3
    elif str_stat == 6 or str_stat == 7:
        str_mod = -2
    elif str_stat == 8 or str_stat == 9:
        str_mod = -1
    elif str_stat == 10 or str_stat == 11:
        str_mod = 0
    elif str_stat == 12 or str_stat == 13:
        str_mod = 1
    elif str_stat == 14 or str_stat == 15:
        str_mod = 2
    elif str_stat == 16 or str_stat == 17:
        str_mod = 3
    elif str_stat == 18 or str_stat == 19:
        str_mod = 4
    elif str_stat == 20:
        str_mod = 5
    print(str_mod)

def all_stats_assign():
    s1 = stat_calc()
    s2 = stat_calc()
    s3 = stat_calc()
    s4 = stat_calc()
    s5 = stat_calc()
    s6 = stat_calc()
    global all_stats_list
    all_stats_list= [s1, s2, s3, s4, s5, s6]
    print("Now assign all number to a stat.")
    global str_stat
    str_stat = int(input("What is your strength base number?\n >"))
    global dex_stat
    dex_stat = int(input("What is your dexterity base number?\n >"))
    global con_stat
    con_stat = int(input("What is your constitution base number?\n >"))
    global wis_stat
    wis_stat = int(input("What is your wisdom base number?\n >"))
    global int_stat
    int_stat = int(input("What is your intelligence base number?\n >"))
    global cha_stat
    cha_stat = int(input("What is your charisma base number?\n >"))

all_stats_assign()

str_mod_calc()