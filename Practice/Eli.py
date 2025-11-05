import os, random, time
from enum import Enum


end_buffer = False
def restart():
    global fih, end_buffer
    fih = Fih(
        luck=random.randrange(10, 200)/100 # 0.1 -> 2
    )
    end_buffer = False
    
    prompt_encounter(encounter_handler.start_life)
    

class Encounter:
        def __init__(self, prompt: str, options: list):
            self.prompt = prompt
            self.options = options

class Location(Enum):
    HOME = "home"
    WATER_SURFACE = "the ocean waters"
    REEF = "the reef"
    INNER_REEF = "the inner reef"
    CAVE = "the cave"
    INNER_CAVE = "the inner cave"

invalid_random_locs = [
    Location.HOME,
    Location.INNER_REEF,
    Location.INNER_CAVE
]

def get_inner_location(loc: Location):
    match loc:
        case Location.CAVE: return Location.INNER_CAVE
        case Location.REEF: return Location.INNER_REEF
        case _: return loc
def get_outer_location(inner: Location):
    match inner:
        case Location.INNER_CAVE: return Location.CAVE
        case Location.INNER_REEF: return Location.REEF
        case _: return inner


class Fih:
    def __init__(self, luck):
        # Birth variables
        self.luck = luck
        
        # Active variables
        self.hunger = 1
        self.food_types = ["plankton"]
        self.health = 0.5
        self.energy = 0.5
        self.age = 0    # Years, 0 to 5
        
        self.location = Location.HOME
        self.depth = 0
        self.visited_locations = set()
        self.migration_stage = False
        
        # Legacy variables
        self.boldness = 0
        self.sociability = 0
    
    
    def give_socio(self, value):
        for _ in range(value):
            self.sociability += (0.5 * pow(2, -1*self.sociability/3))
    
    def give_bold(self, value):
        for _ in range(value):
            self.boldness += (0.5 * pow(2, -1*self.boldness/5))
    
    def update(self):
        global end_buffer, iterations_since_last_random
        
        iterations_since_last_random += 1
        
        self.hunger -= 0.075
        self.energy -= 0.08
        self.energy += (
            (-24.5 * pow(self.hunger, 2) + (9.8*self.hunger) - 0.98) if self.hunger <= 0.2     # y = -24.5x^2 + 9.8x - 0.98
            else ((-0.125*pow(self.hunger, 2) + (0.275 * self.hunger) - 0.05)*(pow(1/2, self.energy)))   # y = (-0.125x^2 + 0.275x - 0.05)((1/2)^z) where z = self.energy
        )   # https://www.desmos.com/calculator/sgqeyniscu
        
        self.age += 0.1
        
        self.luck = max(0.1, self.luck)
        self.boldness = max(0.1, self.boldness)
        self.sociability = max(0.1, self.sociability)
        
        if self.energy <= 0:
            end_buffer = True
            prompt_encounter(exit_prompt)
            
fih = Fih(
    luck=random.randrange(10, 200)/100 # 0.1 -> 2
)

exit_prompt = Encounter(
        "-- GAME OVER --",
        [
            ("Restart", restart),
            ("Quit", quit)
        ]
    )

#region Encounter functions

iterations_since_last_random = 0

class RandomEncounters:
    def __init__(self):
        self.encounters = dict()
        
        self.register_encounter(self.octopus_attack, 0)    # Severely nerfed; it was happening EVERY. SINGLE. RANDOM ENCOUNTER. Seriously almost clocked my monitor.
        self.register_encounter(self.steal_food, 0.25)
        self.register_encounter(self.find_treasure, 1)
    
    def register_encounter(self, enc, positivity:float):
        self.encounters.update({
            positivity: enc
        })
    
    def get_encounter(self, value):
        encounter_list = [(e, self.encounters.get(e)) for e in self.encounters]
        dist = [abs(value-v[0]) for v in encounter_list]
        
        return encounter_list[dist.index(min(dist))][1]
    
    
    def octopus_attack(self):
        global fih
        win_count = 0
        for i in range(5):
            wait_msg = "An octopus waits to attack..." if i == 0 else "The octopus prepares itself"
            if quick_time(
                wait_msg=wait_msg,
                attack_msg=f"The octopus lunges ({i}/5)",
                time_limit=(1/2)
            ):
                win_count += 1
                
        if win_count > 3:
            prompt_encounter(encounter_handler.confirmation(
                "You won against the octopus. You are tired, but alive.",
            ), update=False)
        else:
            prompt_encounter(encounter_handler.confirmation(
                "You got away, but barely. You are very tired."
            ), update=False)
        win_count = 0
        
    def steal_food(self):
        global fih
        fih.energy -= 0.1
        fih.hunger = 1
        prompt_encounter(
            encounter_handler.confirmation(
                "While gorging yourself on a stash of food you found, you see its owner approaching.\nYou run with the food, tired, but satiated."
                ), update=False)
        
    def find_treasure(self):
        global fih
        fih.energy += 0.3
        prompt_encounter(
            encounter_handler.confirmation
            ("While exploring, you find treasure!\nYou are ecstatic, and feel a burst of energy through your fishy veins."
            ), update=False)
random_encounters = RandomEncounters()

def prompt_ending(msg:str):
    bold = fih.boldness > 0.5
    sociable = fih.sociability > 0.5
    
    ending = \
        "gregarious" if bold and sociable else \
        ("intrepid" if bold and not sociable else \
        ("amiable" if not bold and sociable else \
        "reclusive"))
    
    prompt_encounter(Encounter(
        f"{msg}\n\nThe {ending} ending.",
        options=[
            ("Restart", restart),
            ("Quit", quit)
        ]
    ),stats=False, update=False, can_rand=False)

def migrate(with_bubbles:bool):
    if with_bubbles:
        fih.give_socio(1)
        prompt_ending(
            "You leave the reef with Bubbles, Ripple, Ziggy, and Finn.\n"+
            "You hardly notice as your life disappears behind you, but you aren't bothered by it."
        )
    else:
        prompt_ending(
            "Deciding to join the rest of the school, you leave your home.\n"+
            "All you've ever known disappears as you swim away from your home,\n"+
            "past the cave, past the farthest edges of the reef, and into the open water."
        )

def explore():
    fih.depth = min(6, fih.depth+1)
    if fih.depth == 1:
        fih.location = getattr(Location, random.choice(list([l for l in Location if l not in invalid_random_locs])).name)
    elif fih.depth > 5:
        fih.location = get_inner_location(fih.location)
        
        if fih.location not in fih.visited_locations:
            prompt_encounter(encounter_handler.get_welcome_encounter(fih.location), can_rand=False)
        
    fih.visited_locations.add(fih.location)
    prompt_encounter(encounter_handler.get_wait_encounter())
    
def turn_back(wait: bool = True):
    fih.depth = max(0, fih.depth-1)
    if fih.depth == 0:
        fih.location = Location.HOME
    elif fih.depth == 5:
        fih.location = get_outer_location(fih.location)
    if wait: prompt_encounter(encounter_handler.get_wait_encounter())   # ONLY SET TO FALSE IF YOU'RE PROMPTING A DIFFERENT ENCOUNTER IN PLACE OF 'WAIT'

def eat_challenge(fighting: bool):
    if fighting:
        fih.give_bold(1)
        chance_lose = 0.5 / (fih.luck+1) / (fih.energy+1)
        if random.random() <= chance_lose:
            fih.energy -= 0.2
            prompt_encounter(encounter_handler.confirmation("You lose the fight and the food. You are still hungry, and you have less energy."))
        else:
            fih.hunger = 1
            fih.energy -= 0.15
            prompt_encounter(encounter_handler.confirmation("You win the fight and the food. You are satiated, but you have less energy."))
    else:
        prompt_encounter(encounter_handler.confirmation("You surrender the food. Nothing changes."))

def eat():
    global fih
    chance_sick = (0.25 / fih.luck) / fih.health
    chance_fight = (0.1 / fih.luck) / fih.sociability
    
    match fih.age:
        case n if n <= 0.5:
            fih.food_types = ["plankton", "fleas", "copepods"]
        case n if 0.5 < n <= 1.5:
            fih.food_types = ["worms", "larvae", "nymphs"]
        case n if 1.5 < n <= 3:
            fih.food_types = ["sowbugs", "worms", "snail"]
        case _:
            fih.food_types = ["minnow", "sunfish", "crayfish"]
            
    
    if random.random() <= chance_sick:
        fih.hunger = 1
        fih.energy -= 0.2
        prompt_encounter(encounter_handler.confirmation(f"The {random.choice(fih.food_types)} you ate makes you feel ill.\nYou are satiated, but have less energy."))
    elif random.random() <= chance_fight:
        prompt_encounter(encounter_handler.eat_fight)
    else:
        fih.hunger = 1
        prompt_encounter(encounter_handler.confirmation(f"You eat the {random.choice(fih.food_types)}. You are satiated"))

def rest():
    fih.energy = max(1, fih.energy)
    prompt_encounter(encounter_handler.confirmation("You feel rested."))
    
def quick_time(wait_msg, attack_msg, time_limit):
    start_time = time.time()
    os.system('cls')
    print(wait_msg)
    
    def _fight():
        return time.time() - start_time <= time_limit
    
    while (time.time() - start_time < random.randrange(2,5)):
        pass
    
    start_time = time.time()    # resets start_time to be used differently later.
    return prompt_encounter(Encounter(
        prompt=attack_msg,
        options=[
            (f"Attack ({round(time_limit,1)}s)", _fight)
        ]
    ), update=False, can_rand=False, stats=False)
    
#endregion
    
    
class Encounters:
    def __init__(self):
        # Simple encounters that are invariable are placed here.
        
        self.start_life = Encounter(
            "You are born in a nest of pebbles.",
            [
                ("Explore around", explore),
                ("Eat", eat),
                ("Rest", rest)
            ])
        self.eat_fight = Encounter(
            f"You go for the {random.choice(fih.food_types)}, but are challenged.",
            [
                ("Fight", lambda: eat_challenge(True)),
                ("Surrender", lambda: eat_challenge(False))
            ])
        
    def get_wait_encounter(self, additional_msg: str = ""):
        options = [
            ("Eat", eat),
        ]
        turn_back_msg = "Go home" if fih.depth == 1 else "Turn back"
        if fih.depth > 0: options.append((turn_back_msg, turn_back)) 
        if fih.depth < 5: options.insert(0, ("Explore", explore))
        
        match fih.location:
            case Location.HOME:
                options.extend([
                    ("Rest", rest),
                ])
                if fih.migration_stage:
                    options.extend([
                        ("Settle", lambda: prompt_ending(
                            "You decide to stay home. Everyone you know migrates."
                        ))
                    ])
            case Location.REEF:
                if fih.depth == 5:
                    options.extend([
                        ("Rest", rest),
                        ("Travel to Inner Reef", explore)
                    ])
                elif fih.depth == 6:
                    options.extend([
                    ])
            case Location.CAVE:
                if fih.depth == 5:
                    options.extend([
                        ("Rest", rest),
                        ("Travel to Inner Cave", explore)
                    ])
            case Location.INNER_CAVE:
                if fih.migration_stage:
                        options.extend([
                            ("Settle", lambda: prompt_ending(
                                "You decide to settle in the cave. Everyone you know migrates."
                            ))
                        ])
            case Location.WATER_SURFACE:
                if fih.depth >= 5 and fih.migration_stage:
                    options.extend([
                        ("Migrate", lambda: migrate(False))
                    ])
        
        return Encounter(
            f"{additional_msg}{"\n\n" if additional_msg != "" else ""}You are {"alone at" if fih.depth != 5 else "deep in"} {fih.location.value}",
            options
        )
        
    def confirmation(self, msg, stats:bool=True, wait:bool=True):    # ONLY SET WAIT TO FALSE IF YOU'RE PROMPTING A DIFFERENT ENCOUNTER IN PLACE OF 'WAIT'
        return Encounter(
            msg,
            [
                ("Continue", (lambda: prompt_encounter(self.get_wait_encounter(), stats=stats)) if wait else lambda: True)
            ]
        )
    
    def dialogue(self, name: str, msg: str, options: list, last_response:str=""):
        _lr = f'"{last_response}"\n\n' if last_response != "" else ""
        _name = f'{name}:\n    ' if name != "" else ""
        enc = Encounter(
            f'{_lr}{_name}{msg}',
            options
        )
        return enc
    
    def get_welcome_encounter(self, loc: Location):
        
        def fall_back():
            turn_back(False)
            add_msg = ""
            match loc:
                case Location.INNER_CAVE: add_msg = "You leave the inner cave, choosing not to confront Ivan."
                case Location.INNER_REEF: add_msg = "You leave the inner reef, put off by Bubbles's energy."
                case _: None
            prompt_encounter(encounter_handler.get_wait_encounter(add_msg), can_rand=False)
            
        def fight_ivan():
            global fih
            fih.give_bold(2)
            
            win_count = 0
            
            for i in range(4):
                if quick_time("Ivan gets ready to charge you...", "Ivan charges!", 1.5/(i+1)):    # 1.5/(i+1) means that the first quicktime will require 1.5 seconds, and the last will require 1.5/4.
                    win_count += 1
                    prompt_encounter(encounter_handler.confirmation("Ivan charges, but you dodge and land a hit.", wait=False), stats=False, update=False, can_rand=False)
                else:
                    prompt_encounter(encounter_handler.confirmation("You try to fight back, but Ivan lands a hit before you can make a move.", wait=False), stats=False, update=False, can_rand=False)
            if win_count >= 3:
                fih.visited_locations.add(fih.location)
                fih.give_bold(1)
                prompt_encounter(
                    encounter_handler.confirmation("You won the fight against Ivan, gaining access to the inner cave.")
                    , update=False, can_rand=False)
            else:
                fih.location = get_outer_location(fih.location)
                prompt_encounter(
                    encounter_handler.confirmation("You lost the fight against Ivan, so you flee the inner cave.")
                    , update=False, can_rand=False)
        
        def reject_bubbles():
            start_monologue(
                last_response="I don't think I want to leave just yet.",
                name="Bubbles",
                msgs=[
                    "Okay!",
                    "..."
                    "Bye, I guess."
                ], 
                options=[
                    ("Continue", lambda:True)
                ],
                wait = True
            )
        
        def follow_bubbles():
            global fih
            fih.give_socio(2)
            fih.migration_stage = True
            
            inquire_migration = lambda:start_monologue(
                last_response='What do you mean, "Migration"?',
                name = "Bubbles",
                msgs=[
                    "Oh... you don't know what the migration is?",
                    "Well, I have good news and bad news!",
                    "Bad news, everybody you know will be leaving soon...",
                    "Good news, you can come with!",
                    "We're all family here, and we travel together. That includes you!",
                    "We were actually just about to head out!",
                    "... if you'd like to leave, of course...\n(You can come back and migrate)"
                ],
                options=[
                    ("Go with Bubbles", lambda:migrate(True)),
                    ("Stay", reject_bubbles)
                ]
            )
            inquire_who = lambda:start_monologue(
                last_response='Who? You and your friends?',
                name = "Bubbles",
                msgs=[
                    "Well of course! But not just us.",
                    "Don't you know? Everybody is leaving.",
                    "You didn't think we'd all stay HERE, did you?",
                    "We're all family here, and we travel together. That includes you!",
                    "We were actually just about to head out!",
                    "... if you'd like to leave, of course...\n(You can come back and migrate)"
                ],
                options=[
                    ("Go with Bubbles", lambda:migrate(True)),
                    ("Stay", reject_bubbles)
                ]
            )
            
            #   Bubbles dialogue. Teaches about the migration / END GOAL
            start_monologue(
                name="Bubbles",
                msgs=[
                    "Aaaand here we are! These are my friends! :)",
                    "Say hi to our new friend, guys!"
                ],
                options=[
                    ("Continue", lambda: start_monologue(
                        name="",
                        msgs=[
                            "Ripple:\n    ...",
                            "Ziggy:\n    ...",
                            "Finn:\n    ...",
                        ],
                        options=[
                            ("Continue", lambda:start_monologue(
                                last_response="Uhh... hi.",
                                name="Bubbles",
                                msgs=[
                                    "heh...",
                                    "They're just a bit...",
                                    "...",
                                    "Nervous..."
                                ],
                                options=[
                                    ('"Nervous?"', lambda:start_monologue(
                                        last_response="Nervous?",
                                        name = "Bubbles",
                                        msgs=[
                                            "Yeah, yeah. Nervous...",
                                            "We all are, this is our first migration"
                                        ],
                                        options=[
                                            ('"Migration?"', inquire_migration),
                                            ('"We?', inquire_who)
                                        ]
                                        )),
                                    ("Run away", fall_back)
                                    ],
                            ))
                        ]
                    ))
                ]
            )
        
        match loc:
            case Location.INNER_CAVE:
                greeting = "Ivan"
                return self.dialogue(
                    name=greeting,
                    msg="Hey, I don't recognize you. You looking for trouble..?",
                    options=[
                        ("Confirm (fight)", lambda: 
                            prompt_encounter(
                                self.dialogue(
                                    name=greeting,
                                    last_response="Yeah. matter'a fact, I am.",
                                    msg="You don't wanna do this pal.",
                                    options=[
                                        ("Double down (fight)", fight_ivan),
                                        ("Fall back", fall_back)
                                    ]
                                ), update=False, can_rand=False
                            )),
                        ("Deny (passive)", lambda:
                            prompt_encounter(
                                self.dialogue(
                                    name=greeting,
                                    last_response="No, just passing through.",
                                    msg="Who do you think you are? Swim past me and you're losing a fin.",
                                    options=[
                                        ("Double down (swim past)", fight_ivan),
                                        ("Fall back", fall_back)
                                    ]
                                )
                            )),
                        ("Run", fall_back)
                        ])
            case Location.INNER_REEF:
                greeting = "Bubbles"
                return self.dialogue(
                    name=greeting,
                    msg="Hey there! My name's Bubbles! I don't believe we've met! Where'd you come from? What's your name? Do you want to meet my friends?",
                    options=[
                        ("Confirm (meet friends)", lambda: prompt_encounter(
                            self.dialogue(
                                name=greeting,
                                last_response="Oh- Okay, sure.",
                                msg="Yippie!! Come on, come on!!.",
                                options=[
                                    ("Follow (meet friends)", follow_bubbles),
                                    ("Stay behind (stay in inner reef)", lambda: prompt_encounter(encounter_handler.get_wait_encounter(), can_rand=False)),
                                    ("Leave inner reef", fall_back)
                                ]
                        ),stats=False, update=False, can_rand=False)),
                        ("Deny", fall_back)])
            case _: None    # Already happens by default; Just for clarity.
        
encounter_handler = Encounters()

def prompt_encounter(encounter:Encounter, stats:bool=True, update:bool=True, can_rand:bool=True):
    global fih, iterations_since_last_random
    if not end_buffer and update: fih.update()
    
    if can_rand \
    and random.randint(0, 100) <= 20*(fih.age/2) * (iterations_since_last_random-1)/6\
    and fih.location != Location.HOME\
    and fih.energy > 0.2:
        encounter_luck = (0.5 * fih.luck) + (float(random.randint(-40, 40))/100)
        rand_encounter = random_encounters.get_encounter(encounter_luck)
        iterations_since_last_random = 0
        rand_encounter()
        
    else:
        def get_response():
            os.system('cls')
            
            if stats:
                print(f"-- Stats --\n\
        Food   {(chr(9608) + " ") * int(fih.hunger//0.1)}\n\
        Energy {(chr(9608) + " ") * int(fih.energy//0.1)}\n\
        Age    {(chr(9608) + " ") * int(fih.age//0.5)}\n\n\
                ")
                
            print(encounter.prompt + "\n----------\n")    
            for i, option in enumerate(encounter.options):
                print(f"{i+1}) {option[0]}")
                
            response = input("\n>")
            try:
                _result = int(response)
                if 0 < _result <= len(encounter.options):
                    return _result
                raise IndexError
            except:
                return get_response()
        response = get_response()
        
        os.system('cls')
        return encounter.options[response-1][1]()

def start_monologue(name:str, msgs: list, options: list, wait:bool=False, last_response: str=""):
    for i, msg in enumerate(msgs):
        prompt_encounter(encounter_handler.dialogue(
            name=name,
            msg = msg,
            options = [("Continue",lambda: True)] if i+1 != len(msgs) else options,
            last_response=last_response
        ), stats=False, update=False, can_rand=False)
    if wait:
        prompt_encounter(encounter_handler.get_wait_encounter())

prompt_encounter(encounter_handler.start_life)

while True:
    prompt_encounter(exit_prompt)