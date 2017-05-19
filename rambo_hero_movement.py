from sys import stdin
from time import sleep
from rambo_minions import *
from rambo_screens import show_detailed_help, show_detailed_log

DOORS = [colors['black'] + "\b1" + colors['reset'], colors['black'] + "\b2" + colors['reset'],
         colors['black'] + "\b3" + colors['reset'], colors['black'] + "\b4" + colors['reset']]


def getch():
    import tty
    import termios
    fd = stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(stdin.fileno())
        ch = stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def move_hero(board, x, y, OBSTACLES, background, positions_of_enemies, item_positions,
              inv, WEAPONS_ATTRIBUTES, hero_status, current_map, enemy_type):
    pressed_key = getch()
    if pressed_key == "w" and board[y-2][x-1] not in OBSTACLES and not hero_status["Overweight"]:
        if board[y-2][x-1] in DOORS:
            y -= check_doors_status(hero_status, board[y-2][x-1], DOORS)
        else:
            if board[y-2][x-1] == colors['blue'] + "\bR" + colors['reset']:
                manage_events(status=hero_status, event="swimming")
            y -= 1

    elif pressed_key == "s" and board[y][x-1] not in OBSTACLES and not hero_status["Overweight"]:
        if board[y][x-1] in DOORS:
            y += check_doors_status(hero_status, board[y][x-1], DOORS)
        else:
            if board[y][x-1] == colors['blue'] + "\bR" + colors['reset']:
                manage_events(status=hero_status, event="swimming")
            y += 1

    elif pressed_key == "a" and board[y-1][x-2] not in OBSTACLES and not hero_status["Overweight"]:
        if board[y-1][x-2] in DOORS:
            x -= check_doors_status(hero_status, board[y-1][x-2], DOORS)
        else:
            if board[y-1][x-2] == colors['blue'] + "\bR" + colors['reset']:
                manage_events(status=hero_status, event="swimming")
            x -= 1

    elif pressed_key == "d" and board[y-1][x] not in OBSTACLES and not hero_status["Overweight"]:
        if board[y-1][x] in DOORS:
            x += check_doors_status(hero_status, board[y-1][x], DOORS)
        else:
            if board[y-1][x] == colors['blue'] + "\bR" + colors['reset']:
                manage_events(status=hero_status, event="swimming")
            x += 1

    elif pressed_key == "q":
        if input("Type 'quit' to exit ") == "quit":
            exit()

    elif pressed_key == " ":
        if hero_status["Ammo"] > 0:
            kill_enemies(positions_of_enemies, x, y, WEAPONS_ATTRIBUTES[hero_status["Weapon"]][0], hero_status)
        else:
            manage_events(hero_status, event="no_ammo")

    elif pressed_key == "i":
        inv = not inv

    elif pressed_key == "r":
        if hero_status["Medpacks"] > 0:
            manage_events(hero_status, event="medpack_used")

    elif pressed_key == "h":
        while True:
            show_detailed_help()
            sleep(0.1)
            if getch() == "h":
                break

    elif pressed_key == "l":
        while True:
            show_detailed_log(full_log)
            sleep(0.1)
            if getch() == "l":
                break

    elif pressed_key == "e":
        pick_up_item(item_positions, x, y, hero_status)
        if board[y-1][x] == colors['sblue'] + "\bN" + colors['reset']:
            if (current_map == "vietnam_jungle.txt" and hero_status["Keys"] > 1) or \
               (current_map == "pow_camp.txt" and hero_status["Keys"] > 3):
                    current_map = change_map(current_map)
            else:
                manage_events(hero_status, event="no_keys")

    manage_events(hero_status, event="check_load", WEAPONS=WEAPONS_ATTRIBUTES)

    if pressed_key in ["w", "s", "a", "d"]:
        enemy_shooting(positions_of_enemies, x, y, hero_status, enemy_type)
        positions_of_enemies = move_enemies(background[:], positions_of_enemies, OBSTACLES)
        manage_events(hero_status, event="check_load", WEAPONS=WEAPONS_ATTRIBUTES)
        if not hero_status["Overweight"]:
            manage_events(hero_status, event="hero_moved")
    return x, y, positions_of_enemies, inv, current_map
