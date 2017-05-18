from rambo_colors import *
from random import randint
from rambo_screens import show_death_screen

BORDER = colors['black'] + "-" + colors['reset']
message = None


def print_status_bar(message=None):
    if message == "hero_touched":
        print(BORDER + RED + "{:^142}".format("You have been stabbed by an enemy. Your energy fell") + BLUE + BORDER)
    elif message == "enemy_killed":
        print(BORDER + GREEN + "{:^142}".format("Enemy killed. You gain exp!") + BLUE + BORDER)
    elif message == "key_found":
        print(BORDER + GREEN + "{:^142}".format("You found a key. Added to your inventory") + BLUE + BORDER)
    elif message == "chest_opened":
        print(BORDER + GREEN + "{:^142}".format("You found a chest!") + BLUE + BORDER)
    elif message == "life_lost":
        print(BORDER + RED + "{:^142}".format("You lost life!") + BLUE + BORDER)
    elif message == "medpack_used":
        print(BORDER + GREEN + "{:^142}".format("Medpack used. Energy back to full!") + BLUE + BORDER)
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
          BORDER*3, BLUE + "Energy:" + RED + " {:>10}".format(round(status["Energy"], 2)),
          BORDER * 16)
    print(BORDER*144 + colors['reset'])


def print_inventory_extended(status, WEAPONS):
    current_load = (0.5*status["Keys"] + status["Medpacks"] + WEAPONS[status["Weapon"]][1] + 0.1*status["Ammo"])
    ext_inv = ["08" + YELLOW + "<< Hero Progress >>" +
               BLUE + "    Current hero level: " + RED + str(status["Hero Level"]) +
               BLUE + "    Current exp: " + RED + str(status["Experience"]) +
               BLUE + "    You are " + RED + str(20 - status["Experience"] % 20) + BLUE + " exp away from next level",
               "00 ",
               "07" + YELLOW + "<< Weapon Parameters >>" +
               BLUE + "    Type: " + RED + status["Weapon"] +
               BLUE + "    Weight: " + RED + str(WEAPONS[status["Weapon"]][1]) +
               BLUE + "    Shooting Range: " + RED + str(WEAPONS[status["Weapon"]][0]),
               "00 ",
               "11" + YELLOW + "<< Hero Status >>" +
               BLUE + "    Lifes: " + RED + str(status["Lifes"]) +
               BLUE + "    Energy: " + RED + str(round(status["Energy"], 1)) +
               BLUE + "    Energy Regen: " + RED + str(status["Energy Regen"]) + BLUE + "/s" +
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


def manage_events(status, event=None):
    global message
    if event == "enemy_killed":
        message = "enemy_killed"
        status["Experience"] += 1
    if event == "shot_fired":
        status["Ammo"] -= 1
    if event == "medpack_used":
        status["Medpacks"] -= 1
        status["Energy"] = 100
        message = "medpack_used"
    if event == "chest_opened":
        message = "chest_opened"
        random_item = randint(0, 4)
        if random_item == 0:
            amount_of_ammo = randint(1, 5)
            status["Ammo"] += amount_of_ammo
        elif random_item == 1:
            status["Medpacks"] += 1
        elif random_item == 2:
            random_weapon = randint(0, 10)
            if random_weapon == 10:
                status["Weapon"] = "M16"
            elif random_weapon in [8, 9]:
                status["Weapon"] = "M4"
            elif random_weapon in [5, 6, 7]:
                status["Weapon"] = "Uzi"
        elif random_item == 3:
            pass
    if event == "swimming":
        status["Energy"] -= randint(15, 30)
        message = "losing_energy"
        if status["Energy"] <= 0:
            manage_events(status, event="life_lost")
    if event == "life_lost":
        status["Lifes"] -= 1
        message = "life_lost"
    if event == "hero_moved":
        status["Energy"] += status["Energy Regen"]
    else:
        status = change_hero_status(status)
    return status, message


def change_hero_status(status):
    if status["Experience"] % 20 == 0:
        status["Hero Level"] = 1 + status["Experience"] // 20
    if status["Energy"] <= 0:
        status["Energy"] = 100
    if status["Energy"] > 100:
        status["Energy"] = 100
    if status["Lifes"] == 0:
        show_death_screen()
    return status


def change_map(current_map):
    if current_map == "vietnam_jungle.txt":
        next_map = "pow_camp.txt"
    elif current_map == "pow_camp.txt":
        next_map = "soviet_camp.txt"
    elif current_map == "soviet_camp.txt":
        next_map = "final_boss.txt"
    return next_map
