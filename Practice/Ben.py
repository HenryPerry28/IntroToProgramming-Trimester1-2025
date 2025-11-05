#Imports
import sys
import random

#Repeated functions
def dashes():
    global dash_count
    dash_count += 1
    print(f"\n{dash_count}{'-'*51}")
    if dash_count > 488: 
        ending_secret()
def half_dash():
    global dash_count
    dash_count += 1
    print(f"\n{dash_count}{' - '*17}")
    if dash_count > 488:
        ending_secret()
def error():
    print("Error: not an option\nPlease type the value of the choice you would like")


#Starting functions
def menu():
    print(("-"*51+"\n")*5)
    print("welcome to super good text adventure(temporary name)")
    start_game =input("1. start Game\n2. exit game\n>")
    if start_game == "1":
        startup()
    elif start_game == "2":
        sys.exit("see you later")
    else:
        print("I assume you want to exit")
        sys.exit("see you later")
def startup():
    global var_loop_count, chase_monster, small_unlocked, dash_count, dining_room_name, nest_room_name, lab_room_name, monster_name , max_health, current_health, inventory, current_tool, key_obtained, boulders_destroyed, door_unlocked, slide_discovered, button_pressed, boss_activated, clock_spinning, frog_count, frog_max, cool_frog, magic_frog, silly_frog, camo_frog, peculiar_frog, checked_for_frog, nest_tool_located, current_location, dinner_tool, nest_tool, monster_health, monster_defense, dodge_cooldown, dodge_active, block_cooldown, block_active
    var_loop_count =0
    chase_monster = False
    small_unlocked = False
    dash_count =0

    dining_room_name = "front left room"
    nest_room_name = "right room"
    lab_room_name = "hallway"
    monster_name = "monster"

    max_health = 100
    current_health = 100
    inventory = set()
    current_tool = None

    key_obtained = False
    boulders_destroyed = False
    door_unlocked = False
    slide_discovered = False
    button_pressed = False
    boss_activated = False
    clock_spinning = True

    frog_count = 0
    frog_max = 5
    cool_frog = False
    magic_frog = False
    silly_frog = False
    camo_frog = False
    peculiar_frog = False
    checked_for_frog = False

    current_location = None
    dinner_tool = "axe"
    nest_tool = "pickaxe"

    monster_health = 250
    monster_defense = 1

    dodge_cooldown = 0
    dodge_active = 0
    block_cooldown = 0
    block_active = 0

    print("-"*51)
    print("\n"*20)
    event_cave()


#Route choice functions
def event_cave():
    global var_loop_count, chase_monster, small_unlocked
    dashes()
    if small_unlocked == True:
        print("You are back in the main room of the cave\n")
        exit = input("\nCurrent Options:\n1. Look around the main room\n2. Look around the small room\n3. Leave the cave\n>")

        if exit == "1":
            text_cave_lookaround()
        elif exit == "2":
            event_small_room()
        elif exit == "3":
            event_leave()
        else:
            error()
            event_cave()
    else:
        var_loop_count =0
        chase_monster = False
        small_unlocked = False
        print("You are in a cave\nYou dont know where you are\n")
        exit = input("\nCurrent Options:\n1. Stay in the cave\n2. Leave the cave\n>")

        if exit == "1":
            event_stay()
        elif exit == "2":
            event_leave()
        elif exit == "wake up":      #secret option
                ending_death("Waking up", "You shouldn't slam your head into rocks\nThat won't help you escape")
        else:
            error()
            event_cave()
def event_leave():
    dashes()
    print("You left the cave\nYou now see that you are in a clearing in a forest")
    clearing = input("\nCurrent Options:\n1. return to the cave\n2. continue into the trees\n3. investigate the trees\n>")
    if clearing ==  "1":
        event_cave()
    elif clearing == "2":
        event_strait_path()
    elif clearing == "3":
        text_investigate_trees()
    else:
        error()
        event_leave()
def text_investigate_trees():
    half_dash()
    print("There is somthing off about the trees\nAll of the trees are the exact same\nNot just the trees but the scenery behind them too")
    clearing = input("\nCurrent Options:\n1. return to the cave\n2. continue into the trees\n>")
    if clearing ==  "1":
        event_cave()
    elif clearing == "2":
        event_strait_path()
    else:
        error()
        text_investigate_trees()


def event_stay():
    dashes()
    print("You decided you will stay in the cave")
    stay = input("\nCurrent Options:\n1. Look around the cave\n2. Leave the cave\n>")
    if stay == "1":
        event_cave_lookaround()
    elif stay == "2":
        event_leave()
    else:
        error()
        event_stay()
def event_cave_lookaround():
    global small_unlocked
    small_unlocked = True
    dashes()
    print("As you look around you bump into the wall and it crumbles\nbehind the wall is a smaller room")
    look_around = input("\nCurrent Options:\n1. Investigate the smaller room\n2. Continue looking around in the larger room\n3. leave the cave\n>")
    if look_around == "1":
        event_small_room()
    if look_around == "2":
        text_cave_lookaround()
    if look_around == "3":
        event_leave()
    else:
        error()
        event_cave_lookaround()
def text_cave_lookaround():
    half_dash()
    print("The walls are not very stable\nIt seems they could fall at any moment")
    choice = input("\nCurrent Options:\n1. Investigate the small room\n2. Leave the cave\n>")
    if choice == "1":
        dashes()
        event_small_room()
    elif choice == "2":
        event_leave()
    else:
        error()
        text_cave_lookaround()
def event_small_room():
    global inventory, key_obtained
    print("There  are few features in the small room\nA large carpet in the center of the circular room\nFour empty large bookcases along the walls\nA desk with a clock on the wall above it\n")
    investigate_choice = input("Current options\n1. Investigate Carpet\n2. Investigate bookcases\n3. Investigate desk\n4. Investigate clock\n5. Return to the main room\n>")
    
    if investigate_choice == "1":
        half_dash()
        print("You search the carpet")
        if not key_obtained:
            print("Under the edge you find a key and take it")
            key_obtained = True
            inventory.add("key")
        else:
            print("there is nothing new")
        pause = input("\nEnter to continue>")
        half_dash()
        event_small_room()
    
    elif investigate_choice == "2":
        half_dash()
        print("The forth bookshelf to the right of the desk was stuck and could not move\nNo mater what you do you could not move it\nAll bookshelves are empty\nTHe other bookshelves have nothing behind them.")
        pause = input("\nEnter to continue>")
        half_dash()
        event_small_room()

    elif investigate_choice == "3":
        half_dash()
        print("You take a look at the desk\nThere is nothing on top or within its two drawers")
        pause = input("\nEnter to continue>")
        half_dash()
        event_small_room()
    
    elif investigate_choice == "4":
        event_set_clock()

    elif investigate_choice == "5":
        event_cave()
    
    else:
        error()
        event_small_room()
def event_set_clock():
    dashes()
    print("You take a look at the clock\nIts hands are loose\nYou could probably fix it")
    time = input("\nFix clock?\n1. Yes\n2. No\n>")
    if time == "1":
        save()
        text_cave_route_start()
    elif time == "2":
        event_small_room()
    else:
        event_set_clock()


#Forest route
def event_strait_path():
    dashes()
    print("Ahead of you the path seems to continue endlessly\nThe trees mirror eachother on both sides\nYou hear the sound of trees break behind you")
    path = input("\nCurrent Options:\n1. Continue onward\n2. turn around\n3. leave path\n>")
    if path == "1":
        event_loop()
    elif path == "2": 
        text_strait_turnaround()
    elif path == "3":
        event_moon()
    else:
        error()
        event_strait_path()
def text_strait_turnaround():
    half_dash()
    print("Turning, around you see that the trees behind you have all fallen down\nYou have no way back")
    if input("1. turn around\n>") == "1":
        event_strait_path()
    else:
        error()
        event_strait_path()
def event_loop():
    global var_loop_count
    if var_loop_count > 300:
        ending_secret()
    else:    
        dashes()
        print("The path seems to strech endlessly")
        loop_path = input("\nCurrent Options:\n1. Continue forward\n2. Turn around\n3. Leave path\n>")
        if loop_path == "1":
            var_loop_count+= 1
            event_loop()
        elif loop_path == "2":
            var_loop_count += 1
            event_loop()
        elif loop_path == "3":
            event_moon()
        else:
            error()
            event_loop()
def event_moon():
    dashes()
    print("The moon shines brightly through the trees\nFollowing the path of least resistance you find yourself at a juction")
    moon_path = input("\nCurrent Options:\n1. take the left path\n2. take the right path\n>")
    if moon_path == "1":
        dashes()
        print("RESPAWN ACTIVATED")
        print(" - "*17)
        event_chase()
    if moon_path == "2":
        event_chill()
    if moon_path == "3":       #secret option
        ending_death("unknown","dont wander into forests next time")
    else:
        error()
        event_moon()
def event_chase():
    print("it seems left was the wrong choice\ntowering over you is a face with yellow eyes and teeth")
    global chase_monster
    chase_monster = True
    chase_action = input("what are you going to do\n>")

    if len(chase_action) > 10:
        half_dash()
        print("You were to slow to react\nBefore you knew it everything went black\n\n[Hint: Try entering a shorter message]\n")
        while True:
            half_dash()
            replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
            if replay == "1":
                dashes()
                event_chase()
            elif replay == "2":
                startup()
            else:
                error()
   
    elif "run" in chase_action or "flee" in chase_action or "bolt" in chase_action:
        event_chase_run()
    
    elif "fight" in chase_action or "attack" in chase_action:
        half_dash()
        print("You attempt to fight the monster\nYou did well considering you were empty handed\nHowever it was all for naught\nBefore all fades to black you hear the beast release a wretched scream and thump onto the earth")
        while True:
            half_dash()
            replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
            if replay == "1":
                dashes()
                event_chase()
            elif replay == "2":
                startup()   
            else:
                error()

    else:
        half_dash()
        print("In fear of the monster you couldn't think clearly and it killed you\n\n[Hint: Try entering a simple and relevant action]\n")
        while True:
            half_dash()
            replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
            if replay == "1":
                dashes()
                event_chase()
            elif replay == "2":
                startup()
            else:
                error()  
def event_chase_run():
    if var_loop_count > 15:
        ending_death("exaustion", "maybe dont walk so much before needing to run from a monster") 
    else:
        dashes()
        print("you run away from the monster\n after some running you approch an intersection")
        runaway_path = input("Current options\n1. Run to the left\n2. Run to the right\n>")
        if runaway_path == "1":
            event_chill()
        elif runaway_path == "2":
            half_dash()
            print("you ran to the right forgetting that that was the route you came from\nYou reach the strait path and continue to run\nThe moment you start to slow it seems the monster is immediatly behind you\nEvery thing fades to black")
            while True:
                half_dash()
                replay = input("choose an option to continue\n1. Try again from return\n2. Restart story\n>")
                if replay == "1":
                    dashes()
                    event_chase()
                elif replay == "2":
                    startup()
                else:
                    error()
def event_chill():
    dashes()
    if chase_monster:
        print("the danger has passed\nBehind you the monster continues running down the other path\nIts shreiks gradually fading behind you")
        half_dash()
    print("It is getting cold now\nA mist forms with each breath")
    chill_action = input("\nCurrent Options:\n1. Continue onward\n2. attempt to find warmth\n>")
    if chill_action == "1":
        ending_forest_1()
    elif chill_action == "2":
        event_warmth()
    else:
        error()
        event_chill()
def event_warmth():
    dashes()
    print("You manage to find a blanket\nIt has gotten colder but maybe it would allow you to get some rest")
    warmth_action = input("\nCurrent Options:\n1. Take a rest\n2. Continue onward\n>")
    if warmth_action == "1":
        ending_forest_2()
    elif warmth_action == "2":
        if chase_monster:
            ending_forest_3()
        else:    
            ending_forest_2()
    else:
        error()
        event_warmth()    


# cave route code
def status():
    half_dash()
    print(f"Frogs found {frog_count}/{frog_max}")
    print(f"Health: {current_health}/{max_health}")
    print(f"Inventory:\n{ "-Inventory empty" if inventory == [] else " -".join(inventory)}")
    pause = input("\nEnter to return>")
    print(" - "*17)
def save():
    #I just need it to work
    global var_loop_count, chase_monster, small_unlocked, dash_count, dining_room_name, nest_room_name, lab_room_name, monster_name , max_health, current_health, inventory, current_tool, key_obtained, boulders_destroyed, door_unlocked, slide_discovered, button_pressed, boss_activated, clock_spinning, frog_count, frog_max, cool_frog, magic_frog, silly_frog, camo_frog, peculiar_frog, checked_for_frog, nest_tool_located, current_location, dinner_tool, nest_tool, monster_health, monster_defense, dodge_cooldown, dodge_active, block_cooldown, block_active
    global s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36
    s01 = var_loop_count
    s02 = chase_monster
    s03 = small_unlocked
    s04 = dash_count
    s05 = dining_room_name
    s06 = nest_room_name
    s07 = lab_room_name
    s08 = monster_name
    s09 = max_health
    s10 = current_health
    s11 = inventory
    s12 = current_tool
    s13 = key_obtained
    s14 = boulders_destroyed
    s15 = door_unlocked
    s16 = slide_discovered
    s17 = button_pressed
    s18 = boss_activated
    s19 = clock_spinning
    s20 = frog_count
    s21 = frog_max
    s22 = cool_frog
    s23 = magic_frog
    s24 = silly_frog
    s25 = camo_frog
    s26 = peculiar_frog
    s27 = checked_for_frog
    s28 = current_location
    s29 = dinner_tool
    s30 = nest_tool
    s31 = monster_health
    s32 = monster_defense
    s33 = dodge_cooldown
    s34 = dodge_active
    s35 = block_cooldown
    s36 = block_active
    print("- - "*13)
    print("Game Saved       (Doesnt actually work)")
    print("- - "*13)
def load():
    global var_loop_count, chase_monster, small_unlocked, dash_count, dining_room_name, nest_room_name, lab_room_name, monster_name , max_health, current_health, inventory, current_tool, key_obtained, boulders_destroyed, door_unlocked, slide_discovered, button_pressed, boss_activated, clock_spinning, frog_count, frog_max, cool_frog, magic_frog, silly_frog, camo_frog, peculiar_frog, checked_for_frog, nest_tool_located, current_location, dinner_tool, nest_tool, monster_health, monster_defense, dodge_cooldown, dodge_active, block_cooldown, block_active
    global s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36
    var_loop_count = s01
    chase_monster = s02
    small_unlocked = s03
    dash_count = s04
    dining_room_name = s05
    nest_room_name = s06
    lab_room_name = s07
    monster_name = s08
    max_health = s09
    current_health = s10
    inventory = s11
    current_tool = s12
    key_obtained = s13
    boulders_destroyed = s14
    door_unlocked = s15
    slide_discovered = s16
    button_pressed = s17
    boss_activated = s18
    clock_spinning = s19
    frog_count = s20
    frog_max = s21
    cool_frog = s22
    magic_frog = s23
    silly_frog = s24
    camo_frog = s25
    peculiar_frog = s26
    checked_for_frog = s27
    current_location = s28
    dinner_tool = s29
    nest_tool = s30
    monster_health = s31
    monster_defense = s32
    dodge_cooldown = s33
    dodge_active = s34
    block_cooldown = s35
    block_active = s36
    dashes()
    print("the clock is set to 12:00")
    room_clock()

def text_cave_route_start():
    global dining_room_name, nest_room_name, lab_room_name
    dashes()
    print("Gravel starts to fall as the room starts to shake\nThere is the sound of boulders falling in the main room\nA hole opens in the ceiling\nThe moon shines directly above\nyou leave the clock to go check out the main room\nMaybe you can set the time later")
    print("Boulders cover the entrance to the cave\nYou cannot leave without breaking them")
    half_dash()
    print("Two new paths have shown\nthemselves one to the left of the room with the clock\nOne to your right\nThe clock room is to your left")
    pause = input("\nEnter to continue>")
    dining_room_name = "front left room"
    nest_room_name = "right room"
    lab_room_name = "mysterious room"
    room_main()
def event_entrance():
    global boulders_destroyed
    dashes()
    print("The entrance is blocked by bolders")
    if boulders_destroyed == True:
        event_escape()
    elif "pickaxe" not in inventory:
        print("Maybe if you had a tool you could get out")
        pause = input("Enter to return to the main room\n")
        room_main()
    elif "pickaxe" in inventory:
        print("You could probably use your pick axe to break them")
        break_entrace = input("Break the rocks\n1. yes\n2. No\n>")
        if break_entrace == "1":
            event_escape()
        elif break_entrace == "2":
            room_main()
        else:
            error()
            event_entrance()
def event_tool_found():
    half_dash()
    global current_location, nest_tool, dinner_tool, current_tool, inventory
    if current_location == "nest":
        print(f"You find the {nest_tool} in the nest")
        if current_tool != None:
            print("You cannot store both tools")
            tool_choice = input(f"swap the {current_tool} for the {nest_tool}\n1. Yes\n2. No\n>")
            if tool_choice == "1":
                print(f"You take the {nest_tool}")
                
                inventory.discard(current_tool)
                temp_tool = current_tool
                current_tool = nest_tool
                nest_tool = temp_tool
                inventory.add(current_tool)

                pause = input("\nEnter to continue>")
                return
            elif tool_choice == "2":
                return
            else:
                error()
                event_tool_found()
        
        if current_tool == None:
            tool_choice = input(f"Take the {nest_tool}\n1. Yes\n2. No\n>")
            if tool_choice == "1":
                print(f"You take the {nest_tool}")
                
                inventory.discard(current_tool)
                temp_tool = current_tool
                current_tool = nest_tool
                nest_tool = temp_tool
                inventory.add(current_tool)

                pause = input("\nEnter to continue>")
                return
            elif tool_choice == "2":
                return
            else:
                error()
                event_tool_found()
            
    if current_location == "dinner":
        print(f"You find the {dinner_tool} hanging on the wall")
        if current_tool != None:
            print("You cannot store both tools")
            tool_choice = input(f"swap the {current_tool} for the {dinner_tool}\n1. Yes\n2. No\n>")
            if tool_choice == "1":
                print(f"You take the {dinner_tool}")
                
                inventory.discard(current_tool)
                temp_tool = current_tool
                current_tool = dinner_tool
                dinner_tool = temp_tool
                inventory.add(current_tool)

                pause = input("\nEnter to continue>")
                return
            elif tool_choice == "2":
                return
            else:
                error()
                event_tool_found()
        
        if current_tool == None:
            tool_choice = input(f"Take the {dinner_tool}\n1. Yes\n2. No\n>")
            if tool_choice == "1":
                print(f"You take the {dinner_tool}")
                
                inventory.discard(current_tool)
                temp_tool = current_tool
                current_tool = dinner_tool
                dinner_tool = temp_tool
                inventory.add(current_tool)

                pause = input("\nEnter to continue>")
                return
            elif tool_choice == "2":
                return
            else:
                error()
                event_tool_found()
def event_locked_door():
    global door_unlocked, key_obtained
    dashes()
    if door_unlocked == False:
        print("Before you is a metal door\nThe door has a simple lock")
        if "key" in inventory:
            while True:
                use_key = input("Use key on the door\n1. Yes\n2. No\n>")
                if use_key == "1":
                    dashes()
                    room_lab()
                elif use_key == "2":
                    room_nest()
                else:
                    error()
        else:
            print("maybe you could find a key to open the door in one of the other rooms")
            
    else:
        dashes()
        room_lab()
def event_slide():
    global boss_activated
    dashes()
    print(f"You slide down thr slide\nA terrifing screech rings out from behind you coming from the lab\nThe slide leads to the main room\tThe screech echos from the no longer accecable slide and the {nest_room_name}\nThe clock in the clock room begins to ring loudly")
    boss_activated = True
    pause = input("\nEnter to continue>")
    dashes()
    room_main()
def event_escape():
    global boulders_destroyed,frog_count,frog_max
    dashes()
    if boulders_destroyed == False:
        print("You sucessfully manage to destroy the boulders ")
        boulders_destroyed = True
    print("You are at the entrance to the cave\nThe cave leads directly to a strait path\nThe trees are symetric on either side of the path")
    escape_option = input("Current options:\n1. Follow the path\n2. Go into the woods\n3. return to the cave")
    if escape_option == "1":
        ending_cave_1()
    elif escape_option == "2":
        ending_cave_2()
    elif escape_option == "3":
        room_main()
    else:
        error()
        event_escape()

def room_main():
    global current_location
    current_location = "main room"
    dashes()
    print("You are now in the main room")
    main_room_path = input(f"\nCurrent Options:\n1. Investigate the entrance\n2. go to the clock room\n3. go to the {dining_room_name}\n4. go to the {nest_room_name}\ncs. Check status\n>")
    if main_room_path == "1":
        event_entrance()
    elif main_room_path == "2":
        dashes()
        room_clock()
    elif main_room_path == "3":
        dashes()
        room_dinner()
    elif main_room_path == "4":
        dashes()
        room_nest()
    elif main_room_path == "cs":
        status()
        room_main()
    else:
        error()
        room_main()
def room_clock():
    global current_location, inventory, magic_frog, frog_count, frog_max, boss_activated,clock_spinning, key_obtained
    current_location = "clock room"
    if boss_activated == False or clock_spinning == False:
        print("The clock, carpet, desk, and bookshelves remain")
        clock_choice = input("\nCurrent Options:\n1. Investigate \n2. Set the time\n3. Return to the main room\ncs. Check status\n>")

        if clock_choice == "1":
            while True:
                half_dash()
                investigate_choice = input("investigate options:\n1. The carpet\n2. The bookshelves\n3. the desk\n4. Cancel\n>")
                if investigate_choice == "1":
                    print("You search the carpet")
                    if not key_obtained:
                        print("Under the edge you find a key and take it")
                        key_obtained = True
                        inventory.add("key")
                    else:
                        print("there is nothing new")
                    pause = input("\nEnter to continue>")
                    break

                elif investigate_choice == "2":
                    print("The forth bookshelf to the right of the desk was stuck and could not move\nNo mater what you do you could not move it\nAll bookshelves are empty\nThe other bookshelves have nothing behind them.")
                    if "axe" in inventory and magic_frog == False:
                        half_dash()
                        book_break =input("you can try to use the axe to break the book shelf\n1. yes\n2. no\n>")
                        if book_break == "1":
                            half_dash()
                            print("In the sticks you find something silly\n\nYou find a spinning frog in a magical hat")
                            magic_frog = True
                            frog_count += 1
                            print(f"Frogs found {frog_count}/{frog_max}")
                    pause = input("\nEnter to continue>")
                    break

                elif investigate_choice == "3":
                    print("You take a look at the desk\nThere is nothing on top or within its two drawers")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_choice =="4":
                    break
                else:
                    error()

            half_dash()
            room_clock()

        elif clock_choice == "2":
            half_dash()
            print("You Set the time to 12:00")
            save()
            room_clock()

        elif clock_choice == "3":
            room_main()
        
        elif clock_choice == "cs":
            status()
            room_clock()

        else:
            error()
            half_dash()
            room_clock()
    elif boss_activated == True:
        if clock_spinning == True:
            print("The clock sits spinning rapidly on the wall\nEverytime the clock reaches 12:00 a loud bell rings out")
        else:
            print("The clock on the the wall shows 12:00")
        
        while True:
            set_clock = input("\nSet the clock\n1. Yes\n2. No\n>")
            
            if set_clock == "1":
                print("You stop the cock and set it to 12:00")
                clock_spinning = False
                save()
                break
            
            elif set_clock == "2":
                while True:
                    clock_to_main = input("Return to the main room\n1. Yes\n2. No\n>")
                    if clock_to_main == "1":
                        room_main()
                    elif clock_to_main == "2":
                        half_dash()
                        break
                    else:
                        error()
       
            else:
                error()

        half_dash()
        room_clock()
def room_dinner():
    global inventory, dining_room_name, current_tool, current_location, checked_for_frog, frog_count, frog_max, silly_frog
    current_location = "dinner"
    if dinner_tool != None:
        print(f"You are in the {dining_room_name}")
        if dining_room_name == "front left room":
            print(f"the room appears to be some sort of dining room\nThere are four tables and a counter\nThere are 2 simple stools at each table\nthe {dinner_tool} sits pn the wall behind the counter")
            dining_room_name = "dining room"
        else:
            print(f"The {dining_room_name} remains the same")

        dinner_choice  = input("\nCurrent Options:\n1. Investigate\n2. Return to main room\ncs. check status\n>")
        
        if dinner_choice == "1":
            while True:
                investigate_option = input("Investigate options:\n1. The tables\n2. The counter\n3. The stools\n4. The axe\n5. Cancel\n>")
                half_dash()
                if investigate_option == "1":
                    print("the tables are part of the ground carved from the very cave floor you stand on")
                    if checked_for_frog == True and silly_frog == False:
                        half_dash()
                        print("Under the table you enter a hidden encounter\n\nYou find a spinning frog in a silly hat")
                        silly_frog = True
                        frog_count += 1
                        print(f"Frogs found {frog_count}/{frog_max}")
                        pause = input("\nEnter to continue>")
                    else: 
                        print("Strangely you find skeletons under each of the tables")
                    checked_for_frog = True
                    pause = input("\nEnter to continue>")
                    
                        
                    break
                elif investigate_option == "2":
                    print("The counter is on the opsite end of the room as the entrance\nthe counter is part of the floor\nThe countertop is smooth and cool to the touch")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_option == "3":
                    print("the stools are sturdy and smooth to the touch\nEach stool is made of wood")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_option == "4":
                    event_tool_found()
                    break
                elif investigate_option == "5":
                    break
                else:
                    error()
            half_dash()
            room_dinner()
        elif dinner_choice == "2":
            checked_for_frog = False
            room_main()
        elif dinner_choice == "cs":
            status()
            room_clock()
        else:
            error()
            room_clock()
    else:
        print(f"The {dining_room_name} remains the same")
        dinner_choice  = input("\nCurrent Options:\n1. Investigate\n2. Return to main room\ncs. check status\n>")
        if dinner_choice == "1":
            while True:
                investigate_option = input("Investigate options:\n1. The tables\n2. The counter\n3. The stools\n4. Cancel\n>")
                half_dash()
                if investigate_option == "1":
                    print("the tables are part of the ground carved from the very cave floor you stand on\nStrangely you find skeletons on each of the tables")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_option == "2":
                    print("The counter is on the opsite end of the room as the entrance\nthe countker is part of the floor\nThe countertop is smooth and cool to the touch")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_option == "3":
                    print("the stools are sturdy and smooth to the touch\nEach stool is made of wood")
                    pause = input("\nEnter to continue>")
                    break
                elif investigate_option == "4":
                    break
                else:
                    error()
            half_dash()
            room_dinner()
        elif dinner_choice == "2":
            room_main()
        elif dinner_choice == "cs":
            status()
            room_clock()
        else:
            error()
            room_clock()
def room_nest():
    global inventory, nest_room_name, current_location, nest_tool_located,frog_count, frog_max, cool_frog, boss_activated
    current_location = "nest"
    if boss_activated == False:
        print(f"you are in the {nest_room_name}")
        if nest_room_name == "right room":
            print("The right room is a large room\nThe floor is dirt rather than stone\nIt looks vaguely like a bids nest there are branches around the entire perimeter\nThere is a hall to the right")
            nest_room_name = "nest"
        else:
            print(f"the {nest_room_name} remains the same as before\nthe hall remains on the right")
        
        nest_choice = input(f"\nCurrent options:\n1. Search the nest\n2. Return to the main room\n3. go to the {lab_room_name}\ncs. Check status\n>")
        half_dash()
        if nest_choice == "1":
            nest_finding = random.randint(1,20)
            if nest_finding >= 19 and cool_frog == False:
                
                print("In the sticks you find something magical\n\nYou find a spinning frog in a cool hat")
                cool_frog = True
                frog_count += 1
                print(f"Frogs found {frog_count}/{frog_max}")
               
                pause = input("\nEnter to continue>")
            if nest_finding >= 12 or nest_tool != None:
                nest_tool_located = True
                event_tool_found()
            else:
                print("you did not find anything")
                room_nest()
       
        if nest_choice == "2":
            room_main()
        if nest_choice == "3":
            event_locked_door()
        if nest_choice == "cs":
            status()
            room_nest()
        else:
            error()
            room_nest()
    elif boss_activated == True:
        print("In the nest before you stands a tall humanoid figure on 4 legs\nthe way back to the main room is blocked\nYour only choice is to fight")
        boss_fight()
def room_lab():
    global inventory, door_unlocked, current_location, lab_room_name, slide_discovered, button_pressed,monster_name, camo_frog, frog_count, frog_max
    current_location = "lab"
    if slide_discovered == False:
        if door_unlocked == False:
            print("The key opens the door")
            print("the room behind the door seems to be some sort of lab\nThere are 3 large tubes with plaques at the bottom\nthere is a desk on the far end of the room\nThere are filing cabinets on the right side of the room")
            lab_room_name = "Lab"
            door_unlocked = True
        else:
            print("The lab remains\n3 tubes, 1 desk, filing cabinets")
        lab_option = input(f"\nCurrent options:\n1. Investigate\n2. return to the {nest_room_name}\ncs. check status\n>")
        if lab_option == "1":
            half_dash()
            while True:
                investigate_option = input("\nInvestigate options:\n1. Filing cabinets\n2. Desk\n3. Tubes\n4. Cancel\n>")
                half_dash()

                if investigate_option ==  "1":
                    print("There are large amounts ouf filing cabinets")
                    if button_pressed == False:
                        print("The filing cabinets are filled with papers\nAn interesting paper says that:\n\"loot 002 to find somthing awesome\"")
                    elif button_pressed == True:
                        print("In the filing cabinets all you see is ash\n\nHowever\nAlso in the cabinets you find somthing peculiar\n\nYou find a spinning frog in a camouflage hat")
                        camo_frog = True
                        frog_count += 1
                        print(f"Frogs found {frog_count}/{frog_max}")
                    pause = input("\nEnter to continue>")
                    break

                elif investigate_option ==  "2":
                    push = input("On the desk there is a single red button\nPush the button\n1. Yes\n2. No\n>")
                    if push == "1":
                        if button_pressed == True:
                            print("Nothing happened")
                        else:
                            print("you hear the sound of flames for a moment then it stops")
                            button_pressed = True
                        pause = input("\nEnter to continue>")
                    break

                elif investigate_option ==  "3":
                    plaque =input("As you walk to the tubes you notice there is some sort of slide on the right slide of the room\nThe Three large tubes each have a plaque near the bottom\nThe 2 tubes on the end have a stagnant liquid inside but the middle one is brooken opend and empty\n\nlook at the plaques\n1. Yes\n2. No")
                    slide_discovered = True
                    if plaque == "1":
                        print("the only plaque that is readable is the middle one\nIt says 002 Simon")
                        monster_name = "002 Simon"
                        pause = input("\nEnter to continue>")
                    break
                elif investigate_option ==  "4":
                    break
                else:
                    error()
            half_dash()
            room_lab()
        elif lab_option == "2":
            room_nest()
        elif lab_option == "cs":
            status()
            room_lab
    elif slide_discovered == True:
        print("The lab remains\n3 tubes, 1 desk, filing cabinets, and a slide")
        lab_option = input(f"\nCurrent options:\n1. Investigate\n2. return to the {nest_room_name}\n3. slide down the slide\ncs. check status\n>")
        if lab_option == "1":
            half_dash()
            while True:
                investigate_option = input("\nInvestigate options:\n1. Filing cabinets\n2. Desk\n3. Tubes\n4. Cancel\n>")
                half_dash()

                if investigate_option ==  "1":
                    print("There are large amounts ouf filing cabinets")
                    if button_pressed == False:
                        print("The filing cabinets are filled with papers\nAn interesting paper says that:\n\"loot 002 to find somthing awesome")
                    elif button_pressed == True:
                        print("In the filing cabinets all you see is ash\n\nHowever\nAlso in the cabinets you find somthing peculiar\n\nYou find a spinning frog in a camouflage hat")
                        camo_frog = True
                        frog_count += 1
                        print(f"Frogs found {frog_count}/{frog_max}")
                    pause = input("\nEnter to continue>")
                    break

                elif investigate_option ==  "2":
                    push = input("On the desk there is a single red button\nPush the button\n1. Yes\n2. No")
                    if push == "1":
                        if button_pressed == True:
                            print("Nothing happened")
                        else:
                            print("you hear the sound of flames for a moment then it stops")
                            button_pressed = True
                        pause = input("\nEnter to continue>")
                    break

                elif investigate_option ==  "3":
                    plaque =("The Three large tubes each have a plaque near the bottom\nThe 2 tubes on the end have a stagnant liquid inside but the middle one is brooken opend and empty\n\nlook at the plaques\n1. Yes\n2. No")
                    if plaque == "1":
                        print("the only plaque that is readable is the middle one\nIt says 002 Simon")
                        monster_name = "002 Simon"
                        pause = input("\nEnter to continue>")
                    break
                elif investigate_option ==  "4":
                    break
                else:
                    error()
            half_dash()
            room_lab()
        elif lab_option == "2":
            room_nest()
        elif lab_option =="3":
            event_slide()
        elif lab_option == "cs":
            status()
            room_lab


#Boss fight code
def tool_damage_calculator():
    global current_tool
    if current_tool == None:
        return 10
    elif current_tool == "pickaxe":
        return 20
    elif current_tool == "axe":
        return 25  
def boss_status():
    global current_health, max_health, monster_health
    dashes()
    print(f"{monster_name}")
    print(f"{monster_health}/250")
    print(" - "*17)
    print(f"Health: {current_health}/{max_health}")
    print(f"Weapon: {current_tool}")
    print(" - "*17)
def cooldown_error(): print("Error: Cannot use skill while on cooldown"); print(" - "*17) ;player_turn()
def player_turn():
    global current_tool, dodge_cooldown
    print("Actions:")
    print( (f"1. Hit with {f'{current_tool}' if current_tool != None else 'nothing'} and prepare to dodge" if dodge_cooldown <= 0 else f"Dodge on cooldown: active for {dodge_active} turns   cooldown remaining: {dodge_cooldown} turns") )
    print( (f"2. Hit with {f'{current_tool}' if current_tool != None else 'nothing'} and prepare to block" if block_cooldown <= 0 else f"block on cooldown: active for {block_active} turns   cooldown remaining: {block_cooldown} turns") )
    print(f"3. Just attack with {f'{current_tool}' if current_tool != None else 'nothing'}")
    action = input("\n>")
    if action == "1":
        if dodge_cooldown >0: cooldown_error(); player_turn()
        else: attack(); dodge(); print("- - "*13)
    elif action == "2":
        if block_cooldown >0: cooldown_error(); player_turn()
        else: attack(); block(); print("- - "*13)
    elif action == "3": attack(); print("- - "*13)
    else: error(); player_turn()
def attack():
    global damage, monster_health, monster_name, monster_defense
    hit_damage = (random.randint(-5,5)+damage)//monster_defense
    print(f"You hit {monster_name} for {hit_damage} damage")
    monster_health -= hit_damage
def dodge():
    global dodge_cooldown, dodge_active
    dodge_cooldown = 5
    dodge_active = 3
    print("You got ready to dodge (Increased chance to dodge enemy attacks next 3 turns)")
    pass
def block():
    global block_cooldown, block_active
    block_cooldown = 3
    block_active = 1
    print("You got ready to block (Take no damage next turn)")
def monster_turn():
    global monster_defense
    monster_defense = 1
    monster_action = random.randint(0,(1 if monster_health < 125 else 0))
    if monster_action == 0:
        monster_attack()
    elif monster_action == 1:
        print("The monster readies itself for an attack")
        monster_defense = 2
def monster_attack():
    global current_health, dodge_active, block_active, monster_name, monster_health, damage
    hit_damage = (10+random.randint(-5,5))
    if block_active:
        print(f"{monster_name} attempts to stike\nYou manage to block it")
        if random.randint(0,1): 
            parry_damage = (random.randint(-5,5)+damage)
            print(f"In addition you parry dealing {parry_damage} damage")
            monster_health -= parry_damage
    elif random.randint(-3,dodge_active*2) >= 0:
        print(f"{monster_name} attempts to strike\nYou managed to dodge in time")
    else:
        print(f"{monster_name} manages to strike you dealing {hit_damage} damage")
        current_health -= hit_damage
def turn_complete():
    global dodge_active, dodge_cooldown, block_active, block_cooldown
    if dodge_active > 0:
        dodge_active -= 1
    if dodge_cooldown > 0:
        dodge_cooldown -= 1
    if block_active > 0:
        block_active -= 1
    elif block_cooldown > 0:
        block_cooldown -= 1
def boss_fight():
    global damage, monster_health, monster_name, current_health
    damage = tool_damage_calculator()
    while monster_health > 0 and current_health >0:
        input("Enter to continue>")
        boss_status()
        if random.randint(1,2) == 1: print("Your turn"); player_turn()
        else: print(f"{monster_name}'s turn"); monster_turn()
        turn_complete()
    if current_health <=0:
        print("death")
        load()
    elif monster_health <= 0:
        dashes()
        print("The monster releses one last screech as it falls to the ground limp")
        event_victory_nest()
def event_victory_nest():
    global frog_count, frog_max, peculiar_frog
    print("The monster remains dead on the ground\nThe path to the lab has collapsed")
    loot = input("\nCurrent option:\n1. return to the main room\ncs. Check status\n>")
    if loot == "1":
        dashes()
        event_victory_main_room()
    elif loot == "cs":
        status()
        half_dash()
        event_victory_nest()
    elif "loot" in loot.lower():
        print("\nYou find something perfect within the corpse\n\nYou find a spinning frog in a peculiar hat")
        peculiar_frog = True
        frog_count += 1
        print(f"Frogs found {frog_count}/{frog_max}")
        pause = input("\nEnter to continue>")
    else:
        error()
        dashes()
        event_victory_nest()
def event_victory_main_room():
    global frog_count, frog_max
    print("The path to the nest collapses behind you\nYou are in the main room\nThe tunnels to the other rooms have collapsed\nThe boulders blocking the entrace are clear\nTHe light from the entrace is blinding")
    if frog_count == frog_max:
        print(f"Approching the entrace suddenly {frog_max} spinning frogs appear in front of you")
        if "yes" in input("Accept their gift\n>").lower():
            ending_hat()
        else:
            dashes()
            print("The frogs stop spinning\ndissapointment shows on their faces\nA single tear falls from the closest frog\nThe frogs disapear before you can react\n")
            event_victory_main_room()
    else:
        ending_cave_3()


#Endings
def ending_dash():
    print("\n"*5)
    print("*"*51)
    print("***************************************************\n")
def ending_death(cause,text):
    ending_dash()
    print(f"You died")
    print(f"cause of death:")
    print(cause)
    print(text)
    print("***************************************************")
    print("\n"*5)
    dashes()
    while True:
        restart = input("Type 1 to restart\nType 2 to return to menu\n>")
        if restart == "1":
            startup()
        if restart == "2":
            menu()
        if restart == "3":
            sys.exit("see you later")
        else:
            half_dash()
            print("Rather than not typing 1\nyou can type 3 to end game")
    ending_death(death_cause, death_text)
def ending():
    pause = input("\nEnter to continue>")
    dashes()
    print("YOU WIN (kinda)\nthanks for playing\n")
    restart = input("Play Again?\n1. yes\n2. no\n3. return to menu\n>")
    if restart == "1":
        startup()
    elif restart == "2":
        sys.exit("see you later")        
    elif restart == "3":
        menu()
    else:
        print("i'll take that as a no")
        sys.exit("see you later")
def ending_forest_1():
    dashes()
    print("You find yourself in a small town\nYour town\nOn your doorstep your parents stand there expectantly\n")
    while True:
        var_32147836412 = input("Go Home?\n1. Yes\n2. No\n>")
        if var_32147836412 == "1":
            print(" - "*17)
            break
        else:
            half_dash()
            print("Take your time\nEnter 1 when ready\n")


    ending_dash()
    print("                Ending obtained:                   ")
    print("                     Home\n                        ")
    print("            You found your way home                ")
    print("      or.. at least you think you're home.\n        ")
    print("***************************************************")
    ending()
    print("\n"*5)
def ending_forest_2():
    dashes()
    print("You find yourself in a small town\nYour town\nNobody is here but you're to tired to care\nYou head strait to your bed\n")
    while True:
        var_32147836412 = input("Go to sleep?\n1. Yes\n2. No\n>")
        if var_32147836412 == "1":
            print(" - "*17)
            break
        else:
            half_dash()
            print("Take your time\nEnter 1 when ready\n")


    ending_dash()
    print("                Ending obtained:                   ")
    print("                    Alone\n                        ")
    print("         time for some well needed rest            ")
    print("    maybe tomorrow you'll look for your family.     ")
    print("***************************************************")
    print("\n"*5)
    ending()
def ending_forest_3():
    dashes()
    print("You find yourself in a small town\nYour town\nthe corpes of everyone you knew lay everywhere\nno doubt the monster's fault\nYou dont think you can handle this anymore\n")
    while True:
        var_32147836412 = input("wake up?\n1. Yes\n2. No\n>")
        if var_32147836412 == "1":
            print(" - "*17)
            break
        else:
            dashes()
            print("You head strait to your bed\n")
            while True:
                var_32147836412 = input("Go to sleep?\n1. Yes\n2. No\n>")
                if var_32147836412 == "1":
                    print(" - "*17)
                    break
                else:
                    half_dash()
                    print("Take your time\nEnter 1 when ready\n")


            ending_dash()
            print("                Ending obtained:                   ")
            print("                    Alone\n                        ")
            print("         time for some well needed rest            ")
            print("    maybe tomorrow you'll look for your family.     ")
            print("***************************************************")
            print("\n"*5)
            ending()

    ending_dash()
    print("this is the end then                               ")
    print("                  you slam you head into a rock    ")
    print("maybe that will stop this                          ")
    print("   maybe this nightmare will end.                 \n")
    print("                 Dream No More                     ")
    print("                Ending obtained\n                  ")
    print("***************************************************")
    print("\n"*5)
    ending()
def ending_cave_1():
    dashes()
    print("You follow the path\nYou have no idea how long it has been but the sun is rising\n you see a town on the horizon\n")
    while True:
        var_32147836412 = input("Escape?\n1. Yes\n2. No\n>")
        if var_32147836412 == "1":
            print(" - "*17)
            break
        else:
            half_dash()
            print("You dont actually have a choice\n")

    ending_dash()
    print("                Ending obtained:                   ")
    print("                     Escape\n                      ")
    print("        You left the wretched cave behind          ")
    print("           but is this really the end\n            ")
    print("***************************************************")
    ending()
    print("\n"*5)
def ending_cave_2():
    dashes()
    print("You left the path\nYou dont know how long ago that was\nYou hope you find civilization soon\n")
    while True:
        var_32147836412 = input("continue?\n1. Yes\n2. No\n>")
        if var_32147836412 == "1":
            print(" - "*17)
            break
        else:
            print(" - "*17)
            print("The illusion of choice")
            break

    ending_dash()
    print("                Ending obtained:                   ")
    print("                    Wanderer\n                      ")
    print("       You will forever wander this forest          ")
    print("         next time dont leave the path\n            ")
    print("***************************************************")
    ending()
    print("\n"*5)
def ending_cave_3():
    dashes()
    print("The light outside the cave is too brght for you to see\n")
    while True:
        var_32147836412 = input("Leave the cave\n1. Yes\n2. No\n>")
        if var_32147836412 == "1":
            print(" - "*17)
            break
        else:
            half_dash()
            print("It truly is your only option\n")

    ending_dash()
    print("                Ending obtained:                   ")
    print("                    Monster\n                      ")
    print("   the scourge of the cave has been defeated       ")
    print("      Maybe you can find your way home now\n       ")
    print("***************************************************")
    ending()
    print("\n"*5)
def ending_hat():
    dashes()
    print("From the sky floats down a hat\nIt is perfect\nSo perfect you jolt upright\n\nand hit your head on the upper bunk of your bed")
    pause = input("\nEnter to continue>")
    ending_dash()
    print("                Ending obtained:                   ")
    print("                The True Ending\n                  ")
    print("        You woke up the nightmare cave             ")
    print("             but What did it cost\n                ")
    print("***************************************************")
    ending()
    print("\n"*5)
def ending_secret():
    dashes()
    print("You hear a ringing all around\nYou wake up\nYour alarm is going off\n")
    pause = input("\nEnter to continue>")
    ending_dash()
    print("                Ending obtained:                   ")
    print("               The Secret Ending\n                 ")
    print("   You wasted so much time your alarm went off     ")
    print("If I had to guess I would say you are owen Rossing\n")
    print("***************************************************")
    ending()
    print("\n"*5)

#Start the game
menu()