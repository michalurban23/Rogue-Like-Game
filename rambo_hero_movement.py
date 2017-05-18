from sys import stdin
from rambo_minions import *


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
              inv, weapon_range, hero_status, current_map):
    pressed_key = getch()
    es = False
    if pressed_key == "w" and board[y-2][x-1] not in OBSTACLES:
        if board[y-2][x-1] == colors['blue'] + "\bR" + colors['reset']:
            manage_events(status=hero_status, event="swimming")
        y -= 1

    elif pressed_key == "s" and board[y][x-1] not in OBSTACLES:
        if board[y][x-1] == colors['blue'] + "\bR" + colors['reset']:
            manage_events(status=hero_status, event="swimming")
        y += 1

    elif pressed_key == "a" and board[y-1][x-2] not in OBSTACLES:
        if board[y-1][x-2] == colors['blue'] + "\bR" + colors['reset']:
            manage_events(status=hero_status, event="swimming")
        x -= 1

    elif pressed_key == "d" and board[y-1][x] not in OBSTACLES:
        if board[y-1][x] == colors['blue'] + "\bR" + colors['reset']:
            manage_events(status=hero_status, event="swimming")
        x += 1

    elif pressed_key == "q":
        if input("Type 'quit' to exit ") == "quit":
            exit()

    elif pressed_key == " ":
        kill_enemies(positions_of_enemies, x, y, weapon_range, hero_status)

    elif pressed_key == "i":
        inv = not inv

    elif pressed_key == "r":
        if hero_status["Medpacks"] > 0:
            manage_events(hero_status, event="medpack_used")

    elif pressed_key == "e":
        pick_up_item(item_positions, x, y, hero_status)
        if board[y-1][x] == colors['sblue'] + "\bN" + colors['reset']:
            current_map = change_map(current_map)

    if pressed_key in ["w", "s", "a", "d"]:
        enemy_shooting(positions_of_enemies, x, y, hero_status)
        manage_events(hero_status, event="hero_moved")
        positions_of_enemies = move_enemies(background[:], positions_of_enemies, OBSTACLES)

    return x, y, positions_of_enemies, inv, current_map
