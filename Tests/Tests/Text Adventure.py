import random

print("You will be going on an adventure, you will have a choice of certain paths to take, to choose the path, enter the number related to the choice.")

av_armor = ["Padded Armor", "Hide Armor", "Chain Mail", "Scale Mail", "Leather Armor", "Plate Armor", "+1 Chain Mail"]
av_weapons = ["Longsword", "Shortsword", "Daggers", "Heavy Crossbow", "Magic Missile", "Great Club", "Mace", "+2 Daggers", "+2 Longsword", "Sacred Flame"]
av_scrolls = ["Mini Fireball Scroll", "Chromatic Orb Scroll", "Lightning Bolt Scroll", "Shatter Scroll"]
all_races = ["Human", "Elf", "Dwarf", "Tiefling"]
all_classes = ["Fighter", "Wizard", "Rogue", "Cleric"]

gold = 1
silver = 7 
copper = 23

banned_fw = "f"
ran = "f"
sneak = "f"
auto_crit = 0
mayor_talked = False

def equip_stuff():
    print("Would you like to equip armor or weapons?")
    print("1. Yes")
    print("2. No")
    while True:
        x = input("Choice\n> ")
        if not x in num_list_2:
            print("...")
            equip_stuff()
        else:
            equip_armor()
            equip_weapon

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

prof_bonus = 2

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def print_money ():
    print (f"Gold: {gold} Silver: {silver} Copper: {copper}")

num_list_2 = ["1", "2"]
num_list_3 = ["1", "2", "3"]
num_list_4 = ["1", "2", "3", "4"]
num_list_5 = ["1", "2", "3", "4", "5"]
num_list_6 = ["1", "2", "3", "4", "5", "6"]

def stat_calc():
    x = [(random.randint(1, 6)), (random.randint(1, 6)), (random.randint(1, 6)), (random.randint(1, 6))]
    y = min(x)
    x.remove (y)
    z = sum(x)
    print(z)
    return z

def mod_calc(stat):
    x = (stat - 10) // 2
    print(f"Your final {stat} modifier is : {x}")
    return x

def all_stats_assign():
    global str_mod, dex_mod, con_mod, wis_mod,int_mod, cha_mod, hp_die, hp, prof_bonus
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
            print(f"Your final strengh stat is: {str_stat}")
            print(f"Your final dexterity stat is: {dex_stat}")
            print(f"Your final constition stat is: {con_stat}")
            print(f"Your final wisdom stat is: {wis_stat}")
            print(f"Your final intelligence stat is: {int_stat}")
            print(f"Your final charsima stat is: {cha_stat}")
            print(f"Your proficieny bonus (just extra stat every one gets, will add to certain rolls) is: {prof_bonus}")
            dashes()
            str_mod = mod_calc(str_stat)
            dex_mod = mod_calc(dex_stat)
            con_mod = mod_calc(con_stat)
            wis_mod = mod_calc(wis_stat)
            int_mod = mod_calc(int_stat)
            cha_mod = mod_calc(cha_stat) 
        else:
            print("Enter only the numbers given, you cheater!")
            all_stats_assign()
    except ValueError:
        print("Only integers, pal.")
        all_stats_assign()
    return s1, s2, s3, s4, s5, s6 

def roll_20():
    r20 = random.randint(1, 20)
    return r20
def roll_12():
    r12 = random.randint(1, 12)
    return r12
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
    while True:
        race_choice = input("Choose a race\n > ").title()
        if not race_choice in all_races:
            print("Choose one of the race options")
        else:
            if race_choice in ["Human", "Tiefling"]:
                final_race = race_choice
                print(f"Your final race is: {final_race}")
                class_selection() 
                return
            else:
                subrace_selection()
                return   

def subrace_selection():
    global final_race, race_choice
    if race_choice == "Elf":
        all_subraces = ["High Elf", "Wood Elf", "Drow"]
        print("Elves have three different subraces: High elf, Wood elf, and Drow.")
    elif race_choice == "Dwarf":
        all_subraces = ["Mountain Dwarf", "Hill Dwarf"]
        print("Dwarfs have two different subraces: Hill dwarf and Mountain dwarf.")
    else:
        class_selection()
        return

    while True:
        final_subrace = input("Choose a subrace\n > ").title()
        if final_subrace not in all_subraces:
            print("Choose one of the options")
        else: 
            final_race = final_subrace
            print(f"Your final race is: {final_subrace}")
            class_selection()
            return

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
    
def class_selection():
    global class_choice
    dashes()
    print("It is now time to choose your class")
    print("Class options are: Fighter, Wizard, Rogue or Cleric.")
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

race_selection()
print(f"After every thing, you are a level 1 {final_race} {class_choice}")
dashes()
all_stats_assign()

def hp_die_decider():
    global hp_die, hp, max_hp
    if class_key == "f":
        int_hp = 10
        hp_die = roll_10()
    elif class_key == "w":
        int_hp = 6
        hp_die = roll_6()
    elif class_key == "r":
        int_hp = 8
        hp_die = roll_8()
    elif class_key == "c":
        int_hp = 8
        hp_die = roll_8()
    max_hp = int_hp + int(con_mod)
    hp = max_hp

hp_die_decider()



player = {
    "name": f"{class_choice}",
    "hp": hp,
    "ac": 10 + dex_mod,
    "Attack Bonus": 0,
    "Damage Bonus": 0,
    "Inventory": {"Weapons": {}, "Armor": {}, "Items": {}},
    "Equipped Weapon": None,
    "Equipped Armor": None,
    "Money": {"Gold": gold, "Silver": silver, "Copper": copper},
    "Stunned": 0
}

def stuff():
    global damage_bonus, attack_bonus_var
    if player["Equipped Weapon"] == "Heavy Crossbow":
        attack_bonus_var = dex_mod + prof_bonus
        damage_bonus = dex_mod
    elif player["Equipped Weapon"] == "Magic Missile":
        attack_bonus_var = int_mod + prof_bonus
        damage_bonus = int_mod
    else:
        attack_bonus_var = str_mod + prof_bonus
        damage_bonus = prof_bonus
    player["Attack Bonus"] = attack_bonus_var
    player["Damage Bonus"] = damage_bonus
stuff()

weapons_data = {
    "Longsword": {"Damage Die": (1, 8), "Damage Bonus": 0, "Attack Bonus": 0},
    "Shortsword": {"Damage Die": (1, 6), "Damage Bonus": 0, "Attack Bonus": 0},
    "Daggers": {"Damage Die": (1, 4), "Damage Bonus": 0, "Attack Bonus": 0},
    "Mace": {"Damage Die": (1, 6), "Damage Bonus": 0, "Attack Bonus": 0},
    "Heavy Crossbow": {"Damage Die": (1, 12), "Damage Bonus": 0, "Attack Bonus": 0},
    "Magic Missile": {"Damage Die": (3, 4), "Damage Bonus": 0, "Attack Bonus": 0},
    "Great Club": {"Damage Die": (1, 6), "Damage Bonus": 0, "Attack Bonus": 0},
    "Stone Fist": {"Damage Die": (1, 12), "Damage Bonus": 0, "Attack Bonus": 0},
    "Wolf Claws": {"Damage Die": (2, 6), "Damage Bonus": 0, "Attack Bonus": 0},
    "+2 Longsword": {"Damage Die": (1, 8), "Damage Bonus": 2, "Attack Bonus": 2},
    "+2 Daggers": {"Damage Die": (2, 4), "Damage Bonus": 2, "Attack Bonus": 2},
    "Sacred Flame": {"Damage Die": (2, 8), "Damage Bonus": 0, "Attack Bonus": 0}
}
armor_data = {
    "Leather Armor": {"Base ac": 11, "Bonus": "Dex"},
    "Padded Armor": {"Base ac": 11, "Bonus": "Dex"},
    "Hide Armor": {"Base ac": 12, "Bonus": "Dex (max 2)"},
    "Scale Mail": {"Base ac": 14, "Bonus": "Dex (max 2)"},
    "Chain Mail": {"Base ac": 16, "Bonus": "None"},
    "Plate Mail": {"Base ac": 18, "Bonus": "None"},
    "+1 Chain Mail": {"Base ac": 16, "Bonus": "Dex (max 2)"}
}

def calculate_ac():
    equipped = player["Equipped Armor"]
    armor = armor_data[equipped]
    base_ac = armor["Base ac"]
    bonus = armor["Bonus"]
    if equipped in armor_data:
        if bonus == "Dex":
            return base_ac + dex_mod
        elif bonus == "Dex (max 2)":
            return base_ac + min(dex_mod, 2)
        elif bonus == "None":
            return base_ac

def equip_weapon():
    dashes()
    print("Weapons:", player["Inventory"]["Weapons"])
    weapon_name = input("What weapon would you like to equip?\n> ").title()
    if weapon_name in player["Inventory"]["Weapons"] and weapon_name in weapons_data:
        player["Equipped Weapon"] = weapon_name
        print(f"{player['name']} equips the {weapon_name}.")
    else:
        print("You don't have that weapon or it doesn't exist.")

def equip_armor():
    dashes()
    print("Armor:", player["Inventory"]["Armor"])
    armor_name = input("What armor would you like to equip?\n> ").title()
    if armor_name in player["Inventory"]["Armor"] and armor_name in armor_data:
        player["Equipped Armor"] = armor_name
        player["ac"] = calculate_ac()
        print(f"Equipped {armor_name}, current AC: {player['ac']}")
    else:
        print("Invalid armor. You don't have that or it doesn't exist.")

dashes()

def print_decide_inventory(item_name, quantity=1):
    if item_name in av_weapons:
        category = "Weapons"
    elif item_name in av_armor:
        category = "Armor"
    else:
        category = "Items"
    inv_cat = player["Inventory"][category]
    if item_name in inv_cat:
        inv_cat[item_name] += quantity
    else:
        inv_cat[item_name] = quantity

def class_stuff_decider():
    if class_key == "f":
        print_decide_inventory("Longsword", 1)
        print_decide_inventory("Chain Mail", 1)
        print_decide_inventory("Healing Potion", 4)
    elif class_key == "w":
        print("You will choose what item you want out of the options (all are different scrolls, can cast for free)")
        scroll = input("What scroll do you want: Mini Fireball Scroll, Chromatic Orb Scroll, or Lightning Bolt Scroll\n> ")
        while True:
            if not scroll in av_scrolls:
                print("Write the ENTIRE name of the scroll")
                class_stuff_decider()
            else:
                print_decide_inventory("Magic Missile", 1)
                print_decide_inventory("Padded Armor", 1)
                print_decide_inventory(f"{scroll}", 1)
                print_decide_inventory("Healing Potion", 2)
                break
    elif class_key == "r":
        print_decide_inventory("Daggers", 2)
        print_decide_inventory("Padded Armor", 1)
        print_decide_inventory("Smoke Bomb", 2)
        print_decide_inventory("Healing Potion", 2)
    elif class_key == "c":
        print_decide_inventory("Holy Symbol", 1)
        print_decide_inventory("Hide Armor", 1)
        print_decide_inventory("Mace", 1)
        print_decide_inventory("Healing Potion", 2)
    print(player)

class_stuff_decider()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def town1_map():
    dashes()
    global town_location, banned_fw
    print("Locations:")
    print("> 1. City hall")
    print("> 2. Shopping district")
    if banned_fw == "f":
        print("> 3. The Firewater Inn")
    print("> 4. Town Center (I recommend not going here first)")
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
            elif town_location == "2":
                shop_dist_location()
            elif town_location == "3":
                if banned_fw == "f":
                    fw_inn_location()
                elif banned_fw == "t":
                    print("Your'e banned from here.")
                    town1_map()
            elif town_location == "4":
                pass
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def toha_location():
    global npc_toha_interation_cho, guild_clerk_name, adventurer_name
    adventurer_name = "A local adventurer"
    guild_clerk_name = "The guild clerk"
    print("You have arrived in city hall, there are only 3 people of interest.")
    while True:
        print("Would you like a description of each (yes or no)?")
        print("> 1. Yes")
        print("> 2. No")
        desc_npc_toha = input("Choice\n> ")
        if desc_npc_toha not in num_list_2:
            print("Please choose a valid option.")
            continue
        break
    if desc_npc_toha == "1":
        print("The mayor is a big advocate for adventures...")
        print("The guild clerk manages the quest board...")
        print("The local adventurer hopes to join the guild...")
    while True:
        print("> 1. Talk to the mayor")
        print(f"> 2. Talk to the {guild_clerk_name}")
        print(f"> 3. Talk to the {adventurer_name}")
        print("> 4. Leave")
        npc_toha_interation_cho = input("What would you like to do?\n >")
        if npc_toha_interation_cho not in num_list_4:
            print("Please choose a valid option.")
            continue
        if npc_toha_interation_cho == "4":
            town1_map()
            break
        else:
            a_toha_npc_interactions()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #    
def a_toha_npc_interactions():
    global gold, mayor_talked
    if npc_toha_interation_cho == "1":
        print("You walk up to the mayor, and he says")
        if not mayor_talked:
            print("'Here, take this!' and the mayor gives you 2 gold pieces.")
            gold += 2
            mayor_talked = True
        else:
            print("Town is poor, stop farming")
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
            if not guild_status in num_list_2:
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
                    dashes()
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
    global shop_location, gold, silver, copper
    if town_location == "2":
        print("You have entered the shopping district")
        print("There are four different shops in this area")
        print("> 1. The blacksmith (Doused in Flame)")
        print("> 2. The armorer (Steel Driven)")
        print("> 3. The Bank (that's its name)")
        print("> 4. Leave")
        print(f"> Gold: {gold} Silver: {silver} Copper: {copper}")
        print(f"Inventory: ", player["Inventory"])
        shop_location = input("Where would you like to go?\n> ")
        while True:
            if not shop_location in num_list_4:
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
                    print("You head to the bank, where you can  get money exchanged, upon entering, you see a lithe Drow standing at a counter")
                    print("'How are you doing, my name is Viren. I will help you with any amount of currency exchanging you need to do'")
                    shop_dist_npc_interactions()
                elif shop_location == "4":
                    dashes()
                    print("You decide there is nothing helpful here at the moment, so you head back to onto the street")
                    town1_map()
                    
def shop_dist_npc_interactions():
    global gold, silver, copper
    if shop_location == "1":
        while True:
            dashes()
            print(f"Would you like to browse Dorin's wares(Gold: {gold} Silver: {silver} Copper: {copper})")
            print("> 1. Yes")
            print("> 2. No (leave)")
            blacksmith_y_or_n = input("Choice\n> ")
            if not blacksmith_y_or_n in num_list_2:
                print("STOP")
                shop_dist_npc_interactions()
            else:
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
                                    equip_stuff()
                                    print_money()
                                    print("Anything else?")
                                    shop_dist_npc_interactions()

                                elif (copper// 10) >= 1:
                                    copper -= 10
                                    dashes()
                                    print_money()
                                    print_decide_inventory("Shortsword", 1)
                                    equip_stuff()
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
                                    equip_stuff()
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
                                    equip_stuff()
                                    print("Anything else?")
                                    shop_dist_npc_interactions()
                                elif silver >= 10:
                                    silver -= 10
                                    dashes()
                                    print_money()
                                    print_decide_inventory("Heavy Crossbow", 1)
                                    equip_stuff()
                                    print("Anything else?")
                                    shop_dist_npc_interactions()
                                elif silver + (copper//10) >= 10:
                                    silver -= silver
                                    hc_s_shop_payment = 10
                                    hc_s_shop_payment -= silver
                                    copper -= 10*hc_s_shop_payment
                                elif copper >= 100:
                                    copper -= 100
                                    dashes()
                                    print("Why do you have so much copper?")
                                    print_money()
                                    print_decide_inventory("Heavy Crossbow", 1)
                                    equip_stuff()
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
                            elif blacksmith_purchase == "5":
                                print("You leave")
                                shop_dist_location()
                elif blacksmith_y_or_n == "2":
                    if gold < 1:
                        print("You realize that you're broke and can't buy anything anway so you head outside")
                        shop_dist_location()
                    else:
                        print("There is nothing of interest in Dorin's stock so you leave")
                        shop_dist_location()
    if shop_location == "2":
        while True:
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
                    print("> 3. Plate Armor (heavy; 1 gold)")
                    print("> 4. None (leave)")
                    buy_armor = input("What would you like to buy?\n> ")
                    if buy_armor == "1":
                        if silver >= 3:
                            silver -= silver
                            dashes()
                            print_money()
                            print_decide_inventory("Leather Armor", 1)
                            equip_stuff()
                            print("Anything else?")
                            shop_dist_npc_interactions
                        elif silver + (copper//10) >= 3:
                            la_s_payment = 3
                            la_s_payment -= silver
                            copper -= la_s_payment*10
                            dashes()
                            print_money()
                            print_decide_inventory("Leather Armor", 1)
                            equip_stuff()
                            print("Anything else?")
                            shop_dist_npc_interactions()
                        elif copper >= 30:
                            copper -= 30
                            dashes()
                            print_money()
                            print_decide_inventory("Leather Armor", 1)
                            equip_stuff()
                            print("Anything else?")
                            shop_dist_npc_interactions()
                        else:
                            print("You have no money")
                            shop_dist_npc_interactions()
                    if buy_armor == "2":
                        if silver >= 8:
                            silver -= silver
                            dashes()
                            print_money()
                            print_decide_inventory("Scale Mail", 1)
                            equip_stuff()
                            print("Anything else?")
                            shop_dist_npc_interactions
                        elif silver + (copper//10) >= 8:
                            la_s_payment = 8
                            la_s_payment -= silver
                            copper -= la_s_payment*10
                            dashes()
                            print_money()
                            print_decide_inventory("Scale Mail", 1)
                            equip_stuff()
                            print("Anything else?")
                            shop_dist_npc_interactions()
                        elif copper >= 80:
                            copper -= 80
                            dashes()
                            print_money()
                            print_decide_inventory("Scale Mail", 1)
                            equip_stuff()
                            print("Anything else?")
                            shop_dist_npc_interactions()
                        else:
                            print("You have no money")
                            shop_dist_npc_interactions()
                    if buy_armor == "3":
                        if gold >= 1:
                            gold -= 1
                            dashes()
                            print_money()
                            print_decide_inventory("Plate Armor", 1)
                            equip_stuff()
                        elif silver >= 10:
                            silver -= silver
                            dashes()
                            print_money()
                            print_decide_inventory("Plate Armor", 1)
                            equip_stuff()
                            print("Anything else?")
                            shop_dist_npc_interactions
                        elif silver + (copper//10) >= 10:
                            la_s_payment = 10
                            la_s_payment -= silver
                            copper -= la_s_payment*10
                            dashes()
                            print_money()
                            print_decide_inventory("Plate Armor", 1)
                            equip_stuff()
                            print("Anything else?")
                            shop_dist_npc_interactions()
                        elif copper >= 100:
                            dashes()
                            print_money()
                            print_decide_inventory("Plate Armor", 1)
                            equip_stuff()
                            print("Anything else?")
                            shop_dist_npc_interactions()
                        else:
                            print("You have no money")
                            shop_dist_npc_interactions()
                    if buy_armor == "4":
                        print("You decide nothing here is helpful and leave")
                        shop_dist_location()


                if armor_y_or_n == "2":
                    print("You decide that nothing here is worth it")
                    shop_dist_location()
    if shop_location == "3":
        global coin_exchange_y_or_n
        print("Would you like to exchange coins?")
        print("> 1. Yes")
        print("> 2. No")
        coin_exchange_y_or_n = input("Choice\n>")
        while True:
            if not coin_exchange_y_or_n in num_list_2:
                print("STOP")
                shop_dist_location()
            else:
                coin_exchanger()

def check_coin():
    global silver, gold, copper, coin_amount, coin_from
    if gold <= 0 or silver <= 0 or copper <= 0:
        print("You don't have enough of this coin")
        coin_exchanger()
    else:
        if coin_from == "1" and int(int(coin_amount)) > gold:
            print("Thats too much, cheater!")
            coin_exchanger()
        elif coin_from == "2" and int(int(coin_amount)) > silver:
            print("That's too much, cheater!")
            coin_exchanger()
        elif coin_from == "3" and int(int(coin_amount)) > copper:
            print("That's too much, cheater!")
            coin_exchanger()

def coin_exchanger():    
    global coin_exchange_y_or_n, gold, silver, copper, coin_amount, coin_from
    if coin_exchange_y_or_n == "1":
        print("Which coin would you like to exchange?")
        print("> 1. Gold")
        print("> 2. Silver")
        print("> 3. Copper")
        print("> 4. None(leave)")
        print_money()
        while True:
            coin_from = input("Choice\n>")
            if not coin_from in num_list_4:
                print("...")
                continue
            else:
                if coin_from == "4":
                    print("You decide you don't want any coins exchanged and head out")
                    shop_dist_location()
                while True:
                    dashes()
                    print("Which coin would like to exchange to?")
                    print("> 1. Gold")
                    print("> 2. Silver")
                    print("> 3. Copper")
                    print("> 4. None (leave)")
                    print_money()
                    coin_to = input("Choice\n> ")
                    if not coin_to in num_list_4:
                        print("...")
                        continue
                    else:
                        if coin_to == "4":
                            print("You decide that none of these coin types are usefull and head out")
                            shop_dist_location
                        if coin_from == "1" and coin_to == "1":
                            print("These are the same coin type")
                            continue
                        elif coin_from == "1" and coin_to == "2":
                            print("How much would you like to exchange?")
                            coin_amount = input("Amount > ")
                            check_coin()
                            gold -= int(coin_amount); silver += (int(coin_amount) * 10)
                        elif coin_from == "1" and coin_to == "3":
                            print("How much would you like to exchange?")
                            coin_amount = input("Amount > ")
                            check_coin()
                            gold -= int(coin_amount); copper += (int(coin_amount) * 100) 
                        if coin_from == "2" and coin_to == "1":
                            print("How much would you like to exchange(10 silver = 1 gold)?")
                            coin_amount = input("Amount > ")
                            check_coin()
                            if int(coin_amount) < 10:
                                print("That's not enough silver to turn into 1 gold")
                                continue
                            else:
                                if not int(coin_amount) // 10 == 0:
                                    print("Input proper amount of silver(has to be in 10)")
                                    continue
                                else:
                                    silver -= int(coin_amount); gold += (int(coin_amount) /  10)
                                    continue
                        elif coin_from == "2" and coin_to == "2":
                            print("These are the same coin type")
                            continue
                        elif coin_from == "2" and coin_to == "3":
                            print("How much would you like to exchange (1 silver = 10 copper)?")
                            coin_amount = input("Amount > ")
                            check_coin()
                            silver -= int(coin_amount); copper += (int(coin_amount) * 10)
                        if coin_from == "3" and coin_from == "1":
                            print("How much would you like to exchange?")
                            coin_amount = input("Amount > ")
                            check_coin()
                            if int(coin_amount) < 100:
                                print("That's not enough copper to turn into one gold")
                                continue
                            else:
                                if not int(coin_amount) // 10 == 0:
                                    print("Input put proper amount of copper(base 10)")
                                    continue
                                else:
                                    copper -= int(coin_amount); gold += (int(coin_amount) / 100)
                                    continue
                        elif coin_from == "3" and coin_to == "2":
                            print("How much would you like to exchange (10 copper = 1 silver)")
                            coin_amount = input("Amount > ")
                            check_coin()
                            if not int(coin_amount) < 10:
                                print("That's not enough copper to turn into one silver")
                                continue
                            else:
                                if not int(coin_amount) // 10 == 0:
                                    print("Input put proper amount of copper(base 10)")
                                    continue
                                else: 
                                    copper -= int(coin_amount); silver += (int(coin_amount) / 10)
                                    continue
                        elif coin_from == "3" and coin_to == "3":
                            print("These are the same coin")
                            continue
    elif coin_exchange_y_or_n == "2":
        print("You don't wanna exchange coins and so you decide to head out")
        shop_dist_location
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


def fw_inn_location():
    global inn_payment, orc_retalk_y_or_n
    dashes()
    print("You have decide to head back to the orc to pay off you debt.")
    print("Upon entering you instantly spot the orc behind the bar")
    print("What would you like to do?")
    print("1. Talk to orc personally")
    print("2. Just order a drink")
    print("3. Leave")
    print_money()
    while True:
        orc_retalk_y_or_n = input("Choice\n> ")
        if not orc_retalk_y_or_n in num_list_3:
            print("...")
            continue
        else:
            if orc_retalk_y_or_n == "1":
                orc_interaction_2_pay()
            elif orc_retalk_y_or_n == "2":
                orc_interaction_2_drink()
            elif orc_retalk_y_or_n == "3":
                print("You decide that nothing here is helpful")
                shop_dist_location()

                
def orc_interaction_2_pay():
    global orc_retalk_y_or_n, silver, gold, copper, inn_payment, banned_fw
    dashes()
    print("You walk to where the orc is serving people and sit down on a stool.")
    print("The orc finishes with his current customer and comes over to talk to you.")
    print(f"'Well if it isn't the adventurer that owes my {inn_payment} silver, if you have the payment now great, but otherwise you still have time.'")
    print("Would you like to pay the orc?")
    print("1. Yes")
    print("2. No")
    repay_orc_y_or_n = input("Choice\n> ")
    print_money()
    while True:
        if not repay_orc_y_or_n in num_list_2:
            print("...")
            continue
        else:
            if repay_orc_y_or_n == "1":
                if silver >= inn_payment:
                    silver -= inn_payment
                elif (silver + (copper // 10)) >= inn_payment:
                    if silver <= inn_payment:
                        silver -= silver
                        x = (inn_payment - silver); copper -= (x * 10) 
                    else:
                        silver -= inn_payment                    
                else:
                    print("You still don't have enough money, just leave me alone and forget about the payment")
                    banned_fw = "t"
                    town1_map()
            if repay_orc_y_or_n == "2":
                print("Well comeback later to pay me, but feel free to order a drink")
                fw_inn_location()

def orc_interaction_2_drink():
    global con_mod, copper, silver, gold, inn_payment
    count = 0; tab = 0
    max_drink = (15 + con_mod) #put con_mod in after testing
    print("You walk up to the orc and he asks what you want")
    print("1. Addicting drink")
    print("2. Some juice")
    print("3. Water")
    print("4. None (leave)")
    while True:
        drink_cho = input("Choice\n> ")
        if drink_cho not in num_list_4:
            print("...")
            continue
        if drink_cho == "1":
            print("You want an addicting drink, the orc serves it to you and says, 'That'll be one copper piece'")
            while count <= max_drink:
                if count == max_drink:
                    print("You have had too many addicting drinks!")
                    print("Secret ending discovered: Drunkard")
                    exit()
                print("The drink is quite addicting. Would you like another one?")
                print("1. Yes")
                print("2. No")
                drink_more = input("Choice\n> ")
                if drink_more not in num_list_2:
                    print("...")
                    continue
                if drink_more == "1":
                    count += 1
                    tab += 1
                    print(f"You drink another. Total: {count}")                
                if drink_more == "2":
                    print(f"You decide {count} is enough addicting drinks, your tab comes out to {tab}")
                    fw_inn_location() 
            break
        if drink_cho == "2":
            x = "juice"
        elif drink_cho == "3":
            x = "water"
        if drink_cho == "2" or drink_cho == "3":
            print(f"The orc hands you your {x}, that's one copper peice.")
            copper -= 1
            print("Now scram if you aren't gonna have a real drink")
            town1_map()
        if drink_cho == "4":
            print("You decide that a drink isn't worth it")
            fw_inn_location()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def town_center():
    global gold
    dashes()
    print("You head to town center and when you get there, a group of dwarfs are standing anxioulsy around what appears to be a quest board.")
    print("As you're looking, one of them locks eyes with you, and rushes over.")
    print("'Please we need your help, the town of Waterock has been attacked by a stone golem, they need supplies in order to keep their town afloat.'")
    print("'You seem like the only one in this town who could help them, please, I'll give you all that I have, which is 3 gold, 27 silver, and 132 copper.'")
    print("'Please just help me!'")
    print("Do you want to help the dwarfs?")
    print("1. Yes")
    print("2. No")
    while True:
        quest_help = input("Choice\n >")
        if not quest_help in num_list_2:
            print("...")
            continue
        else:
            if quest_help == "1":
                print("Oh thank you so much, just take this cart of supplies off down that trail until you hit Waterock, and take this gold as thanks."); gold += 3; print_money
                the_trail()
            elif quest_help == "2":
                print("You decide to not do your job as an adventurer and help people")
                print("Secret ending discovered: Useless")
                exit()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def orc_interaction():
    global orc_return_y_or_n, s0_c1, orc_man_relation_npc, gold, silver, copper, inn_payment
    orc_man_relation_npc = 0
    if s0_c1 == "1":
        if silver >= inn_payment:
            print("He takes your money and says, 'Great, I never need to see you again.'")
            silver -= inn_payment
            town1_map()
            return silver
        elif (silver + (copper // 10)) >= inn_payment:
            if silver <= inn_payment:
                silver -= silver
                x = (inn_payment - silver); copper -= (x * 10) 
            else:
                silver -= inn_payment
            print("He takes your money and says, 'Great, now I never need to see you again'")
            town1_map()
        else:
            dashes()
            print("'You don't have enough money, head to the bank (in the shopping district) if you wanna get that gold piece traded in for silver or copper.'")
            print("Would you like to keep talking to the orc")
            print("> 1. Yes")
            print("> 2. No")
            while True:
                orc_return_y_or_n = input("Choice\n > ")
                if not orc_return_y_or_n in num_list_2:
                    print("Please stop (or you actually messed up on this one, if so, it's only the number)")
                    continue
                else:
                    if orc_return_y_or_n == "1":
                        print("Look man, I just told you you don't have enough money to pay me, head into town to earn some, I'm sure the mayor will give you some for free.")
                        town1_map()
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
    global orc_man_relation_npc, gold, silver, copper, s0_c1, s0_c2, inn_payment
    orc_man_relation_npc = 0
    inn_payment = 10
    dashes()
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

# Create another ending where loot is taken right before town enterance
# Add a battle loop of 10 random encounters (with loot), quest ends with talking to mayor and delivering goods
# Treasure: 4 gold, +1 longsword, +1 magic missile, +1 heavy crossbow 

total_encounters = 10
encounter_counter = 0
day = 1

all_encounters = [
    "Broken Cart",
    "Sudden Storm",
    "Singing Stone",
    "Lost Animal",
    "Herbal Grove",
    "Traveling Scholar",
    "Nothing",
    "Nothing",
    "Nothing",
    "Nothing",
]

def print_mods():
    print(f"Strength modifier: {str_mod} Dexterity modifier: {dex_mod} Constitution modifier: {con_mod} ")
    print(f"Wisdom modifier: {wis_mod} Intelligence modifier: {int_mod} Charisma modifier: {cha_mod}")

def Broken_Cart():
    global total_encounters
    dashes()
    print("As you are walking along the path your cart starts to fail, and it brakes, lucky you brought spare part, but do you know how to intall them is the question.")
    print("To fix them you will roll a survial check (wisdom)"); 
    x = (roll_20() + wis_mod); print(x)
    if x >= 10:
        print("It is not terribly hard to figure out how fixing a wheel works, and thus get it on quickly before any struggles occur.")
    else:
        print("It takes a long while before you get something that could even pass for a wheel, your journey will be take long.")
        total_encounters += 5
def Sudden_Storm():
    dashes()
    print("As you walk the trail, out of no where a storm hits, and it hits hard, you must either find shelter (wisdom) or keep pushing though (constitution)")
    print("1. Find shelter")
    print("2. Push through (cargo will be fine)")
    while True:
        x = input("Choice\n> ")
        if x not in num_list_2:
            print("We're so far just stop")
            Sudden_Storm()
        else:
            if x == "1":
                y = (roll_20() + wis_mod); print(y)
                if y >= 12:
                    print("Being surrounded by trees it's not terribly hard to find a dense patch for cover, where you wait it out."); total_encounters += 1
                else:
                    print("The heavy storm makes it very hard to see and you fail to find adequate shelter, take 1 point of exhaustion damage"); total_encounters += 1; player["hp"] -= 1; print(player('hp'))
            if x == "2":
                z = (roll_20() + con_mod); print(z)
                if z >= 14:
                    print("You push forward with no further consequences")
                else:
                    print("You try your hardest to push through the brutal storm, unfortunatly your best is not good enough, you take 2 points of exhaustion damage"); player["hp"] -= 2; print(player('hp'))

def Singing_Stone():
    dashes()
    print("You approach a medium sized stone that is making strange sounds, do you ignore it or listen closer")
    print("1. Ignore")
    print("2. Listen closer")
    while True:
        x = input("Choice\n> ")
        if x not in num_list_2:
            print("We're so far just stop")
            Singing_Stone()
        else:
            if x == "1":
                print("You move on seeing no value and only risk from the stone")
            elif x == "2":
                y = (roll_20 + wis_mod); print(y)
                if y >= 20:
                    print("Upon listening really close you can make out the words, 'Never gonna give you up, never gonna let you down, never gonna turn around and desert you,' and after that you decide to move on")
                else:
                    print("You listen really close yet can't make out a sound and so you move on")
def Lost_Animal():
    dashes()
    print("Just traveling down the path you start to hear a whine, like that of an animal. Soon you spot the source of the sound, a small little fox who is stuck in a trap")
    print("Do you want to hlep the poor critter?")
    print("1. Help it")
    print("2. Don't help it")
    while True:
        x = input("Choice\n> ")
        if not x in num_list_2:
            print("...")
            Lost_Animal()
        else:
            if x == "1":
                print("You decide to free the fox, but in order to do so you must make an animal handling check (wisdom) to soothe it.")
                y = (roll_20() + wis_mod); print(y)
                if y >= 12:
                    print("You successfully soothe the fox and free it, once you do it dashes into the trees.")
                else:
                    print("You thought you had it soothed until you undo the trap, when it then bites you, take 1 point of damage."); player["hp"] -= 1; print(player('hp'))
            elif x == "2":
                print("You decide the fox isn't worth it and move on")
def Herbal_Grove():
    dashes()
    print("While traveling you stuble across a patch of dense flora, you can't quite tell what it is, but the aroma is very pleasent.")
    print("Would you like to investigate the flora?")
    print("1. Yes")
    print("2. No")
    while True:
        x = input("Choice\n> ")
        if not x in num_list_2:
            print("...")
            Herbal_Grove()
        else:
            if x == "1":
                print("Upon investigatin the flora the plants seem familiar, only if you could remember, roll history (intelligence)")
                y = (roll_20 + int_mod); print
                if y >= 12:
                    print("You remeber that eating these plants has some medicinal effcts (healing)"); print_decide_inventory("Medicinal Plants", 5)
                else:
                    print("You can't quite remeber what they are, would you like to take them?")
                    while True:
                        z = input("Choice\n> ")
                        if not z in num_list_2:
                            print("...")
                            Herbal_Grove()
                        else:
                            if z == "1":
                                print("You decide that they can't be that bad and take a bundle."); print_decide_inventory("Medicinal Plants", 5)
                            elif z == "2":
                                print("You decide that the plants are not worth the risk an move on.")
def Traveling_Scholar():
    dashes()
    print("As you walk down the trail you spot a figure, they get closer and greet you, 'Why hello there, would you like to know what these woods were named after?'")
    print("1. Yes")
    print("2. No")
    while True:
        x = input("Choice\n> ")
        if not x in num_list_2:
            print("...")
            Traveling_Scholar()
        else:
            if x == "1":
                print("'Great, these woods are called the Whispergrove Woods and are known for their singing stones—smooth rocks that make soft tones when the wind passes over them. Travelers often rest near these stones, finding them strangely soothing. The woods are home to woodland animals, some stray hunters, and the occasional wandering merchant. The forest has small clearings with streams, berry bushes, and fallen logs, providing natural places to camp. The trail through Whispergrove is well-trodden, though some spots are muddy or overgrown after rain. Locals say the woods have been used for generations for foraging, hunting, and resting on long journeys. While mostly peaceful, travelers are advised to keep an eye out for wild animals or bandits who sometimes use the forest as cover.'")
            elif x == "2":
                print("'Shame, anyway see you around'")
def Nothing():
    print("Nothing eventful happens")
def waterock():
    global class_key
    dashes()
    print("After quite some time you finally make it to Waterock, and the mayor greets you vigorously, 'You must be the adventurer to deliver us much needed supplies, thank you so much. Here is 5 gold as a thanks'")
    print("'We may not have much now, but we a an Inn where you could sleep and stay, or if you are really feeling adventerus you could go kill a stone golem that has been bothering us for a while'")
    print("1. Do you want to stay in town")
    print("2. Head back to Firewater")
    print("3. Take care of the golem")
    while True:
        x = input("Choice\n> ")
        if not x in num_list_3:
            print("...")
            waterock()
        else:
            if x == "1":
                print("'Great I'll get you a room at the inn right away, free of charge!'")
                print("================================= Ending discoverd: Waterock, New Begginings =================================")
                print("   Now staying in Waterock, you find that there are lots more oppourtinties for growth here than Firewater.   ")
            elif x == "2":
                print("'Okay, well thanks for the supplies, it was good to know you.'")
                print("===================================== Ending discoverd: Firewater, Home Sweet Home =====================================")
                print("You decide that a new town wasn't for you, and you'd rather stay with something familiar, hence you return to firewater.")
            elif x == "3":
                print("'Thanks so much, you really are the greatest! The golem is out to the west by about a mile, oh, and you might need this.'")
                print("+1 or +2 means that that item has the respective + to their stats, +1 longsword will deal one more damage")
                if class_key == "f":
                    print("The mayor gives you 5 healing potions and a +2 Longsword, and +1 Chain Mail Armor.")
                    print_decide_inventory("+2 Longsword", 1); print_decide_inventory("+1 Chain Mail Armor", 1); print_decide_inventory("Healing Potion", 5)
                elif class_key == "w":
                    print("The mayor hands you a 'Shatter' scroll, and says 'Should work great against the golem' he also hands you 5 healing potions.")
                    print_decide_inventory("Shatter Scroll", 1); print_decide_inventory("Healing Potion", 5)
                elif class_key == "r":
                    print("The mayor hands you a pair of +2 daggers, 5 healing potions, and an invisibility potion, he says 'Good luck with killing the golem!'")
                    print_decide_inventory("+2 Daggers", 1); print_decide_inventory("Invisibility Potion", 1), print_decide_inventory("Healing Potion", 5)
                elif class_key == "c":
                    print("The mayor hand you a large orb radiating with divine energy, and he teaches you the incantation for sacred flame (you can use it as a weapon)")
                    print_decide_inventory("Divine Orb", 3); print_decide_inventory("Sacred Flame", 1)
                print("You start heading towards where the golem was pointed out to you, you arrive at the spot and prepare.")
                equip_armor()
                equip_weapon()
                print("After equipping the new gear, you engage in combat.")
                battle(player, goblin_enemy)

def encounter_rand():
    global encounter_counter
    encounter = random.choice(all_encounters)
    if encounter == "Broken Cart":
        Broken_Cart(); all_encounters.remove("Broken Cart"); encounter_counter += 1
    elif encounter == "Sudden Storm":
        Sudden_Storm(); all_encounters.remove("Sudden Storm"); encounter_counter += 1
    elif encounter == "Singing Stone":
        Singing_Stone(); all_encounters.remove("Singing Stone"); encounter_counter += 1
    elif encounter == "Lost Animal":
        Lost_Animal(); all_encounters.remove("Lost Animal"); encounter_counter += 1
    elif encounter == "Herbal Grove":
        Herbal_Grove(); all_encounters.remove("Herbal Grove"); encounter_counter += 1
    elif encounter == "Traveling Scholar":
        Traveling_Scholar(); all_encounters.remove("Traveling Scholar"); encounter_counter += 1
    elif encounter == "Nothing":
        Nothing(); encounter_counter += 1
        

def the_trail():
    global total_encounters, encounter_counter, day
    print("You begin down the forest trail...")
    while encounter_counter < total_encounters:
        total_encounters <= 10
        if (encounter_counter % 5) == 0:
            print("You decide that you have traveled enough for today and take a rest")
            print(f"=== Day {day} ===")
            day += 1
            print(f"=== Day {day} ===")
        elif random.randint(1, 4) <= 3:
            print_mods()
            encounter_rand()
        elif encounter_counter == total_encounters:
            waterock()
        else:
           battle(player, random.choice(enemies)); encounter_counter += 1



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def print_char():
    if class_key == "f":
        print(f"""
                                                         
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

-------------------- ------------------------------------
|      HP: {hp}/{max_hp}      | Attacks: Abilities: Inventory: |
-------------------- ------------------------------------
          """),

    elif class_key == "w":
        print(f"""                 
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

-------------------- -------------------------------------
|      HP: {hp}/{max_hp}      | Attacks: Abilities: Inventory: |
-------------------- -------------------------------------

"""),
    elif class_key == "r":
        print(f"""

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
-------------------- -------------------------------------
|      HP: {hp}/{max_hp}      | Attacks: Abilities: Inventory: |
-------------------- -------------------------------------

"""),
    elif class_key == "c":
        print(f"""
                             
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

-------------------- -------------------------------------
|      HP: {hp}/{max_hp}      | Attacks: Abilities: Inventory: |
-------------------- -------------------------------------
    """)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

equip_armor()
equip_weapon()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

s0()

def fireball():
    print("Are you sure you want to cast this fireball, the enemy is within melee range.")
    print("1. Yes")
    print("2. No")
    while True:
        x = input("Choice\n> ")
        if not x in num_list_2:
            print("You're still doing it")
        else:
            if x == "1":
                print("You decide that casting an explosive spell from 2ft away is a great way to die")
                print("Ending discovered: I CAST FIREBALL!!!!")
                exit()
            elif x == 2: 
                continue

def money_loot():
    global gold, silver, copper
    # 1: Gold, 2: Gold + silver, 3: Gold + silver + copper, 4: Silver, 5: Silver + copper, 6: Copper
    x = random.randint(1, 3)
    if x == 1:
        gold_rand = random.randint(0, 3);
        silver_rand = 0
        copper_rand = 0
    elif x == 2:
        gold_rand = random.randint(1, 3)
        silver_rand = random.randint(5, 20)
        copper_rand = 0
    elif x == 3:
        gold_rand = random.randint(1, 3)
        silver_rand = random.randint(5, 20)
        copper_rand = random.randint(50, 200)
    elif x == 4:
        gold_rand = 0
        silver_rand = random.randint(5, 20)
        copper_rand = 0
    elif x == 5:
        gold_rand = 0
        silver_rand = random.randint(5, 20)
        copper_rand = random.randint(50, 200)
    elif x == 6:
        gold_rand = 0
        silver_rand = 0
        copper_rand = random.randint(50, 200)
    gold += gold_rand; silver += silver_rand; copper += copper_rand

def roll_damage(num_dice, die_type):
    global damage_bonus
    total = 0; weapon = player["Equipped Weapon"]
    for _ in range(num_dice):
        total += random.randint(1, die_type); 
    total += damage_bonus
    print(f"You used a {weapon} and rolled a {num_dice}d{die_type} for {total}.")
    return total
    
wolf_enemy = {
    "name": "Hungry Wolf",
    "hp": 14,
    "ac": 10,
    "Equipped Weapon": {"Wolf Claws"},
    "Special": "Double Swipe",
    "Stunned": 0
}

golem_enemy = {
    "name": "Stone Golem",
    "hp": 50,
    "ac": 15,
    "Equipped Weapon": {"Stone Fists"},
    "Special": "Crush", 
    "Stunned": 0
}

bandit_enemy = {
    "name": "Bandit",
    "hp": 12,
    "ac": 14,
    "Equipped Weapon": {"Shortsword"},
    "Special": "Run", 
    "Stunned": 0
}

goblin_enemy = {
    "name": "Goblin",
    "hp": 7,
    "ac": 13,
    "Equipped Weapon": {"Great Club"},
    "Special": "None",
    "Stunned": 0
}

enemies = [goblin_enemy, bandit_enemy, wolf_enemy]

def attack(attacker, defender):
    equipped_weapon = attacker.get("Equipped Weapon")
    attack_bonus = 0
    damage_die = (1, 4)
    damage_bonus = 0
    if equipped_weapon and equipped_weapon in weapons_data:
        weapon_info = weapons_data[equipped_weapon]
        attack_bonus = weapon_info.get("Attack Bonus", 0)
        damage_die = weapon_info.get("Damage Die", (1, 4))
        damage_bonus = weapon_info.get("Damage Bonus", 0)
    roll = roll_20()
    total_attack = roll + attack_bonus
    num_dice, die_size = damage_die
    damage = roll_damage(num_dice, die_size) + damage_bonus
    attacker_name = attacker.get("name", "Attacker")
    defender_name = defender.get("name", "Defender")
    if auto_crit == 1:
        damage *= 2
        defender["hp"] -= damage
        print(f"CRITICAL HIT! {attacker_name} deals {damage} damage to {defender_name}! (Roll: {roll})")        
    if sneak == "t":
        damage += roll_damage(3, 6)
    if roll == 20:
        damage *= 2
        defender["hp"] -= damage
        print(f"CRITICAL HIT! {attacker_name} deals {damage} damage to {defender_name}! (Roll: {roll})")
    elif roll == 1:
        print(f"{attacker_name} critically misses! (Roll: {roll})")
    elif total_attack >= defender.get("ac", 10):
        defender["hp"] -= damage
        print(f"{attacker_name} hits {defender_name} for {damage} damage! (Roll: {roll})")
    else:
        print(f"{attacker_name} misses {defender_name}! (Roll: {roll})")
    print(f"{defender_name} HP: {defender.get('hp', 0)}\n")

def player_turn(player, enemy):
    global hp, max_hp, auto_crit, sneak
    while True:
        if player["Stunned"] > 0:
            print(f"{player['name']} is stunned and connot act this turn")
            player["Stunned"] -= 1
        else:
            print("Choose an action:")
            print("1. Attack (daggers will attack twice automaticaly)")
            print("2. Switch Weapon")
            print("3. Use Item")
            action = input("> ")
            if action == "1":
                if player["Equipped Weapon"] == "Daggers": 
                    attack(player, enemy); attack(player, enemy)
                else:
                    attack(player, enemy)
                break
            elif action == "2":
                equip_weapon()
            elif action == "3":
                if not player["Inventory"]:
                    print("No items in inventory!")
                    continue
                print(player["Inventory"])
                item_choice = input("Which item do you want to use?\n> ").title()
                if item_choice in player["Inventory"] and player["Inventory"][item_choice] > 0:
                    if item_choice == "Healing Potion":
                        heal = roll_damage(1, 6)
                        player["hp"] += heal
                        print(f"You heal {heal} hp, hp: {player['hp']}")
                    elif item_choice == "Mini Fireball Scroll":
                        fireball()
                    elif item_choice == "Chromatic Orb Scroll":
                        print("A orb of mixed light flies toward your enemy")
                        enemy["hp"] -= roll_damage(2, 8)
                    elif item_choice == "Lightning Bolt Scroll":
                        print("A large lightning bolt streaks toward your enemy and stuns them for 1 turn")
                        roll_damage(2, 6)
                        enemy["Stunned"] = 1
                    elif item_choice == "Smoke Bomb":
                        print("You decide that this combat is far to difficult and decide to flee, using a smoke bomb in the process")
                    elif item_choice == "Holy Symbol":
                        if hp <= (max_hp / 2):
                            print("Your patron blesses you with life")
                            hp = max_hp; print(hp)
                        elif enemy["hp"] <= 10:
                            print("Your patron brings down divine justice and smotes your foe")
                            enemy["hp"] = 0
                        else:
                            print("Your patron blesses you with strength, your next hit will auto crit")
                            auto_crit = 1
                    elif item_choice == "Medicinal Plants":
                        heal_m = roll_damage(1, 4)
                        player["hp"] += heal_m
                        print(f"You consume 1 plant, and it heals you for {heal_m} health, {player['hp']}")
                    
# Boosted items

                    elif item_choice == "Invisibility Potion":
                        print("You chugg down the invisibility potion, and vanish, you will get 3d6 additional damage on your next attack, and can't be attacked during the next turn")
                        sneak = "t"; enemy["Stunned"] = 1
                    elif item_choice == "Shatter Scroll":
                        print("You speak the incantation the scoll and SHATTER the golem, dealing 5d6 damage")
                        x = roll_damage(5, 6); enemy["hp"] -= x
                    elif item_choice == "Divine Orb":
                        max_usage = 3
                        current_usage = 0
                        print("What divine power would you like summon (can be used 3 times)?")
                        print("1. Health")
                        print("2. Damage")
                        print("3. Critical Strikes")
                        while True:
                            y = input("Choice\n> ")
                            if not y in num_list_3:
                                print("You're on the final boss, really")
                                player_turn(player, enemy)
                            else:
                                if y == "1":
                                    player["hp"] = max_hp
                                elif y == "2":
                                    z = (enemy["hp"] // 4); enemy["hp"] -= z


                    player["Inventory"][item_choice] -= 1
                    break
                else:
                    print("Invalid choice or no items left!")
            else:
                print("Invalid action!")

#-------------#

def enemy_turn(enemy, player):
    global ran
    if enemy["Stunned"] > 0:
        print(f"{enemy['name']} is stunned and connot act this turn")
        enemy["Stunned"] -= 1
    # Bandit
    elif enemy["hp"] < 3 and enemy.get("Special") == "Run":
        print(f"{enemy['name']} uses {enemy['Special']}!")
        ran = "t"
    # Wolf
    elif enemy["hp"] < 5 and enemy.get("Special") == "Double Swipe":
        print("The hungry wolf is desperate for food and sipes twice!")
        attack(enemy, player); attack(enemy, player)
    # Stone Golem
    elif enemy["hp"] < 7 and enemy.get("Special") == "Crush":
        print("A giant fist slams down on you stunning you for one turn")
        attack(enemy, player); player["Stunned"] = 1
    else:
        attack(enemy, player)

def battle(player, enemy):
    global ran
    print(f"A wild {enemy['name']} appears!")
    while player["hp"] > 0 and enemy["hp"] > 0:
        player_turn(player, enemy)
        if enemy["hp"] <= 0:
            print(f"{enemy['name']} is defeated!")
            if enemy == bandit_enemy:
                print("As loot you recive and his shortsword")
                print_decide_inventory("Shortsword", 1); money_loot(); print(player['Inventory'])
            elif enemy == goblin_enemy:
                print("As loot you recive and his great club")
                print_decide_inventory("Shortsword", 1); money_loot(); print(player['Inventory'])
            elif enemy == golem_enemy:
                print("As loot you recive a pile of rocks and a gem worth 100 gold!")
                print_decide_inventory("Valuable gem"); print_decide_inventory("a pile of rocks"); print(player['Inventory'])
                print("====================================== Unlocked Ending: Golem, Victory ======================================")
                print("Deafeating the golem is no easy feat, but with you and the town's power you slayed golem and claimed victory.")
            break
        
        elif ran == "t":
            print("The bandit has run after you lowering it, you won but got no rewards")
            ran = "f"
        enemy_turn(enemy, player)
        if player["hp"] <= 0:
            if enemy == golem_enemy:
                print("=========================== Unlocked Ending: Golem, Defeat ===========================")
                print("Succumbing to the powers of the golem were expected, you were still a weak adventurer.")
                print("         Yet you still took on the challenge when most would have surrendered         ")
            else:
                print(f"You you died to {enemy["name"]}!")
                print("Ending discovered: Failure")
                exit()
