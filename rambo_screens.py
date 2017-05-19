from os import system
from rambo_colors import *
from time import sleep


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
    sleep(2)
    print(LPURPLE + ascii_arts(5) + RESET)
    print(BLUE + "This is " + RED + "Colonel Samuel Trautman" + BLUE + " from US Marine Coorps.\n")
    sleep(3)
    print("As a part of our agreement for freeing you from prison, you are now due to perform a special",
          "\noperation for your country. There has been rumours about Vietnamese cooperating with Soviets",
          "\nand keeping our soldiers prisoners at their camp. You task is to travel to a jungle, perform",
          "\na reckon, confirm our suspicions with photographies and get to the extraction point to return home.\n")
    sleep(7)
    print("Under any circumstances," + RED + " do NOT interact with our POW's or enemies.\n")
    sleep(4)
    print(BLUE + "Good luck soldier, I expect everything goes swift. After all, you're our most renown veteran\n")
    sleep(3)
    print("Godspeed!\n\n")
    sleep(2)
    while True:
        start = input("Type 'start' to begin your adventure\n")
        if start == 'start':
            break


def show_1st_cutscene():
    '''
    1st cut-scene
    '''
    system("clear")
    print(BLUE + "You have succesfully traveled through vientamese jungle and found a passage")
    print("Now it's time to infiltrate the camp where our POW's are kept\n")
    input("Press enter: ")


def show_2nd_cutscene():
    '''
    2nd cut-scene
    '''
    system("clear")
    print(BLUE + "As predicted, camp was full of captured american soldiers.")
    print("To help them, despite the orders, you must now clear the nearby fortress, full of soviet soldiers\n")
    input("Press enter: ")


def show_3rd_cutscene():
    '''
    3rd cut-scene
    '''
    system("clear")
    print(BLUE + "You have defeated soviets and freed prisoners. But the HQ is not happy.")
    print("They send general Marshall Murdock to deal with you. He is not your every-day oppponent though\n")
    input("Press enter: ")


def create_character():
    '''
    Allows user to choose a few characteristics of a hero. Returns them for future use
    '''
    hero_customization = []
    system("clear")
    print(RED + "\nWelcome adventurer\n")
    print(BLUE + "\nAs we all well know, John Rambo is an ultimate killing machine\n")
    print("\nHowever, even a perfect machine can be adjusted. Here you can customize our hero in few steps\n")
    input("\nPress enter to continue\n")
    system("clear")

    skins = {"1": 'white',
             "2": 'yellow',
             "3": 'light_sky_blue_3a',
             "4": 'indian_red_1a',
             "5": 'light_goldenrod_2a'}
    print(UNDERLINE + "\nI. Choose your skin color\n" + RESET)
    print(BLUE + "Pick one of the following:")
    for key in sorted(skins):
        print("\n" + key + ")  " + bg(skins[key])+"\b" + 20*" " + attr('reset') + BLUE)
    while True:
        skin = input("\nSelect number: ")
        if skin in ["1", "2", "3", "4", "5"]:
            system("clear")
            break
    hero_customization.append(skins[skin])

    avatars = {"1": fg('red')+"\b"+chr(920),
               "2": fg('red')+"\b"+"@",
               "3": fg('red')+"\b"+"$",
               "4": fg('red')+"\b"+chr(922),
               "5": fg('red')+"\b"+"&"}
    print(UNDERLINE + "\nII. Choose your avatar\n" + RESET)
    print(BLUE + "Pick one of the following:")
    for key in sorted(avatars):
        print("\n" + key + ")   " + RED + avatars[key] + attr('reset') + BLUE)
    while True:
        avatar = input("\nSelect number: ")
        if avatar in ["1", "2", "3", "4", "5"]:
            system("clear")
            break
    hero_customization.append(avatars[avatar])

    skills = {"Spotter": "Increased sight radius (by 50%)",
              "Sniper": "Increased shooting distance (by +1 tile)",
              "Survivor": "Increased vitality (+1 starting life)",
              "Swimmer": "Decreased energy loss in water (by 50%)",
              "Veteran": "Incresed exp from killing enemies (by 25%)",
              "Athlete": "Increased energy regeneration (by 25%)",
              "Camper": "Increased maximum carry (by 10 kg)",
              "Smartass": "Easier time with riddles (+3 attempts)",
              "Thief": "Starts a game with a universal key (keys +1)"}
    print(UNDERLINE + "\nIII. Choose your preferenced abilities\n" + RESET)
    print(BLUE + "Pick three out of the following:")
    for key in skills:
        print("\n" + RED + key + " - " + BLUE + skills[key])
    while True:
        skill = input("\nSelect a skill (e.g. 'ninja'): ").title()
        if skill in skills:
            hero_customization.append(skill)
            print(RED + "Rambo is now a", skill + "!" + BLUE)
            del skills[skill.title()]
        else:
            print("\nNot a valid skill (or already taken)")
        if len(skills) == 6:
            break

    input("\nYou are ready. Press enter for a mission briefing")
    return(hero_customization)


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
    print(BLUE + "\n\n\nHere you can find a list of brave heroes who completed the game:\n")
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
    print("R - use medpack")
    print(UNDERLINE + "\nOther:" + RESET)
    print(BLUE + "Q - quits the game")
    print("I - shows extended inventory")
    print("H - show detailed in-game help")
    print("E - interact with doors and other objects\n")
    input("Press enter to go back to menu ")


def show_detailed_help():
    '''
    Displays detailed information about items, enemies, etc.
    '''
    system("clear")
    print(BLUE + "A detailed panel about all the things you encouter in game\n")
    print(UNDERLINE + "\nEnergy:" + RESET)
    print(BLUE + "Energy regenerates with every move. You lose it while swimming,\nshooting and being hit by enemies")
    print(UNDERLINE + "\nWeapons & Ammo:" + RESET)
    print(BLUE + "New weapons come from chests. Weapon vary in weight\nand shooting range. You use ammo on every shot")
    print(UNDERLINE + "\nEnemies:" + RESET)
    print(BLUE + "They can shoot you if you come to close. Vietnams have\nrange 0-1, Soviets 2-3. They provide exp")
    print(UNDERLINE + "\nMedpacks:" + RESET)
    print(BLUE + "Returns your hero to 100 energy. Drops from chests")
    print(UNDERLINE + "\nChests" + RESET)
    print(BLUE + "Random chance to drop weapons, ammo, medpacks or absolutely nothing")
    print(UNDERLINE + "\nKeys" + RESET)
    print(BLUE + "You need them open some doors")
    print(UNDERLINE + "\nInteligence" + RESET)
    print(BLUE + "Final boss is a riddler. The more inteligent you are\nthe better chances you have")
    print(UNDERLINE + "\nWater" + RESET)
    print(BLUE + "You can swim through, but you lose energy!")
    print(UNDERLINE + "\nBackpack" + RESET)
    print(BLUE + "If you go over the weight limit, your hero will suffer")
    print(UNDERLINE + "\nSight" + RESET)
    print(BLUE + "You can only see as far as your sight range")
    print(UNDERLINE + "\nExperience & Levels" + RESET)
    print(BLUE + "You get a level each 20exp points. Max level is 10.\nAffects your inteligence and other atributes\n")
    print("Press 'h' to return to game ")
    return


def show_detailed_log(full_log):
    '''
    Displays list of all messages so far.
    '''
    system("clear")
    print(full_log[0], "\n")
    for index in range(1, len(full_log)):
        if full_log[index] and (full_log[index] != full_log[index-1]):
            print(full_log[index])
    print("\nPress 'l' to return to game ")
    return


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


def show_death_screen():
    '''
    Shows a death screen, replays main program
    '''
    system("clear")
    print(RED + ascii_arts(4) + BLUE)
    input()
    exit()


def show_victory_screen(status):
    '''
    Shows a victory screen and updates highscores
    '''
    system("clear")
    print(YELLOW + ascii_arts(6) + RESET)
    print(BLUE + "You are victorious. Rambo once again saved the world.")
    print("There is only one more thing before you can get ready for sequel.")
    input("\nPress enter for Hall of Fame. You certainly deserved it!")
    system("clear")
    player_name = input("Your name? ")
    with open("highscores.txt", "a") as file:
        file.write(player_name + ",")
        file.write(str(int(status["Hero Level"])) + ",")
        file.write(str(round(status["End Time"] - status["Start Time"], 1)) + ",")
        file.write(str(round(min(status["Experience"]+status["Inteligence"], 150)/150)*100) + "%,")
        file.write(str(status["Experience"]//status["Experience Ratio"]) + "\n")
    input()
    show_highscores()
    exit()
