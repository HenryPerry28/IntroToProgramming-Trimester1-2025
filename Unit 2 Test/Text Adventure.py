import random

print("You will be going on an adventure, you will have a choice of certain paths to take, to choose the path, enter the number related to the choice.")

def roll_20():
    r20 = random.randint(1, 20)
    return r20
def roll_10():
    return random.randint(1, 10)
def roll_8():
    return random.randint(1, 8)
def roll_6():
    return random.randint(1, 6)
def roll_4():
    return random.randint(1, 4)
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
            break
    return class_choice

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
    global inventory
    if class_key == "f":
        f_inventory = "Sword", "Heavy Armor", "Healing Potion"
        inventory = f_inventory    
    elif class_key == "w":
        print("You will choose what item you want out of the option")
        scroll = input("What scroll do you want: Fligt, Misty Step (teleportation), Fireball, or Chromatic Orb")
        w_inventory = "Staff", "Light Armor", f"{scroll}"
        inventory = w_inventory
    elif class_key == "r":
        r_inventory = "2 Dagger", "Light Armor", "2 Smoke Bombs"
        inventory = r_inventory
    elif class_key == "c":
        c_inventory = "Staff", "Holy Symbol", "Medium Armor", "Mace"
        inventory = c_inventory
    print(f"{inventory}")

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
    global town_location, town_location_var
    print("Locations:")
    print("> 1. City hall")
    print("> 2. Shopping district")
    print("> 3. The Firewater Inn")
    print("> 4. Town Center")
    av_tl = ["1", "2", "3", "4"]
    while True:
        dashes()
        town_location_var = input("Where would you like to go?\n > ")
        if town_location_var == "1":
            town_location = "City Hall"
        elif town_location_var == "2":
            town_location = "Shopping District"
        elif town_location_var == "3":
            town_location = "The Firewater Inn"
        elif town_location_var == "4":
            town_location = "Town Center"
        if not town_location_var in av_tl:
            print("Input just the number")
        else:
            print(f"You will go to {town_location}")
            toha_hall_location()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def toha_hall_location ():
    global npc_toha_interation_cho, guild_clerk_name, adventurer_name
    adventurer_name = "A local adventurer"
    guild_clerk_name = "The guild clerk"
    if town_location == "City Hall":
        print("You have arrived in city hall, there are only 3 people of intrest.")
        print("> 1. The mayor")
        print(f"> 2. {guild_clerk_name}")
        print(f"> 3. {adventurer_name}")
        print("> 4. Leave")
        av_npc_toha_interations = ["1", "2", "3", "4"]
        av_desc_of_npc_toha_y_or_no = ["Yes", "No"]
        while True:
            desc_npc_toha = input("Would yoo like a description of each (yes or no)?\n > ").title
            if not desc_npc_toha in av_desc_of_npc_toha_y_or_no:
                print("Choose just the number")
            else:
                if desc_npc_toha == "Yes":
                    dashes()
                    print("The mayor is a big advocate for adventures, beacuse you are one is the only reason you could approach him.")
                    print("The guild clerk is responsible for managing the quest board, and is a representative from the 'Blazing Sun' guild")
                    print("The local adventurer is another adventurer like yourself(duh), but he is hoping to join the 'Blazing Sun' guild")
                    dashes()
                    npc_toha_interation_cho = input("Who would you like to talk to?\n > ")
                else:
                    while True:
                        npc_toha_interation_cho = input("Who would you like to talk to?\n > ")
                        if not npc_toha_interation_cho in av_npc_toha_interations:
                            print("Choose just the number(at his point of tired of reminding you)")
                        else:    
                            a_toha_npc_interactions()

def a_toha_npc_interactions():
    global guild_clerk_name, adventurer_name, name_signature
    av_guild_status_y_or_n = ["Yes", "No"]
    if npc_toha_interation_cho == "1":
        dashes()
        print("You walk up to the mayor, and start a chat")
        print("'Oh thank you mighty adventurer (take in mind your level 1) for you service, it means the world to me that you would spend time in such a small town!'")
        print("'Here, take this!' and the mayor gives you 2 gold pieces.")
        gold += 2
        toha_hall_location()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #    
    elif npc_toha_interation_cho == "2":
        dashes()
        print("You walk up to the guild clerk")
        guild_clerk_name = "Eldric Varnell"
        while True:
            guild_status = input("'Hello, my name is Eldric Varnell, I see that you must be an adventurer (based off of you gear), are you looking to join the guild?'\n > ").title
            if not guild_status in av_guild_status_y_or_n:
                print("Really, please, I'm tired of putting in this line of code.")
                a_toha_npc_interactions()
            else:
                if guild_status == "Yes":
                    dashes()
                    print("Great, I will get the set up in a couple of days, I just need you to sign here")
                    name_signature = input("Write your signature here (don't do anything dumb)\n > ")
                    if "67" in name_signature:
                        print("You die of cringe for putting '67' in your name")
                        exit()
                    print("Great, like I said, I'll get back to you in a couple of days.")
                elif guild_status == "No":
                    dashes()
                    print("Bummer, I think you would have been a great fit")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    elif npc_toha_interation_cho == "3":
        dashes()
        adventurer_name = "George [Lurk] Lark"
        print("You walk up to the local adventurer, and he greets you with a kind smile")
        print("'Why hello there, it's nice to see another adventurer in this town, sorry to be rude, my name is George, George Lark, but some call me George lurk, I'm a rogue.'")
        av_join_guild_y_or_no = ["Yes", "No"]
        while True:
            join_guild_y_or_n = input("Anyway I was just signing up to join the 'Blazing Guild', how about you?").title
            if not join_guild_y_or_n in av_join_guild_y_or_no:
                print("Dude stop, I'm still puting them in for every option.")
            else:
                if join_guild_y_or_n == "Yes":
                    dashes()
                    print("Cool, I guess I'll see you around.")
                    toha_hall_location()
                elif join_guild_y_or_n == "No":
                    dashes()
                    print("Lame, well I might see you around?")
                    toha_hall_location()
                    shop_dist_location()


def shop_dist_location():
    if town_location == "Shopping District":
        print("You have entered the shopping district")
        print("There are four different")

def orc_interaction():
    global inn_payment_t_or_f, orc_return_y_or_n, s0_c1, orc_man_relation_npc, gold, silver, copper, inn_payment
    gold = 1; silver = 7; copper = 23; inn_payment = 10
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
    gold = 1
    silver = 7 
    copper = 23
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
                break
        

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
                break
    
#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333#
    
    elif s0_c1 == "3":
        dashes()
        print("'WAKE UP! Payment is due! I'm kicking you out if you don't pay by 12:00 today, and it's already 10:00.' Yells a large voice.")
        orc_man_relation_npc -= 1

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def s1():
    if town_location == "":
        print("Where would you like to go")

def attack_goblin():
    print("""
                    .             
                : .-             
               :#%#:             
               -##+*+            
               +*%##             
                #@#              
                #-               
               #%+               
               *=                
              -*  =++ -%%+*.     
              #     -#+*-+::-    
             #=   :-=-*#+-+=+    
           .:+:  .  *@%%*+-==    
           .+%* : =-===*#+**:    
           :%@@  .-:--=+#%@*.    
          :*@@@# ===::-+#@@@#    
         .:#=@@%*#*+::--+%@%#=   
          *= %@@#%@#*-==*%@%+%#: 
         :-:  *@%+-+*+*+-+=:==%* 
        . :   .:-  -#*#+=#%%%%#%.
        .     =   .+**%%%@@+%#%-.
                  :**%%%##.=+=-: 
                .-*#++*%%%+      
                  *%*%+=%%%      
                  -#%*=-+%%      
                   @-*==+%%:     
                   : %**###:     
                    ##%*@#%      
                   =%%%@%#.      
                   @%%@@%-       
                  +++#@%%%       
                 :%%%**#%#       
                 .:*++-=.        
                    --=--        
    __________________________________
           -------------------- 
           |      HP: 0/0     | 
           --------------------

                                                         
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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

race_selection()
print(f"After every thing, you are a level 1 {final_race} {class_choice}")
dashes()
class_key_decider()
class_stuff_decider()
all_stats_assign()
dashes()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

s0()
