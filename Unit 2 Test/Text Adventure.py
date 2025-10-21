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

def str_dex_calc():
    global dex_mod
    if dex_stat == 1:
        dex_mod = -5
    elif dex_stat == 2 or dex_stat == 3:
        dex_mod = -4
    elif dex_stat == 4 or dec_stat == 5:
        dex_mod = -3
    elif dex_stat == 6 or dex_stat == 7:
        dex_mod = -2
    elif dex_stat == 8 or dex_stat == 9:
        dex_mod = -1
    elif dex_stat == 10 or dex_stat == 11:
        dex_mod = 0
    elif dex_stat == 12 or dex_stat == 13:
        dex_mod = 1
    elif dex_stat == 14 or dex_stat == 15:
        dex_mod = 2
    elif dex_stat == 16 or dex_stat == 17:
        dex_mod = 3
    elif dex_stat == 18 or dex_stat == 19:
        dex_mod = 4
    elif dex_stat == 20:
        dex_mod = 5
    print(dex_mod)

def con_mod_calc():
    global con_mod
    if con_stat == 1:
        con_mod = -5
    elif con_stat == 2 or con_stat == 3:
        con_mod = -4
    elif con_stat == 4 or con_stat == 5:
        con_mod = -3
    elif con_stat == 6 or con_stat == 7:
        con_mod = -2
    elif con_stat == 8 or con_stat == 9:
        con_mod = -1
    elif con_stat == 10 or con_stat == 11:
        con_mod = 0
    elif con_stat == 12 or con_stat == 13:
        con_mod = 1
    elif con_stat == 14 or con_stat == 15:
        con_mod = 2
    elif con_stat == 16 or con_stat == 17:
        con_mod = 3
    elif con_stat == 18 or con_stat == 19:
        con_mod = 4
    elif con_stat == 20:
        con_mod = 5
    print(con_mod)

def wis_mod_calc():
    global wis_mod
    if wis_stat == 1:
        wis_mod = -5
    elif wis_stat == 2 or wis_stat == 3:
        wis_mod = -4
    elif wis_stat == 4 or wis_stat == 5:
        wis_mod = -3
    elif wis_stat == 6 or wis_stat == 7:
        wis_mod = -2
    elif wis_stat == 8 or wis_stat == 9:
        wis_mod = -1
    elif wis_stat == 10 or wis_stat == 11:
        wis_mod = 0
    elif wis_stat == 12 or wis_stat == 13:
        wis_mod = 1
    elif wis_stat == 14 or wis_stat == 15:
        wis_mod = 2
    elif wis_stat == 16 or wis_stat == 17:
        wis_mod = 3
    elif wis_stat == 18 or wis_stat == 19:
        wis_mod = 4
    elif wis_stat == 20:
        wis_mod = 5
    print(wis_mod)

def int_mod_calc():
    global int_mod
    if int_stat == 1:
        int_mod = -5
    elif int_stat == 2 or int_stat == 3:
        int_mod = -4
    elif int_stat == 4 or int_stat == 5:
        int_mod = -3
    elif int_stat == 6 or int_stat == 7:
        int_mod = -2
    elif int_stat == 8 or int_stat == 9:
        int_mod = -1
    elif int_stat == 10 or int_stat == 11:
        int_mod = 0
    elif int_stat == 12 or int_stat == 13:
        int_mod = 1
    elif int_stat == 14 or int_stat == 15:
        int_mod = 2
    elif int_stat == 16 or int_stat == 17:
        int_mod = 3
    elif int_stat == 18 or int_stat == 19:
        int_mod = 4
    elif int_stat == 20:
        int_mod = 5
    print(int_mod)

def cha_mod_calc():
    global cha_mod
    if cha_stat == 1:
        cha_mod = -5
    elif cha_stat == 2 or cha_stat == 3:
        cha_mod = -4
    elif cha_stat == 4 or cha_stat == 5:
        cha_mod = -3
    elif cha_stat == 6 or cha_stat == 7:
        cha_mod = -2
    elif cha_stat == 8 or cha_stat == 9:
        cha_mod = -1
    elif cha_stat == 10 or cha_stat == 11:
        cha_mod = 0
    elif cha_stat == 12 or cha_stat == 13:
        cha_mod = 1
    elif cha_stat == 14 or cha_stat == 15:
        cha_mod = 2
    elif cha_stat == 16 or cha_stat == 17:
        cha_mod = 3
    elif cha_stat == 18 or cha_stat == 19:
        cha_mod = 4
    elif cha_stat == 20:
        cha_mod = 5
    print(cha_mod)

def all_stats_assign():
    s1 = stat_calc()
    s2 = stat_calc()
    s3 = stat_calc()
    s4 = stat_calc()
    s5 = stat_calc()
    s6 = stat_calc()
    global all_stats_list
    rand_stats_list= [s1, s2, s3, s4, s5, s6]
    rand_stats_list.sort()
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
    player_stats_sorted_list = [str_stat, dex_stat, con_stat, wis_stat, int_stat, cha_stat]
    if player_stats_sorted_list == rand_stats_list:
        print("Right order")
    else:
        print("Wrong order")
    
all_stats_assign()

str_mod_calc()
