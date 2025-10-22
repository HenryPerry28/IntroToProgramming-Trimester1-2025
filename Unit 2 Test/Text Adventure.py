import random

print("You will be going on an adventure, you will have a choice of certain paths to take, to choose the path, enter the number related to the choice.")

def race_selection():
    global final_race, race_choice
    print("The first step in your adventure is to choose your race")
    print("Race options are: Human, Elf, Dwarf or Tiefling.")
    all_races = ["Human", "Elf", "Dwarf", "Tiefling"]
    while True:
        race_choice = input("Choose a race\n > ").title()
        if not race_choice in all_races:
            print("Choose one of the race options (an actual race)")
        else:
            break
    final_race = subrace_selection() or race_choice
    print(f"Your final race is {final_race}")
    return final_race

def subrace_selection():
    if race_choice == "Elf":
        all_subraces = ["High Elf", "Wood elf", "Drow",]
        print("Elves have three different subraces: High elf, Wood elf, and Drow.")
    elif race_choice == "Dwarf":
        all_subraces = ["Mountain dwarf", "Hill dwarf"]
        print("Dwarfs have two different subraces: Hill dwarf and Mountain dwarf.")
    else:
        return None
    
    while True:
        final_subrace = input("Choose a subrace")
        if not final_subrace in all_subraces:
            print("Choose one of the options")
        else: 
            return final_subrace 
    
def race_stat_bonus():
    global str_stat, dex_stat, con_stat, wis_stat, int_stat, cha_stat
    if final_race == "Human":
        str_stat += 1; dex_stat += 1; con_stat += 1; wis_stat += 1; int_stat += 1; cha_stat += 1
    elif final_race == "High elf":
        dex_stat += 2; int_stat += 1
    elif final_race == "Wood elf":
        dex_stat += 2; wis_stat += 1
    elif final_race == "Drow":
        dex_stat += 2; cha_stat += 1
    elif final_race == "Hill dwarf":
        con_stat += 2; wis_stat += 1
    elif final_race == "Mountain dwarf":
        con_stat += 2; str_stat += 2
    elif final_race == "Tiefling":
        cha_stat += 2; int_stat += 1
    
def class_selction():
    global final_class, class_choice
    print("It is now time to choose your class")
    print("Class options are: Fighter, Wizard, Rouge or Cleric.")
    all_classes = ["Fighter", "Wizard", "Rouge", "Cleric"]
    while True:
        class_choice = input("Choose a class\n > ").title()
        if not class_choice in all_classes:
            print("Choose one of the race options (an actual race)")
        else:
            break
    final_class = subrace_selection() or class_choice
    print(f"Your final class is {final_class}")
    return final_class


def stat_calc():
    x = [(random.randint(1, 6)), (random.randint(1, 6)), (random.randint(1, 6)), (random.randint(1, 6))]
    y = min(x)
    x.remove (y)
    z = sum(x)
    print(z)
    return z

def str_mod_calc(str_stat):
    str_mod = (str_stat - 10) // 2
    print(f"Your strength modifier is: {str_mod}")

def dex_mod_calc(dex_stat):
    dex_mod = (dex_stat - 10) // 2
    print(f"Your dexterity modifier is: {dex_mod}")

def con_mod_calc(con_stat):
    con_mod = (con_stat - 10) // 2
    print(f"Your constitution modifier is: {con_mod}.")

def wis_mod_calc(wis_stat):
    wis_mod = (wis_stat - 10) // 2
    print(f"Your wisdom modifier is: {wis_mod}")

def int_mod_calc(int_stat):
    int_mod = (int_stat - 10) // 2
    print(f"Your intelligence modifier is: {int_mod}")

def cha_mod_calc(cha_stat):
    cha_mod = (cha_stat - 10) // 2
    print(f"Your charisma modifier is: {cha_mod}")

def all_stats_assign():
    try:
        s1 = stat_calc()
        s2 = stat_calc()
        s3 = stat_calc()
        s4 = stat_calc()
        s5 = stat_calc()
        s6 = stat_calc()
        print("Now assign all numbers to a stat.")
        global rand_stats_list
        rand_stats_list = [s1, s2, s3, s4, s5, s6]
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
        
        race_stat_bonus()

        if sorted(player_stats_sorted_list) == sorted(rand_stats_list):
            str_mod_calc(str_stat)
            dex_mod_calc(dex_stat)
            con_mod_calc(con_stat)
            wis_mod_calc(wis_stat)
            int_mod_calc(int_stat)
            cha_mod_calc(cha_stat)
        else:
            print("Enter only the numbers given, you bum!")
    except ValueError:
        print("Only integers, pal.")
    
race_selection()

all_stats_assign()

class_selction()
