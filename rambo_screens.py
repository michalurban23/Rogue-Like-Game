from os import system
from rambo_colors import *
from time import sleep
from colored import fg, bg, attr


def show_ascii_intro():
    '''
    Display initial ascii art with John Rambo
    '''
    system("clear")
    with open("intro.txt", "r") as file:
        rambo_ascii = file.readlines()
        i = 0
        for line in rambo_ascii:
            i += 1
            if i % 2 != 1:
                print(LPURPLE, line[:-1])


def show_main_menu():
    '''
    Main screen after intro. Redirects to other screens. Loops used for smart coloring
    '''
    while True:
        system("clear")
        print(RED + ascii_arts(0), RESET)
        print(BLUE + "\nEnter one of the following commands:\n")
        MENU = {"start": " - to start a new game",
                "howto": " - to learn how to play the game",
                "highscores": " - to display a highscore list",
                "about": " - to learn more about the authors",
                "exit": " - to leave the game (although you might regret it!)"}
        for text in MENU:
            print(RED + text + BLUE + MENU[text])
        choice = proper_input_choice()
        if choice == "start":
            return


def proper_input_choice():
    '''
    Checks user input to match the commands. Will continue to ask until proper answer given
    '''
    choice = input()
    if choice.lower() == "start":
        return choice
    elif choice.lower() == "howto":
        show_rules()
    elif choice.lower() == "highscores":
        show_highscores()
    elif choice.lower() == "about":
        show_credits()
    elif choice.lower() == "exit":
        exit()


def start_game():
    '''
    A plot initiation, will lead to an actuall game board
    '''
    system("clear")
    print(UNDERLINE + "\nGood day soldier!\n" + RESET)
    sleep(1)
    print(LPURPLE + ascii_arts(5) + RESET)
    print(BLUE + "This is " + RED + "Colonel Samuel Trautman" + BLUE + " from US Marine Coorps.\n")
    sleep(2)
    print("As a part of our agreement for freeing you from prison, you are now due to perform a special",
          "\noperation for your country. There has been rumours about Vietnamese cooperating with Soviets",
          "\nand keeping our soldiers prisoners at their camp. You task is to travel to a jungle, perform",
          "\na reckon, confirm our suspicions with photographies and get to the extraction point to return home.\n")
    sleep(5)
    print("Under any circumstances," + RED + " do NOT interact with our POW's or enemies.\n")
    sleep(3)
    print(BLUE + "Good luck soldier, I expect everything goes swift. After all, you're our most renown veteran\n")
    sleep(2)
    print("Godspeed!\n\n")
    sleep(1)
    while True:
        start = input("Type 'start' to begin your adventure\n")
        if start == 'start':
            break


def create_character():
    '''
    Allows user to choose a few characteristics of a hero. Returnts them for future use
    '''
    hero = []
    system("clear")
    print(RED + "\nWelcome adventurer\n")
    print(BLUE + "\nAs we all well know, John Rambo is an ultimate killing machine\n")
    print("\nHowever, even a perfect machine can be adjusted. Here you can customize our hero in few steps\n")
    input("\nPress enter to continue\n")
    system("clear")

    skins = {"1": bg('white')+"\b",
             "2": bg('yellow')+"\b",
             "3": bg('light_sky_blue_3a')+"\b",
             "4": bg('indian_red_1a')+"\b",
             "5": bg('light_goldenrod_2a')+"\b"}
    print(UNDERLINE + "\nI. Choose your skin color\n" + RESET)
    print(BLUE + "Pick one of the following:")
    for key in skins:
        print("\n" + key + ")  " + skins[key] + 20*" " + attr('reset') + BLUE)
    while True:
        skin = input("\nSelect number: ")
        if skin in ["1", "2", "3", "4", "5"]:
            system("clear")
            break
    hero.append(skins[skin])

    avatars = {"1": fg('red')+"\b"+chr(920),
               "2": fg('red')+"\b"+"@",
               "3": fg('red')+"\b"+"$",
               "4": fg('red')+"\b"+chr(922),
               "5": fg('red')+"\b"+"&"}
    print(UNDERLINE + "\nII. Choose your avatar\n" + RESET)
    print(BLUE + "Pick one of the following:")
    for key in avatars:
        print("\n" + key + ")   " + skins[skin] + avatars[key] + attr('reset') + BLUE)
    while True:
        avatar = input("\nSelect number: ")
        if avatar in ["1", "2", "3", "4", "5"]:
            system("clear")
            break
    hero.append(avatars[avatar])

    skills = {"Spotter": "Increased sight radius (by +20%)",
              "Sniper": "Increased shooting distance (by +1 tile)",
              "Survivor": "Increased vitality (+1 starting life)",
              "Swimmer": "Decreased energy loss in water (by 25%)",
              "Veteran": "Incresed exp from killing enemies (by 25%)",
              "Athlete": "Increased energy regeneration (by 50%)",
              "Camper": "Incresed maximum carry (by 15 lbs)",
              "Smartass": "Easier time with riddles (+3 attempts)",
              "Thief": "Starts a game with a universal key (keys +1)"}
    print(UNDERLINE + "\nIII. Choose your preferenced abilities\n" + RESET)
    print(BLUE + "Pick three out of the following:")
    for key in skills:
        print("\n" + RED + key + " - " + BLUE + skills[key])
    while True:
        skill = input("\nSelect a skill (e.g. 'ninja'): ").title()
        if skill in skills:
            hero.append(skill)
            print(RED + "Rambo is now a", skill + "!" + BLUE)
            del skills[skill.title()]
        else:
            print("\nNot a valid skill (or already taken)\n")
        if len(skills) == 6:
            break

    input("\nYou are ready. Press enter for a mission briefing")
    return(hero)


def show_highscores():
    '''
    Reads highscores from a file (or prompts its missing). Displays output in an amazing table.
    A lot of smart coloring inside
    '''
    system("clear")
    try:
        file = open("highscores.txt")
    except FileNotFoundError:
        print("Couldn't find a hiscores.txt file in game directory")
    else:
        highscores = file.readlines()
    print(RED + ascii_arts(1), RESET)
    HASH = GRAY + "*" + BLUE
    HORIZONTAL_BAR = (HASH + RED).join([" Player Name ", " Hero Level ", " Time ", " Completion ", " Enemies Killed "])
    print(BLUE + "\n\n\nHere you can find a list of brave heroes how completed the game:\n")
    print(HASH * 65)
    print(HASH + RED + HORIZONTAL_BAR + HASH)
    print(HASH * 65)
    for entry in highscores:
        item = entry.rstrip("\n").split(",")
        print(HASH + HASH.join(["{:^13}", "{:^12}", "{:^6}", "{:^12}",
                                "{:^16}"]).format(item[0], item[1], item[2], item[3], item[4]) + HASH)
    print(HASH * 65 + BLUE)
    input("\nPress enter to go back to menu ")


def show_credits():
    '''
    Displays information about best programmers on planet earth, creators of this astounding masterpiece
    '''
    system("clear")
    print(RED + ascii_arts(2))
    print(UNDERLINE + "\nMichał Urban\n" + RESET)
    print(BLUE + "O Mój Boże, jaki on jest dobry")
    print(UNDERLINE + "\nPaweł Rybka\n" + RESET)
    print(BLUE + "Zwycięzca I edycji 'Jak oni kodzą'. Kozak.")
    print(BROWN + "\n\n\nRambo Reborn", u"\u2122", "@ Kraków, 2017")
    input(BLUE + "\nPress enter to go back to menu ")


def show_rules():
    '''
    Displays information about key mapping
    '''
    system("clear")
    print(RED + ascii_arts(3), RESET)
    print(BLUE + "In rambo adventures game you are able to move, fight and interact with enviroment")
    print(UNDERLINE + "\nMovement:" + RESET)
    print(BLUE + "W - move up")
    print("S - move down")
    print("A - move left:")
    print("D - move right:")
    print(UNDERLINE + "\nFighting:" + RESET)
    print(BLUE + "F - shoot")
    print(UNDERLINE + "\nOther:" + RESET)
    print(BLUE + "Q - quits the game")
    print("I - shows extended inventory")
    print("E - interact with doors and other objects\n")
    input("Press enter to go back to menu ")


def ascii_arts(n):
    '''
    Reads appropriate ascii arts for further display in different screens
    '''
    with open("ascii_arts.txt", "r") as file:
        ascii_arts = file.read().split(',')
        arts = []
        for element in ascii_arts:
            arts.append(element)
    return arts[n]
