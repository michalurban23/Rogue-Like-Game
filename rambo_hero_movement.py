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
    if pressed_key == "w" and board[y-2][x-1] not in OBSTACLES:
        y -= 1
    elif pressed_key == "s" and board[y][x-1] not in OBSTACLES:
        y += 1
    elif pressed_key == "a" and board[y-1][x-2] not in OBSTACLES:
        x -= 1
    elif pressed_key == "d" and board[y-1][x] not in OBSTACLES:
        x += 1
    elif pressed_key == "q":
        if input("Type 'quit' to exit ") == "quit":
            exit()
    elif pressed_key == " ":
        kill_enemies(positions_of_enemies, x, y, weapon_range, hero_status)
    elif pressed_key == "i":
        inv = not inv
    elif pressed_key == "e":
        pick_up_item(item_positions, x, y, hero_status)
    if pressed_key in ["w", "s", "a", "d"]:
        manage_events(hero_status)
        positions_of_enemies = move_enemies(background[:], positions_of_enemies, OBSTACLES)
    if pressed_key == "e" and board[y-1][x] == colors['sblue'] + "\bN" + colors['reset']:
        current_map = change_map(current_map)
    return x, y, positions_of_enemies, inv, current_map
