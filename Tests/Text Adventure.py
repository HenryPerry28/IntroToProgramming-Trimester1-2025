import random

print("You will be going on an adventure, you will have a choice of certain paths to take, to choose the path, enter the number related to the choice.")

av_weapons = ["Longsword", "Shortsword", "Dagger", "Heavy Crossbow", "Quarterstaff"]

player = {"Inventory": {}, 
          "Equipped": {}}

gold = 1
silver = 7 
copper = 23

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def equip_weapon_all():
    equip_weapon()
    add_weapon_from_inventory()

def add_weapon_from_inventory(quantity = 1):
    global equip_input
    equipped = player["Equipped"]
    if equip_input in equipped:
        print("Already equipped")
    else:
        equipped[equip_input] = quantity
        print(player["Equipped"])

def equip_weapon():
    global inventory, equip_input
    print(player["Equipped"])
    print(player["Inventory"])
    equip_input = input("What would you like to equip (you have to type out the full item name)?\n> ").title
    if equip_input in player["Inventory"]:
        while True:
            if not equip_input in av_weapons:
                print("Choose one of you weapons")
            else:
                print("IT WORKED")
    else:
        print("Invalid input")
        equip_weapon()


def attack(weapon):
    for item in inventory:
        print()
    weapon = input("")
    roll_damage(weapon)

# dice_type is entered as just the number for the kind of die (d8 = 8)
# amount_dice is the amout of dice rolled
def roll_damage(dice_type, amount_dice = 1):
    return sum(random.randint(1, dice_type) for _ in range(amount_dice))

def print_decide_inventory(item, quantity=1):
    global inventory
    inventory = player["Inventory"]
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def print_money ():
    print (f"Gold: {gold} Silver {silver} Copper: {copper}")

time = 0
num_list_2 = ["1", "2"]
num_list_3 = ["1", "2", "3"]
num_list_4 = ["1", "2", "3", "4"]
num_list_5 = ["1", "2", "3", "4", "5"]
num_list_6 = ["1", "2", "3", "4", "5", "6"]


def roll_20():
    r20 = random.randint(1, 20)
    return r20
def roll_10():
    r10 = random.randint(1, 10)
    return r10
def roll_8():
    r8 = random.randint(1, 8)
    return r8
def roll_6():
    r6 = random.randint(1, 6)
    return r6
def roll_4():
    r4 = random.randint(1, 4)
    return r4
def dashes():
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def race_selection():
    global final_race, race_choice
    print("The first step in your adventure is to choose your race")
    print("Race options are: Human, Elf, Dwarf or Tiefling.")
    all_races = ["Human", "Elf", "Dwarf", "Tiefling"]
    while True:
        race_choice = input("Choose a race\n > ").title()
        if not race_choice in all_races:
            print("Choose one of the race options")
        else:
            print(f"Your final race is {race_choice}")
            break
    final_race = subrace_selection() or race_choice
    return final_race

def subrace_selection():
    if race_choice == "Elf":
        all_subraces = ["High Elf", "Wood Elf", "Drow",]
        print("Elves have three different subraces: High elf, Wood elf, and Drow.")
    elif race_choice == "Dwarf":
        all_subraces = ["Mountain Dwarf", "Hill Dwarf"]
        print("Dwarfs have two different subraces: Hill dwarf and Mountain dwarf.")
    else:
        class_selction()
        return None
    while True:
        final_subrace = input("Choose a subrace\n >").title()
        if not final_subrace in all_subraces:
            print("Choose one of the options")
        else: 
            print(f"Your final race is {final_subrace}")
            class_selction()
            return final_subrace

def race_stat_bonus():
    global str_stat, dex_stat, con_stat, wis_stat, int_stat, cha_stat
    if final_race == "Human":
        str_stat += 1; dex_stat += 1; con_stat += 1; wis_stat += 1; int_stat += 1; cha_stat += 1
    elif final_race == "High Elf":
        dex_stat += 2; int_stat += 1
    elif final_race == "Wood Elf":
        dex_stat += 2; wis_stat += 1
    elif final_race == "Drow":
        dex_stat += 2; cha_stat += 1
    elif final_race == "Hill Dwarf":
        con_stat += 2; wis_stat += 1
    elif final_race == "Mountain Dwarf":
        con_stat += 2; str_stat += 2
    elif final_race == "Tiefling":
        cha_stat += 2; int_stat += 1
    
def class_selction():
    global class_choice
    dashes()
    print("It is now time to choose your class")
    print("Class options are: Fighter, Wizard, Rogue or Cleric.")
    all_classes = ["Fighter", "Wizard", "Rogue", "Cleric"]
    while True:
        class_choice = input("Choose a class\n > ").title()
        if not class_choice in all_classes:
            print("Choose one of the class options")
        else:
            class_key_decider()
            break

def class_key_decider():
    global class_key
    if class_choice == "Fighter":
        class_key = "f" 
    elif class_choice == "Wizard":
        class_key = "w"
    elif class_choice == "Rogue":
        class_key = "r"
    elif class_choice == "Cleric":
        class_key = "c"
    return class_key

def class_stuff_decider():
    if class_key == "f":
        print_decide_inventory("Longsword", 1)
        print_decide_inventory("Chain Mail", 1)
        print_decide_inventory("Healing Potion", 2)
        print(player)
    elif class_key == "w":
        print("You will choose what item you want out of the options (all are different scrolls, can cast for free)")
        scroll = input("What scroll do you want: Fligt, Misty Step (teleportation), Fireball, or Chromatic Orb\n> ")
        print_decide_inventory("Quarter-staff", 1)
        print_decide_inventory("Padded Armor", 1)
        print_decide_inventory(f"{scroll}", 1)
    elif class_key == "r":
        print_decide_inventory("Daggers", 2)
        print_decide_inventory("Padded Armor", 1)
        print_decide_inventory("Smoke Bomb", 2)
    elif class_key == "c":
        print_decide_inventory("Holy Symbol (Auto-crit on any roll)", 1)
        print_decide_inventory("Hide Armor", 1)
        print_decide_inventory("Mace", 1)
    #print(player)

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
    return str_mod

def dex_mod_calc(dex_stat):
    dex_mod = (dex_stat - 10) // 2
    print(f"Your dexterity modifier is: {dex_mod}")
    return dex_mod

def con_mod_calc(con_stat):
    con_mod = (con_stat - 10) // 2
    print(f"Your constitution modifier is: {con_mod}.")
    return con_mod

def wis_mod_calc(wis_stat):
    wis_mod = (wis_stat - 10) // 2
    print(f"Your wisdom modifier is: {wis_mod}")
    return wis_mod

def int_mod_calc(int_stat):
    int_mod = (int_stat - 10) // 2
    print(f"Your intelligence modifier is: {int_mod}")
    return int_mod

def cha_mod_calc(cha_stat):
    cha_mod = (cha_stat - 10) // 2
    print(f"Your charisma modifier is: {cha_mod}")
    return cha_mod

def all_stats_assign():
    try:
        s1 = stat_calc()
        s2 = stat_calc()
        s3 = stat_calc()
        s4 = stat_calc()
        s5 = stat_calc()
        s6 = stat_calc()
        dashes()
        print("Now assign all numbers to a stat.")
        global rand_stats_list
        rand_stats_list = [s1, s2, s3, s4, s5, s6]
        global str_stat
        str_stat = int(input("What is your strength base number?\n > "))
        global dex_stat
        dex_stat = int(input("What is your dexterity base number?\n > "))
        global con_stat
        con_stat = int(input("What is your constitution base number?\n > "))
        global wis_stat
        wis_stat = int(input("What is your wisdom base number?\n > "))
        global int_stat
        int_stat = int(input("What is your intelligence base number?\n > "))
        global cha_stat
        cha_stat = int(input("What is your charisma base number?\n > "))
        player_stats_sorted_list = [str_stat, dex_stat, con_stat, wis_stat, int_stat, cha_stat]
        race_stat_bonus()
        dashes()
        if sorted(player_stats_sorted_list) == sorted(rand_stats_list):
            global str_mod, dex_mod, con_mod, wis_mod, int_mod, cha_mod
            dashes()
            print(f"Your final strengh stat is: {str_stat}")
            print(f"Your final dexterity stat is: {dex_stat}")
            print(f"Your final constition stat is: {con_stat}")
            print(f"Your final wisdom stat is: {wis_stat}")
            print(f"Your final intelligence stat is: {int_stat}")
            print(f"Your final charsima stat is: {cha_stat}")
            dashes()
            str_mod = str_mod_calc(str_stat)
            dex_mod = dex_mod_calc(dex_stat)
            con_mod = con_mod_calc(con_stat)
            wis_mod = wis_mod_calc(wis_stat)
            int_mod = int_mod_calc(int_stat)
            cha_mod = cha_mod_calc(cha_stat)        
        else:
            print("Enter only the numbers given, you cheater!")
            all_stats_assign()
    except ValueError:
        print("Only integers, pal.")
        all_stats_assign()
    return s1, s2, s3, s4, s5, s6 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def town1_map():
    print()
    global town_location
    print("Locations:")
    print("> 1. City hall")
    print("> 2. Shopping district")
    print("> 3. The Firewater Inn")
    print("> 4. Town Center")
    av_tl = ["1", "2", "3", "4"]
    town_location = input("Where would you like to go?\n > ")
    while True:
        if not town_location in av_tl:
            print("Input just the number")
            town1_map()
        else:
            dashes()
            if town_location == "1":
                toha_location()
                return town_location 
            elif town_location == "2":
                shop_dist_location()
                return town_location
            elif town_location == "3":
                pass
                return town_location
            elif town_location == "4":
                return town_location
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def toha_location ():
    global npc_toha_interation_cho, guild_clerk_name, adventurer_name
    adventurer_name = "A local adventurer"
    guild_clerk_name = "The guild clerk"
    if town_location == "1":
        print("You have arrived in city hall, there are only 3 people of intrest.")
        print("> 1. Talk to the mayor")
        print(f"> 2. Talk to the {guild_clerk_name}")
        print(f"> 3. Talk to the {adventurer_name}")
        print("> 4. Leave")
        npc_toha_interation_cho = input("What would you like to do?\n >")
        av_npc_toha_interations = ["1", "2", "3", "4"]
        av_desc_of_npc_toha_y_or_no = ["1", "2"]
        while True:
            if not npc_toha_interation_cho in av_npc_toha_interations:
                print("please stop")
                toha_location()
            else:
                if npc_toha_interation_cho == "4":
                    town1_map()
                else:
                    print("Would you like a description of each (yes or no)?")
                    print("> 1. Yes")
                    print("> 2. No")
                    desc_npc_toha = input("Choice\n> ")
                    if not desc_npc_toha in av_desc_of_npc_toha_y_or_no:
                        print("Choose just the number")
                        toha_location()
                    else:
                        if desc_npc_toha == "1":
                            dashes()
                            print("The mayor is a big advocate for adventures, beacuse you are one is the only reason you could approach him.")
                            print("The guild clerk is responsible for managing the quest board, and is a representative from the 'Blazing Sun' guild")
                            print("The local adventurer is another adventurer like yourself (duh), but he is hoping to join the 'Blazing Sun' guild")
                            dashes()
                        else:
                            a_toha_npc_interactions()
                            while True:
                                dashes()
                                npc_toha_interation_cho = input("Choice\n> ")
                                if not npc_toha_interation_cho in av_npc_toha_interations:
                                    print("Choose just the number(at his point of tired of reminding you)")
                                    toha_location()
                                else:    
                                    a_toha_npc_interactions()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #    
def a_toha_npc_interactions():
    global guild_clerk_name, adventurer_name, name_signature, gold, guild_status
    av_guild_status_y_or_n = ["1", "2"]
    if npc_toha_interation_cho == "1":
        dashes()
        print("You walk up to the mayor, and start a chat")
        print("'Oh thank you mighty adventurer (take in mind your level 1) for you service, it means the world to me that you would spend time in such a small town!'")
        print("'Here, take this!' and the mayor gives you 2 gold pieces.")
        gold += 2
        toha_location()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #    
    elif npc_toha_interation_cho == "2":
        dashes()
        print("You walk up to the guild clerk")
        guild_clerk_name = "Eldric Varnell"
        while True:
            print("'Hello, my name is Eldric Varnell, I see that you must be an adventurer (based off of you gear), are you looking to join the guild?'")
            print("> 1. Yes")
            print("> 2. No")
            guild_status = input("Choice\n> ")
            if not guild_status in av_guild_status_y_or_n:
                print("Really, please, I'm tired of putting in this line of code.")
                a_toha_npc_interactions()
                return guild_clerk_name
            else:
                if guild_status == "1":
                    dashes()
                    print("Great, I will get the set up in a couple of days, I just need you to sign here")
                    name_signature = input("Write your signature here (don't do anything dumb)\n > ")
                    if "6" and "7" in name_signature:
                        print("You die of cringe for putting '67' in your name")
                        exit()
                    elif "six" and "seven" in name_signature:
                        print("You die of cringe for putting '67' in your name")                        
                        exit()
                    elif "sixty" and "seven" in name_signature:
                        print("You die of cringe for putting '67' in your name")
                        exit()
                    print("Great, like I said, I'll get back to you in a couple of days.")
                    toha_location()
                elif guild_status == "2":
                    dashes()
                    print("Bummer, I think you would have been a great fit")
                    toha_location()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    elif npc_toha_interation_cho == "3":
        dashes()
        adventurer_name = "George [Lurk] Lark"
        print("You walk up to the local adventurer, and he greets you with a kind smile")
        print("'Why hello there, it's nice to see another adventurer in this town, sorry to be rude, my name is George, George Lark, but some call me George lurk, I'm a rogue.'")
        av_join_guild_y_or_no = ["1", "2"]
        print("Anyway I was just signing up to join the 'Blazing Guild', how about you?")
        while True:
            print("> 1. Yes")
            print("> 2. No")
            join_guild_y_or_n = input("Choice\n> ")
            if not join_guild_y_or_n in av_join_guild_y_or_no:
                print("Dude stop, I'm still putting them in for every option.")
            else:
                if join_guild_y_or_n == "1":
                    dashes()
                    print("Cool, I guess I'll see you around.")
                    toha_location()
                elif join_guild_y_or_n == "2":
                    dashes()
                    print("Lame, well I might see you around?")
                    toha_location()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def shop_dist_location():
    global shop_location, inventory, gold, silver, copper, time
    if town_location == "2":
        dashes()
        print("You have entered the shopping district")
        print("There are four different shops in this area")
        print("> 1. The blacksmith (Doused in Flame)")
        print("> 2. The armorer (Steel Driven)")
        print("> 3. The general store (Grampy's Goods)")
        print("> 4. The restaurant (Steamin' Pie)")
        print("> 5. The Bank (that's its name)")
        print("> 6. Leave")
        print(f"> Gold: {gold} Silver: {silver} Copper: {copper}")
        print(f"Inventory: {inventory}")
        shop_location = input("Where would you like to go?\n> ")
        while True:
            if not shop_location in num_list_6:
                print("Why")
                shop_dist_location()
            else:
                if shop_location == "1":
                    dashes()
                    print("You have chosen to head to Doused in Flame, upon entering you see a small halfling behind the counter")
                    print("'Welcome in adventurer, my name is Dorin, I assume you come in for new weapons, if not I recomend you leave.'")
                    print("'Otherwise here are my wares!'")
                    shop_dist_npc_interactions()
                elif shop_location == "2":
                    dashes()
                    print("You have chosen to had to Steel Driven, upon entering you see a tall human hammering away at a piece of metal.")
                    print("'Hey, my name is Brom! Good to see a hero that will buy my wares, if you have the money anyway, I know the quests don't pay well.'")
                    print("Any who, you need anything from my stock?")
                    shop_dist_npc_interactions()
                elif shop_location == "3":
                    dashes()
                    print("You have chosen ")
                    print("Hello there young lad, nice to see a young face around here.")
                    print("I don't have a lot but if you want to see it anyway, feel free to take a look.")
                    shop_dist_location()
                elif shop_location == "4":
                    dashes()
                    print("You have chosen to head into the Steaming Pie, upon entering there is a chipper high elf waiting to sit you at a table.")                    
                    print("Hey there! Coming to look for some food, or our world renown pie (not actually, they just say it is)")
                    print("Here, take a look at our menu (food can heal you during combat) or, if you want something more practical to head to our shop out the back.")
                    shop_dist_location()
                elif shop_location == "5":
                    dashes()
                    print("You head to the bank, where you can take out a loan or get money exchanged, upon entering, you see a lithe Drow standing at a counter")
                    print("'How are you doing, my name is Viren. I will help you with any amount of currency exchanging you need to do'")
                    print("'If you need to take out a loan, go talk to Rurik (he points to a dwarf in the corner).'")
                    shop_dist_npc_interactions()
                elif shop_location == "6":
                    dashes()
                    print("You decide there is nothing helpful here at the moment, so you head back to onto the street")
                    town1_map()
                    
def shop_dist_npc_interactions():
    global gold, silver, copper, inventory
    if shop_location == "1":
        while True:
            dashes()
            print(f"Would you like to browse Dorin's wares(Gold: {gold} Silver: {silver}) Copper: {copper})")
            print("> 1. Yes")
            print("> 2. No (leave)")
            blacksmith_y_or_n = input("\n> ")
            if not blacksmith_y_or_n in num_list_2:
                print("STOP")
                shop_dist_npc_interactions()
            else:
                # if time >= 1 
                    #print(d)
                if blacksmith_y_or_n == "1":
                    dashes()
                    print("Dorin's Wares")
                    print("> 1. A shortsword (1 silver)")
                    print("> 2. A pair of daggers (5 copper)")
                    print("> 3. A heavy crossbow (20 bolts included)(1gp)")
                    print("> 4. 20 Climbing Spikes (3 copper)")
                    print("> 5. None (leave)")
                    blacksmith_purchase = input("What would you like to buy?\n> ")
                    while True:
                        if not blacksmith_purchase in num_list_5:
                            print("...")
                        else:
                            if blacksmith_purchase == "1":
                                if silver >= 1:
                                    silver -= 1
                                    dashes()
                                    print_decide_inventory("Shortsword", 1)
                                    print_money()
                                    print("Anything else?")
                                    shop_dist_npc_interactions()

                                elif (copper// 10) >= 1:
                                    copper -= 10
                                    dashes()
                                    print_money()
                                    print_decide_inventory("Shortsword", 1)
                                    print("Anything else?")
                                    shop_dist_npc_interactions()
                                else:
                                    print("You don't have enough money to purchase this item")
                                    shop_dist_npc_interactions()
                            elif blacksmith_purchase == "2":
                                if copper >= 5:
                                    copper -= 5
                                    dashes()
                                    print_money()
                                    print_decide_inventory("Daggers")
                                    print("Anything else?")
                                    shop_dist_npc_interactions()
                                else:
                                    print("You don't have enough copper to purchase this item, if you have silver you can turn it into copper at The Bank.")
                                    shop_dist_npc_interactions()
                            elif blacksmith_purchase == "3":
                                if gold >= 1:
                                    gold -= 1
                                    dashes()
                                    print_money()
                                    print_decide_inventory("Heavy Crossbow", 1)
                                    print("Anything else?")
                                    shop_dist_npc_interactions()
                                elif silver >= 10:
                                    silver -= 10
                                    dashes()
                                    print_money()
                                    print_decide_inventory("Heavy Crossbow", 1)
                                    print("Anything else?")
                                    shop_dist_npc_interactions()
                                elif silver + (copper//10) >= 10:
                                    silver -= silver
                                    hc_s_shop_payment = 10
                                    hc_s_shop_payment -= silver
                                    copper -= hc_s_shop_payment
                                elif copper >= 100:
                                    copper -= 100
                                    dashes()
                                    print("Why do you have so much copper?")
                                    print_money()
                                    print_decide_inventory("Heavy Crossbow", 1)
                                    print("Anything else")
                                    shop_dist_npc_interactions()
                                else:
                                    print("Your broke, but would you like to buy anything else?")
                                    shop_dist_npc_interactions()
                            elif blacksmith_purchase == "4":
                                if copper >= 3:
                                    copper -= copper
                                    dashes()
                                    print_money()
                                    print_decide_inventory("Climbing Spikes", 20)
                                    print("Anything else?")
                                    shop_dist_npc_interactions()
                                else:
                                    print("Your broke and have nothing")
                                    shop_dist_npc_interactions()
                elif blacksmith_y_or_n == "2":
                    if gold < 1:
                        print("You realize that you're broke and can't buy anything anway so you head outside")
                        shop_dist_location()
                    else:
                        print("There is nothing of interest in Dorin's stock so you leave")
                        shop_dist_location()
    if shop_location == "2":
        dashes()
        while True:
            print("")
            dashes()
            print(f"Would you like to browse Brom's wares (Gold: {gold} Silver: {silver}) Copper: {copper})")
            print("> 1. Yes")
            print("> 2. No (leave)")
            armor_y_or_n = input("Choice\n>")
            if not armor_y_or_n in num_list_2:
                print("PLEAASE")
                shop_dist_npc_interactions()
            else:
                if armor_y_or_n == "1":
                    print("Brom's Wares:")
                    print("> 1. Leather Armor (light; 3 silver)")
                    print("> 2. Scale Mail (medium; 8 silver)")
                    print("> 3. Chain Mail(heavy; 1 gold)")
                    print("> 4. Steel Sheild (off hand; 5 silver)")
                    buy_armor = input("What would you like to buy?\n> ")
                    if buy_armor == "1":
                        if silver >= 3:

                            print("")
                if armor_y_or_n == "2":
                    print("You decide that nothing here is worth it")
                    shop_dist_location()


def orc_interaction():
    global inn_payment_t_or_f, orc_return_y_or_n, s0_c1, orc_man_relation_npc, gold, silver, copper, inn_payment
    orc_man_relation_npc = 0
    if s0_c1 == "1":
        if silver >= 10:
            print("He takes your money and says, 'Great, I never need to see you again.'")
            silver -= 10
            town1_map()
            return silver
        elif (silver + (copper // 10)) >= inn_payment:
            if silver <= inn_payment:
                silver -= silver
                x = (inn_payment - silver); copper -= (x * 10) 
            else:
                silver -= inn_payment
            print("He takes your money and says, 'Great, now I never need to see you again'")
            inn_payment_t_or_f = "t"
            town1_map()
        else:
            print("'You don't have enough money, head to the bank (in the shopping district) if you wanna get that gold piece traded in for silver or copper.'")
            inn_payment_t_or_f = "f"
            av_orc_re_y_or_n = ["1", "2"]
            print("Would you like to keep talking to the orc")
            print("> 1. Yes")
            print("> 2. No")
            while True:
                orc_return_y_or_n = input("Choice\n > ")
                if not orc_return_y_or_n in av_orc_re_y_or_n:
                    print("Please stop (or you actually messed up on this one, if so, it's only the number)")
                    orc_interaction()
                else:
                    if orc_return_y_or_n == "1":
                        orc_interaction()
                    elif orc_return_y_or_n == "2":
                        print("You decide that you would like to head into town to aquire some money.")
                        town1_map()
    elif s0_c2 == "2":
        dashes()
        print("'I could lower the prices, but depends what's in it for me.'")
        bargain_roll1 = (roll_20() + cha_mod)
        orc_man_relation_npc += 0
        if bargain_roll1 <= -5:
            print("'You didn't do nothing for me, so why should I cut you any slack, just go figure out a way to get me the money.'")
            town1_map()
            orc_man_relation_npc -= 1
        elif bargain_roll1 <= 10:
            print("'Just cause I feel bad for such a weak and pathetic adventurer, I will give you 3 silver off, find me later, I have something to do.'")
            orc_man_relation_npc += 0
            inn_payment -= 3
            town1_map()
        elif bargain_roll1 <= 15:
            print("'You make a point, you suck at life, I'll give you 5 off, you failure.' He says laughs 'Oh, and find me later to actually pay'")
            inn_payment -= 5; orc_man_relation_npc += 1
            town1_map()
    elif s0_c2 == "3": 
        print("Good, find me by 12:00 today.")
        orc_man_relation_npc += 0
        town1_map()
    elif s0_c2 == "4": 
        print("Okay pal, the size between me and you alone makes me way stronger.") 
        print("If you don't come up with the payments by 12:00, I'll find you with my squad.")
        orc_man_relation_npc -= 2

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def s0():
    global orc_man_relation_npc, gold, silver, copper, s0_c1, s0_c2, inn_payment_t_or_f, inn_payment
    orc_man_relation_npc = 0
    inn_payment = 10
    print("You wake up on your bed in the The Firewater Inn, you had rented it for the week.")
    print("As you wake, their is a knock on your door.")
    while True:
        print("1. Answer the door")
        print("2. Tell them to come in")
        print("3. Ignore them")
        s0_c1 = input("Choice (remember input just the number)\n > ")
        av_ch_s0_c1 = ["1", "2", "3"]
        if not s0_c1 in av_ch_s0_c1:
            print("Choose a valid choice")
        else:
            break

#111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111#

    if s0_c1 == "1":
        dashes()
        print("A large orcish man greets you, and says that payments is due today, and if you don't pay he will kick you out.")
        while True:
            print("What would you like to do?")
            print(f"1. Pay the 10 silver (Gold: {gold}, Silver: {silver}, Copper: {copper})")
            print("2. Discuss payment plans (barter)")
            print("3. Agree to pay later")
            print("4. Say you aren't paying, ever")
            s0_c2 = input("Choice\n > ")
            av_ch_s0_c2 = ["1", "2", "3", "4"]
            if not s0_c2 in av_ch_s0_c2:
                print("Choose a valid choice (only the number)")
            else:
                orc_interaction()
        

#222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222#

    elif s0_c1 == "2":
        dashes()
        print("A large orcish man opens the door, and tells you that payments is due, and if you don't pay he will kick you out.")
        orc_man_relation_npc += 0
        while True:
            print("What would you like to do?")
            print(f"1. Pay the 10 silver (Gold: {gold}, Silver: {silver}, Copper: {copper}")
            print("2. Discuss payment plans (barter)")
            print("3. Agree to pay later")
            print("4. Say you aren't paying, ever")
            s0_c2 = input("Choice\n > ")
            av_ch_s0_c2 = ["1", "2", "3", "4"]
            if not s0_c2 in av_ch_s0_c2:
                print("Choose a valid choice (only the number)")
            else:
                orc_interaction()
    
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333#
    
    elif s0_c1 == "3":
        dashes()
        print("'WAKE UP! Payment is due! I'm kicking you out if you don't pay by 12:00 today, and it's already 10:00.' Yells a large voice.")
        orc_man_relation_npc -= 1
        
        av_follow_orc_man_y_or_n = ["1", "2"]
        print("You hear footsteps receeding down the hall.")
        print("Would you like to follow them or head into town?")
        print("> 1. Yes")
        print("> 2. Into town")
        follow_orc_man_y_or_n = input("Choice\n >")
        if not follow_orc_man_y_or_n in av_follow_orc_man_y_or_n:
            print("Please just stop")
        else: 
            if follow_orc_man_y_or_n == "1":
                print("You run out of your room to see a large orc man storming down the stairs")
                print("He hears you and says, 'Go away, but get me your payment later'")
                print("He looks angry so you take his words serioulsy, and head into town")
                town1_map()
            elif follow_orc_man_y_or_n == "2":
                print("You decide that angering such a large person is not a good idea, and so you head into town")
                town1_map()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def s1():
    if town_location == "":
        print("Where would you like to go")
def attack_goblin():
    #print("""
    #                .             
    #            : .-             
    #           :#%#:             
    #           -##+*+            
    #           +*%##             
    #            #@#              
    #            #-               
    #           #%+               
    #           *=                
    #          -*  =++ -%%+*.     
    #          #     -#+*-+::-    
    #         #=   :-=-*#+-+=+    
    #       .:+:  .  *@%%*+-==    
    #       .+%* : =-===*#+**:    
    #       :%@@  .-:--=+#%@*.    
    #      :*@@@# ===::-+#@@@#    
    #     .:#=@@%*#*+::--+%@%#=   
    #      *= %@@#%@#*-==*%@%+%#: 
    #     :-:  *@%+-+*+*+-+=:==%* 
    #    . :   .:-  -#*#+=#%%%%#%.
    #    .     =   .+**%%%@@+%#%-.
    #              :**%%%##.=+=-: 
    #            .-*#++*%%%+      
    #              *%*%+=%%%      
    #              -#%*=-+%%      
    #               @-*==+%%:     
    #               : %**###:     
    #                ##%*@#%      
    #               =%%%@%#.      
    #               @%%@@%-       
    #              +++#@%%%       
    #             :%%%**#%#       
    #             .:*++-=.        
    #                --=--        
    #__________________________________
    #       -------------------- 
    #       |      HP: 0/0     | 
    #       --------------------
#""")
    if class_key == "f":
        print("""
                                                         
                       +%.           
                      :@#%           
                 +=%**-=*%           
                  *%# %*#@:          
                  +# #%#%@%=         
                   . #%%%%*#*        
                    %#*%+#*##:       
                    #%*+#*%%%%       
                   .*%+***@%@%++     
                   =##**##@+*#+%%.   
                   @@+**%%@+##%##%   
                  -#@+*#%%*%%%#*%#.  
                  =#+@##@%+%#%#%%%-  
                  #% ###@%#%%##%%%@  
                  %%+#%%@%%%%%#%%@@  
                 -**%#@%%@@%%#%%@%%  
                  #*%%%@@%@@%@%%%@%  
                  # %%@@@%@#%%@@@@%  
                 =.:*#%@@%%@%@@@@*-  
                 * @%%%@%%@@%%%@=.   
                :: @%*%@@#%@@@%      
                # -@#%@@@@@@@@#*     
               .* #@@%@@@@@@%@+*     
               *  #@@%@@-.@@@@@      
              .*  =+ %%   @@@@       
              -      %+   @*@#       
              =     @%+   :-@@:      
             .     :#%*-----@%%---:  
               ...-%%@=------@@---   
                  :=:.    .:-@%      
        ___________________________________ 

-------------------- ---------------------------------
|      HP: 0/0      | Attacks: Abilities: Inventory: |
-------------------- ---------------------------------
          """),

    elif class_key == "w":
        print("""                 
                  -                  
                  +                  
                 :*                  
                *:#=+===             
                +-**.#***     .      
                 -**.#*#%:    ..     
                  -#+#*=#-    .:     
                  :#**#-##    -.     
                   +***=*#    . .    
                  :==*++*%=  ..=:    
                 .*-*++####: :=.     
                 =+=*%=+%*%%.=:      
                 #*##%+*#%@*#*       
                 #*%%@%@@@@*%@+      
                 +%@%@@@%@@%@@%=     
                 #%%%#@@@@@%%%%%     
                .#%*%*%%@@@@@%%%*    
                +###%@#%%@@@@#-:=-   
                +#%%+@#%%@@@@%%*.    
                *#%#+@#%%@@@@@%%%    
                *###*%*#%@@@@@%%%%.  
                ####*%##%@@%@@@%#%%  
                %%%##%###%@%@@@%   . 
                %#%%#%@#+%@@%@@@-    
                ###@%%@#+#%%%@@%#    
                *##@%%@##*#@#@@@%:   
                ####%%@+**#@#%@@@@   
                @@@@@@@***#%@%@@+    
                %@@@@@@##*##@%+      
                #%%@@@@#######-      
                *%%@+@@#####.=.      
                 #%%:@-+#%+:         
                  %#   *@#@+         
                 +%+     -..         
                 .:                     
        __________________________________

-------------------- ---------------------------------
|      HP: 0/0      | Attacks: Abilities: Inventory: |
-------------------- ---------------------------------

"""),
    elif class_key == "r":
        print("""

                                 :.      
                                **+      
                               %#+#.     
                              .#%##+     
                             :*%*+%=  *  
                           *=#%%+=#* **  
                          ##*#+-#***-=.  
                          %#*#*-#+=**=   
                          %%%**=##*#++   
                         +%#%######%*    
                        .#%%*##@*=*@*=   
                       .#@%%#***#  -%#   
                       *%%%%%%%%-   -#=. 
                      *%%#%%*%%.=+#*+#** 
                     *%%%%%%##+ **#####* 
                    *%%%%%%%%## :#*. +   
                   -%%%%@@%%%%#:   +-:   
                   %%%%%@@%%%%%#*   -+*: 
                  .%%%%%@@@@%%%@*@       
                  :%%%%@@@@@@%@@%***     
                  =%#%%%%%@@@@@@%%#++    
                  .%#%%%%%%@@@@@%%##=    
                   %%%%%###**#%#=%%%=    
                  .@@%%%%%%%%@@%*%%%     
                  .@@@%%%%%%%@@%%%%+     
                   @@@@%%#%%@@@@@#%      
                   =@@@@@@%%%@@@@%@      
                   @@@@@@%@@@@@@@%=      
                  #@@@@@@@@@%%@%%%-      
                 :@@@@@@@@@@@@@@%@:      
                :@@@@@@@@%@@@@@@%%       
                 *@@@@@@@@@#%#+@%%       
                  .@@@+*+ :   .@@%:      
                   %@=        @@@%+      
                  ..@@........@@@%%+*    
                  .:%@*:.....:=+#@@@@.   
          __________________________________
-------------------- ---------------------------------
|      HP: 0/0      | Attacks: Abilities: Inventory: |
-------------------- ---------------------------------

"""),
    elif class_key == "c":
        print("""
                             
                   -**-          .*- 
              ..   -+==          *=+-
             .:..  -==-           *=:
             -*=.   +==           -  
            ..-=.   #=+           =  
             .-+  :+++*#+        .-  
              -+  *******#.       -  
             ..* -=*+++=***. .       
              :*-*-=#+-**++=.    .   
              :#+=++*+:=%%*=-.   -   
              .%==***===%%*+-+   *   
               #==#+#-++%%%+---:.+   
               *++**#+*%%%%+=-=+#+.  
               #*+=+*%*+#%%#===*#*.  
                . ++*-+=+#%%=-++ =   
                ..#+*:++=+%%*=+. .   
               .. =+*-=*+*%%%*=.     
                . =++-=+###%%#= -    
                 -+**--*%#*%%#- +    
                  :+*---*=+%%#+ +    
                  :**=:-:-+#%%* -    
                  -#**--==-*%%#=:    
                  -*#*--:---%%#*-    
                  =###-:::::+%#*+    
                 .=##%--:-::=-*+*+.  
                 ==*#%+-::::-.=+*=   
                 ==*#%*---:--: =     
                 -+*#  ==--+=  +     
                  +##: .-= ++: -     
                  :+-      -+:.=     
                  ===       +.::     
              .=++==*===-:. ***      
                .==:..:-=++**=-      
                            -*=-     
                              ..     
       ___________________________________

-------------------- ---------------------------------
|      HP: 0/0      | Attacks: Abilities: Inventory: |
-------------------- ---------------------------------
    """)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

race_selection()
print(f"After every thing, you are a level 1 {final_race} {class_choice}")
dashes()
class_stuff_decider()
attack_goblin()
all_stats_assign()
dashes()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

s0()

'''
# Player stats with multiple weapons
player = {"name": f"{class_choice}",
    "hp": 30,
    "ac": 15,  # Armor Class
    "attack_bonus": 5,
    "weapons": {
        "Sword": {"damage_dice": (8, 1), "attack_bonus": 5},
        "Axe": {"damage_dice": (12, 1), "attack_bonus": 4},
        "Dagger": {"damage_dice": (4, 2), "attack_bonus": 6},
    },
    "current_weapon": "Sword",
    "inventory": {"Healing Potion": 2, "Fire Scroll": 1},
}




player = {"name": f"{class_choice}", "hp": (roll_20 + con_mod), "AC": 15,  # Armor Class
    "attack_bonus": 5,
    "weapons": {
        "Sword": {"damage_dice": (8, 1), "attack_bonus": 5},
        "Axe": {"damage_dice": (12, 1), "attack_bonus": 4},
        "Dagger": {"damage_dice": (4, 2), "attack_bonus": 6},
    },
    "current_weapon": "Sword",
    "inventory": {"Healing Potion": 2, "Fire Scroll": 1},
}

'''
'''
# Enemy stats
enemy = {
    "name": "Goblin",
    "hp": 20,
    "ac": 13,
    "attack_bonus": 3,
    "damage_dice": (6, 1),
    "special": "Sneaky Strike"
}

# Attack function
def attack(attacker, defender):
    weapon = attacker.get("current_weapon")
    attack_bonus = attacker["attack_bonus"]
    damage_dice = (1, 1)
    
    if weapon:
        weapon_info = attacker["weapons"][weapon]
        attack_bonus = weapon_info["attack_bonus"]
        damage_dice = weapon_info["damage_dice"]

    roll = roll_d20()
    total_attack = roll + attack_bonus

    if roll == 20:
        damage = roll_damage(*damage_dice) * 2
        defender["hp"] -= damage
        print(f"CRITICAL HIT! {attacker['name']} deals {damage} damage to {defender['name']}! (Roll: {roll})")
    elif roll == 1:
        print(f"{attacker['name']} critically misses! (Roll: {roll})")
    elif total_attack >= defender["ac"]:
        damage = roll_damage(*damage_dice)
        defender["hp"] -= damage
        print(f"{attacker['name']} hits {defender['name']} for {damage} damage! (Roll: {roll})")
    else:
        print(f"{attacker['name']} misses {defender['name']}! (Roll: {roll})")
    print(f"{defender['name']} HP: {defender['hp']}\n")

# Player turn with weapon switching
def player_turn(player, enemy):
    while True:
        print("\nChoose an action:")
        print("1. Attack")
        print("2. Switch Weapon")
        print("3. Use Item")
        print("4. Cast Spell")
        action = input("> ")

        if action == "1":
            attack(player, enemy)
            break
        elif action == "2":
            print("Available weapons:", ", ".join(player["weapons"].keys()))
            choice = input("Choose a weapon to equip: ").title()
            if choice in player["weapons"]:
                player["current_weapon"] = choice
                print(f"Equipped {choice}")
            else:
                print("Invalid weapon choice.")
        elif action == "3":
            if not player["inventory"]:
                print("No items in inventory!")
                continue
            print("Inventory:", player["inventory"])
            item_choice = input("Which item do you want to use?\n> ").title()
            if item_choice in player["inventory"] and player["inventory"][item_choice] > 0:
                if item_choice == "Healing Potion":
                    heal = roll_damage(8)
                    player["hp"] += heal
                    print(f"You heal {heal} HP! Current HP: {player['hp']}")
                player["inventory"][item_choice] -= 1
                break
            else:
                print("Invalid choice or no items left!")
        elif action == "4":
            if "Fire Scroll" in player["inventory"] and player["inventory"]["Fire Scroll"] > 0:
                damage = roll_damage(10)
                enemy["hp"] -= damage
                print(f"You cast Fireball! {enemy['name']} takes {damage} fire damage!")
                player["inventory"]["Fire Scroll"] -= 1
                break
            else:
                print("No spells available!")
        else:
            print("Invalid action!")

# Enemy turn
def enemy_turn(enemy, player):
    if enemy["hp"] < 10 and enemy.get("special") == "Sneaky Strike":
        print(f"{enemy['name']} uses {enemy['special']}!")
        damage = roll_damage(8)
        player["hp"] -= damage
        print(f"{player['name']} takes {damage} damage!\n")
    else:
        attack(enemy, player)

# Battle loop
def battle(player, enemy):
    print(f"A wild {enemy['name']} appears!")
    while player["hp"] > 0 and enemy["hp"] > 0:
        player_turn(player, enemy)
        if enemy["hp"] <= 0:
            print(f"{enemy['name']} is defeated!")
            break
        enemy_turn(enemy, player)
        if player["hp"] <= 0:
            print("You have been defeated!")
            break

battle(player, enemy)


'''