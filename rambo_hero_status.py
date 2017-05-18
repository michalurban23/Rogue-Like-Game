from rambo_colors import *

BORDER = colors['black'] + "-" + colors['reset']
message = None


def print_status_bar(message=None):
    if message == "hero_touched":
        print(RED + "You have been stabbed by an enemy. Your energy greatly fell" + BLUE)
    elif message == "enemy_killed":
        print(BORDER + GREEN + "{:^142}".format("Enemy killed. You gain exp!") + BLUE + BORDER)
    elif message == "key_found":
        print(GREEN + "You found a key. Added to your inventory" + BLUE)
    elif message == "energy_zero":
        print(RED + "Your energy dropped below zero. You lose a life" + BLUE)
    elif message == "chest_opened":
        print(BORDER + GREEN + "{:^142}".format("You found a chest!") + BLUE + BORDER)
    elif message == "":
        print("")
    else:
        print(BORDER + BLUE + "{:^142}".format("= = = = =") + BORDER)
    print(BORDER*144 + colors['reset'])


def print_inventory_basic(status):
    print(BORDER * 13 +
          BORDER*3, BLUE + "Lifes:" + RED + "{:>10}".format(status["Lifes"]),
          BORDER*3, BLUE + "Hero Level:" + RED + " {:>10}".format(status["Hero Level"]),
          BORDER*3, BLUE + "Weapon:" + RED + " {:>10}".format(status["Weapon"]),
          BORDER*3, BLUE + "Ammo:" + RED + " {:>10}".format(status["Ammo"]),
          BORDER*3, BLUE + "Energy:" + RED + " {:>10}".format(status["Energy"]),
          BORDER * 16)
    print(BORDER*144 + colors['reset'])


def print_inventory_extended(status, WEAPONS):
    current_load = (0.5*status["Keys"] + WEAPONS[status["Weapon"]][1] + 0.1*status["Ammo"])
    ext_inv = ["08" + YELLOW + "<< Hero Progress >>" +
               BLUE + "    Current hero level: " + RED + str(status["Hero Level"]) +
               BLUE + "    Current exp: " + RED + str(status["Experience"]) +
               BLUE + "    You are " + RED + str(10 - status["Experience"] % 10) + BLUE + " exp away from next level",
               "00 ",
               "07" + YELLOW + "<< Weapon Parameters >>" +
               BLUE + "    Type: " + RED + status["Weapon"] +
               BLUE + "    Weight: " + RED + str(WEAPONS[status["Weapon"]][1]) +
               BLUE + "    Shooting Range: " + RED + str(WEAPONS[status["Weapon"]][0]),
               "00 ",
               "11" + YELLOW + "<< Hero Status >>" +
               BLUE + "    Lifes: " + RED + str(status["Lifes"]) +
               BLUE + "    Energy: " + RED + str(status["Energy"]) +
               BLUE + "    Energy Regen: " + RED + str(status["Energy Regen"]) + BLUE + "/s" +
               BLUE + "    Sight Range: " + RED + str(status["Sight"]) + BLUE + " tiles",
               "00 ",
               "09" + YELLOW + "<< Backpack Status >>" +
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


def manage_events(status, event=None):
    global message
    if event == "enemy_killed":
        message = "enemy_killed"
        status["Experience"] += 1
    if event == "shot_fired":
        status["Ammo"] -= 1
    if event == "chest_opened":
        message = "chest_opened"
    status = change_hero_status(status)
    return status, message


def change_hero_status(status):
    if status["Experience"] % 10 == 0:
        status["Hero Level"] = 1 + status["Experience"] // 10
    return status
