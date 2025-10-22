import random

global gold, silver, copper
gold = 1
sliver = 7 
copper = 23

print("You will be going on an adventure, you will have a choice of certain paths to take, to choose the path, enter the number related to the choice.")

def roll_20():
    return random.randint(1, 20)
def roll_10():
    return random.randint(1, 10)
def roll_8():
    return random.randint(1, 8)
def roll_6
    return random.randint(1, 6)
def roll_4():
    return random.randint(1, 4)

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
    global class_choice
    print("It is now time to choose your class")
    print("Class options are: Fighter, Wizard, Rogue or Cleric.")
    all_classes = ["Fighter", "Wizard", "Rogue", "Cleric"]
    while True:
        class_choice = input("Choose a class\n > ").title()
        if not class_choice in all_classes:
            print("Choose one of the race options (an actual race)")
        else:
            break
    return class_choice

def class_key_decider():
    global class_key
    if class_choice == "Fighter":
        class_key = 1 
        print(class_key)
    elif class_choice == "Wizard":
        class_key = 2
        print(class_key)
    elif class_choice == "Rogue":
        class_key = 3
        print(class_key)
    elif class_choice == "Cleric
        class_key = 4
        print(class_key)
    return class_key

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
            print("Enter only the numbers given, you cheater!")
    except ValueError:
        print("Only integers, pal.")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

def orc_interaction():
    if s1_c2 == "1":
        if silver >= 10:
            print("He takes your money and says, 'Great, I never need to see you again.'")
            silver -= 10
            return silver
        elif (silver + (copper // 10)) >= silver_payment:
            global inn_payment
            inn_payment = 10
            if silver <= inn_payment:
                silver -= silver
                x = (inn_payment - silver); copper - (x * 10) 
            else:
                silver -= inn_payment
                print("He takes your money and saya, 'Great, now I never need to see you again'")
        else:
            print("'You don't have enough money, head to the bank if you wanna get that gold piece traded in for silver or copper.' He grunts.")
    elif s1_c2 == "2":
        print("I could lower the prices, but depends what's in it for me")
        bargain_roll1 = (roll_20() + cha_mod)
        if bargain_roll >= -5
            print("You didn't do nothing for me, so why should I cut you any slack, just figure out a way to get me the money.")
            orc_man_relation_npc -= 1
        elif bargain_roll >= 5
            print("I feel bad for you, but not enough to care, give me the money or go find it.")
            orc_man_relation_npc += 0
        elif bargain_roll >= 10
            print("Just cause I feel bad for such a weak and pathetic adventurer, I will give you 3 silver off")
            orc_man_relation_npc += 0
            inn_payment -= 3
        elif bargain_roll >= 15
            print("'You make a point, you suck at life, I'll give you 5 off, you failure.' He says laughing jovially")
            inn_payment -= 5; orc_man_relation_npc += 1
    elif s1_c2 == "3": 
        print("Good, find me by 12:00 today.")
        orc_man_relation_npc += 0
    elif s1_c2 == "4": 
        print("Okay pal, the size between me and you alone makes me way stronger".) 
        print("If you don't come up with the payments by 12:00, I'll find you with my squad.")
        orc_man_relation_npc -= 2

def story_start():
    print("You wake up on your bed in the The Firewater Inn, you had rented it for the week.")
    print("As you wake, their is a knock on your door.")
    while True:
        print("1. Answer the door")
        print("2. Tell them to come in")
        print("3. Ignore them")
        s1_c1 = input("Choice (remember input just the number)\n >")
        av_ch_s1_c1 = ["1", "2", "3"]
        if not s1_c1 in av_ch_s1_c1:
            print("Choose a valid choice")
        else:
            break
    if s1_c1 == "1":
        print("A large orcish man greets you, and says that payments is due today, and if you don't pay he will kick you out.")

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        orc_man_relation_npc = 0
        while True:
            print("What would you like to do?")
            print(f"1. Pay the 10 silver (Gold: {gold}, Silver: {silver}, Copper: {copper}")
            print("2. Discuss payment plans (barter)")
            print("3. Agree to pay later")
            print("4. Say you aren't paying, ever")
            s1_c2 = input("Choice\n >")
            av_ch_s1_c2 = ["1", "2", "3", "4"]
            if not s1_c2 in av_ch_s1_c2:
                print("Choose a valid choice (only the number)")
            else:
                break
        if s1_c2 == "1":
            if silver >= 10:
                print("He takes your money and says, 'Great, I never need to see you again.'")
                silver -= 10
                return silver
            elif (silver + (copper // 10)) >= silver_payment:
                global inn_payment
                inn_payment = 10
                if silver <= inn_payment:
                    silver -= silver
                    x = (inn_payment - silver); copper - (x * 10) 
                else:
                    silver -= inn_payment
                print("He takes your money and saya, 'Great, now I never need to see you again'")
            else:
                print("'You don't have enough money, head to the bank if you wanna get that gold piece traded in for silver or copper.' He grunts.")
        elif s1_c2 == "2":
            print("I could lower the prices, but depends what's in it for me")
            bargain_roll1 = (roll_20() + cha_mod)
            orc_man_relation_npc += 0
            if bargain_roll >= -5
                print("You didn't do nothing for me, so why should I cut you any slack, just figure out a way to get me the money.")
                orc_man_relation_npc -= 1
            elif bargain_roll >= 5
                print("I feel bad for you, but not enough to care, give me the money or go find it.")
                orc_man_relation_npc += 0
            elif bargain_roll >= 10
                print("Just cause I feel bad for such a weak and pathetic adventurer, I will give you 3 silver off")
                orc_man_relation_npc += 0
                inn_payment -= 3
            elif bargain_roll >= 15
                print("'You make a point, you suck at life, I'll give you 5 off, you failure.' He says laughing jovially")
                inn_payment -= 5; orc_man_relation_npc += 1
        elif s1_c2 == "3": 
                print("Good, find me by 12:00 today.")
                orc_man_relation_npc += 0
        elif s1_c2 == "4": 
                print("Okay pal, the size between me and you alone makes me way stronger".) 
                print("If you don't come up with the payments by 12:00, I'll find you with my squad.")
                orc_man_relation_npc -= 2
    elif s1_c1 == "2"
        print("A large orcish man opens a door, tells you that payments is due, and if you don't pay he will kick you out.")
        orc_man_relation_npc += 0
        

    elif s1_c1 == "3"
        print("'WAKE UP! Payment is due! I'm kicking you out if you don't pay by 12:00 today, and it's already 10:00.' Yells a large voice.")
        orc_man_relation_npc -= 1
        
    
race_selection()

all_stats_assign()

class_selction()

class_key_decider()
