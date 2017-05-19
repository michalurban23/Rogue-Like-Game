from rambo_colors import *
from random import randint
from rambo_screens import show_death_screen
import time

BORDER = colors['black'] + "-" + colors['reset']
message = None
full_log = ["Log of all messages from the game engine"]


def change_initial_stats(status, changes):
    if "Spotter" in changes:
        status["Sight"] += 5
    if "Sniper" in changes:
        status["Bonus Range"] += 1
    if "Survivor" in changes:
        status["Lifes"] += 1
    if "Swimmer" in changes:
        status["Swimming"] = 0.5
    if "Veteran" in changes:
        status["Experience Ratio"] = 1.25
    if "Athlete" in changes:
        status["Energy Regen"] *= 1.25
    if "Camper" in changes:
        status["Max Load"] += 10
    if "Smartass" in changes:
        status["Inteligence"] += 3
    if "Thief" in changes:
        status["Keys"] += 1
    return status


def print_status_bar(message=None):
    if message == "hero_touched":
        print(BORDER + RED + "{:^142}".format("You have been shot by an enemy. Your energy fell") + BLUE + BORDER)
    elif message == "overweight":
        print(BORDER + RED + "{:^142}".format("Your backpack is too heavy. Lose some weight!") + BLUE + BORDER)
    elif message == "enemy_killed":
        print(BORDER + GREEN + "{:^142}".format("Enemy killed. You gain exp!") + BLUE + BORDER)
    elif message == "key_found":
        print(BORDER + GREEN + "{:^142}".format("You found a key. Added to your inventory") + BLUE + BORDER)
    elif message == "chest_opened_ammo":
        print(BORDER + GREEN + "{:^142}".format("You found a chest! You got ammo!") + BLUE + BORDER)
    elif message == "chest_opened_weapon":
        print(BORDER + GREEN + "{:^142}".format("You found a chest! Weapon inside!") + BLUE + BORDER)
    elif message == "chest_opened_medpack":
        print(BORDER + GREEN + "{:^142}".format("You found a chest! Additiona medpack!") + BLUE + BORDER)
    elif message == "chest_opened_nothing":
        print(BORDER + GREEN + "{:^142}".format("You found a chest! It was empty...") + BLUE + BORDER)
    elif message == "life_lost":
        print(BORDER + RED + "{:^142}".format("You lost life!") + BLUE + BORDER)
    elif message == "no_keys":
        print(BORDER + RED + "{:^142}".format("Not enough keys. Go find some!") + BLUE + BORDER)
    elif message == "medpack_used":
        print(BORDER + GREEN + "{:^142}".format("Medpack used. Energy back to full!") + BLUE + BORDER)
    elif message == "no_ammo":
        print(BORDER + RED + "{:^142}".format("You have no ammo left!") + BLUE + BORDER)
    else:
        print(BORDER + BLUE + "{:^142}".format("= = = = =") + BORDER)
    print(BORDER*144 + colors['reset'])
    full_log.append(message)


def print_inventory_basic(status):
    print(BORDER * 13 +
          BORDER*3, BLUE + "Lifes:" + RED + "{:>10}".format(status["Lifes"]),
          BORDER*3, BLUE + "Hero Level:" + RED + " {:>10}".format(status["Hero Level"]),
          BORDER*3, BLUE + "Weapon:" + RED + " {:>10}".format(status["Weapon"]),
          BORDER*3, BLUE + "Ammo:" + RED + " {:>10}".format(status["Ammo"]),
          BORDER*3, BLUE + "Energy:" + RED + " {:>10}".format(round(status["Energy"], 2)),
          BORDER * 16)
    print(BORDER*144 + colors['reset'])
    print(BORDER * 22 +
          BORDER*3, BLUE + "Shoot:" + RED + "{:>9}".format("SpaceBar"),
          BORDER*3, BLUE + "Use Medpack:" + RED + "{:>3}".format("R"),
          BORDER*3, BLUE + "Pick / Use:" + RED + "{:>3}".format("E"),
          BORDER*3, BLUE + "Help:" + RED + "{:>3}".format("H"),
          BORDER*3, BLUE + "Log:" + RED + "{:>3}".format("L"),
          BORDER*3, BLUE + "Quit:" + RED + "{:>3}".format("Q"),
          BORDER * 25)
    print(BORDER*144 + colors['reset'])


def print_inventory_extended(status, WEAPONS):
    current_load = (0.5*status["Keys"] + status["Medpacks"] + WEAPONS[status["Weapon"]][1] + 0.05*status["Ammo"])
    ext_inv = ["11" + YELLOW + "<< Hero Progress >>" +
               BLUE + "    Current hero level: " + RED + str(status["Hero Level"]) +
               BLUE + "    Current exp: " + RED + str(status["Experience"]) +
               BLUE + "    You are " + RED + str(20 - status["Experience"] % 20) + BLUE + " exp away from next level" +
               BLUE + "    Play time is " + RED + str(round(status["End Time"] - status["Start Time"], 1)) + BLUE + "s",
               "00 ",
               "09" + YELLOW + "<< Weapon Parameters >>" +
               BLUE + "    Type: " + RED + status["Weapon"] +
               BLUE + "    Weight: " + RED + str(WEAPONS[status["Weapon"]][1]) +
               BLUE + "    Shooting Range: " + RED + str(WEAPONS[status["Weapon"]][0]+status["Bonus Range"]) +
               BLUE + "    Ammo (0.05 kg each): " + RED + str([status["Ammo"]][0]),
               "00 ",
               "13" + YELLOW + "<< Hero Status >>" +
               BLUE + "    Lifes: " + RED + str(status["Lifes"]) +
               BLUE + "    Max Energy: " + RED + str(round(status["Max Energy"], 1)) +
               BLUE + "    Energy Regen: " + RED + str(status["Energy Regen"]) + BLUE + "/s" +
               BLUE + "    Inteligence: " + RED + str(status["Inteligence"]) +
               BLUE + "    Sight Range: " + RED + str(status["Sight"]) + BLUE + " tiles",
               "00 ",
               "11" + YELLOW + "<< Backpack Status >>" +
               BLUE + "    Medpacks (1 kg each): " + RED + str(status["Medpacks"]) +
               BLUE + "    Keys (0.5 kg each): " + RED + str(status["Keys"]) +
               BLUE + "    Load limit: " + RED + str(status["Max Load"]) + BLUE + " kg" +
               BLUE + "    Current load: " + RED + str(round(current_load/status["Max Load"]*100, 1)) + BLUE + "%"]
    # This made a lot of sense when I first wrote it, so bear with me. If there were no coloring of output,
    # we could simply format it within the lenght of bar (being 144 chars). But every command to change color will
    # also extend lenght of a string by 7 chars, despite those 7 chars not showing on screen. So I have to extend
    # formating area by 7 times the amount of coloring commands in each element. To do that, I add to the begining of
    # each element a number of how many colors commands are in it and then use it to calculate total width
    for element in ext_inv:
        print(BORDER + "{:^{width}}".format(element[2:], width=142+int(element[:2])*7) + BORDER)
    print(BORDER*144 + colors['reset'])


def manage_events(status, event=None, WEAPONS=None):
    global message
    if event == "no_ammo":
        message = "no_ammo"
    if event == "no_keys":
        message = "no_keys"
    if event == "enemy_killed":
        message = "enemy_killed"
        status["Experience"] += 1*status["Experience Ratio"]
    if event == "shot_fired":
        status["Ammo"] -= 1
    if event == "medpack_used":
        status["Medpacks"] -= 1
        status["Energy"] = status["Max Energy"]
        message = "medpack_used"
    if event == "key_picked":
        status["Keys"] += 1
        message = "key_found"
    if event == "swimming":
        status["Energy"] -= randint(15, 30)*status["Swimming"]
        message = "losing_energy"
        if status["Energy"] <= 0:
            manage_events(status, event="life_lost")
    if event == "life_lost":
        status["Lifes"] -= 1
        message = "life_lost"
    if event == "hero_moved":
        status["Energy"] += status["Energy Regen"]
        message = None
    if event == "enemy_shot":
        status["Energy"] -= randint(35, 55)
        if status["Energy"] <= 0:
            manage_events(status, event="life_lost")
        message = "hero_touched"
    if event == "chest_opened":
        random_item = randint(0, 4)
        if random_item == 0:
            status["Ammo"] += randint(5, 10)
            message = "chest_opened_ammo"
        elif random_item == 1:
            status["Medpacks"] += 1
            message = "chest_opened_medpack"
        elif random_item == 2:
            random_weapon = randint(0, 10)
            message = "chest_opened_weapon"
            if random_weapon == 10:
                status["Weapon"] = "M16"
                status["Ammo"] = max(status["Ammo"], 50)
            elif random_weapon in [7, 8, 9] and status["Weapon"] != "M16":
                status["Weapon"] = "M4"
                status["Ammo"] = max(status["Ammo"], 50)
            elif random_weapon in [3, 4, 5, 6] and status["Weapon"] not in ["M4", "M16"]:
                status["Weapon"] = "Uzi"
                status["Ammo"] = max(status["Ammo"], 50)
            else:
                status["Ammo"] += 10
        elif random_item == 3:
            message = "chest_opened_nothing"
    if event == "check_load":
        if 0.05*status["Ammo"]+0.5*status["Keys"]+status["Medpacks"]+WEAPONS[status["Weapon"]][1] > status["Max Load"]:
            status["Overweight"] = True
            message = "Overweight"
        else:
            status["Overweight"] = False
    else:
        status = change_hero_status(status)
    return status, message


def change_hero_status(status):
    old_level = status["Hero Level"]
    if status["Experience"] % 20 == 0:
        status["Hero Level"] = 1 + status["Experience"] // 20
    if old_level != status["Hero Level"]:
        status["Sight"] += 1
        status["Max Energy"] *= 1.1
        status["Max Load"] += 1
        if old_level % 2 == 1:
            status["Inteligence"] += 1
    if status["Energy"] <= 0:
        status["Energy"] = status["Max Energy"]
    if status["Energy"] > status["Max Energy"]:
        status["Energy"] = status["Max Energy"]
    if status["Lifes"] == 0:
        show_death_screen()
    status["End Time"] = time.time()
    return status


def check_doors_status(status, element, doors):
    for n in range(0, 4):
        if element == doors[n] and status["Keys"] > n:
            return 1
    manage_events(status, event="no_keys")
    return 0


def change_map(current_map):
    if current_map == "vietnam_jungle.txt":
        next_map = "pow_camp.txt"
    elif current_map == "pow_camp.txt":
        next_map = "soviet_camp.txt"
    elif current_map == "soviet_camp.txt":
        next_map = "final_boss.txt"
    return next_map
