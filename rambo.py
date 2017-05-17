from rambo_screens import *
from rambo_hero_status import *
from rambo_hero_movement import *


OBSTACLES = [colors['black']+"\bX"+colors['reset'],  # Edges
             colors['dorange']+"\bW"+colors['reset'],  # Walls
             colors['green']+"\bT"+colors['reset']]  # Trees

STARTING_MAP = "vietnam_jungle.txt"
WEAPONS = {"Beretta": (1, 11)}
STARTING_STATUS = {"Lifes": 3,
                   "Energy": 100,
                   "Experience": 56,
                   "Ammo": 20,
                   "Weapon": "Beretta",
                   "Hero Level": 5,
                   "Keys": 0}

WEAPONS_ATTRIBUTES = {
    "Beretta" : (1, 10),
    "Uzi" : (2, 20),
    "M4" : (3, 30),
    "M16" : (4, 40)
}


def create_board(file_name):
    playboard = []
    with open(file_name, "r") as board:
        playboard_temp = board.readlines()
    for line in playboard_temp:
        playboard_line = []
        for element in line[:-1]:
            if element == "T":
                element = colors['green'] + "\b" + element + colors['reset']
            elif element == "X":
                element = colors['black'] + "\b" + element + colors['reset']
            elif element == "R":
                element = colors['blue'] + "\b" + element + colors['reset']
            elif element == "B" or element == "W":
                element = colors['dorange'] + "\b" + element + colors['reset']
            elif element == ".":
                element = colors['reset'] + "\b" + element + colors['reset']
            else:
                element = colors['yellow4b'] + "\b" + element + colors['reset']
            playboard_line.append(element)
        playboard.append(playboard_line)
    return playboard


def print_board(board):
    system("clear")
    for line in board:
        print(*line)


def insert_player(board, x, y, hero_skin, hero_face):
    board[y-1][x-1] = bg(hero_skin) + fg('red') + hero_face
    return board


def main():
    current_map = STARTING_MAP
    x = 2
    y = 2
    extend_inv = False
    amount_of_enemies = 50
    amount_of_chests = 10
    amount_of_keys = 3
    hero_status = STARTING_STATUS
    weapon_range = WEAPONS_ATTRIBUTES[hero_status["Weapon"]][0]
    # show_ascii_intro()
    # input()
    # show_main_menu()
    # hero_customization = create_character()
    hero_customization = ['white', "\b"+chr(920)]
    # start_game()
    background = create_board(current_map)
    positions_of_enemies = create_objects(background, amount_of_enemies, OBSTACLES)
    positions_of_chests = create_objects(background, amount_of_chests, OBSTACLES)
    positions_of_keys = create_objects(background, amount_of_keys, OBSTACLES)
    while True:
        background = create_board(current_map)
        board = insert_objects(background[:], positions_of_enemies, "E")
        board = insert_objects(background[:], positions_of_chests, "C")
        board = insert_objects(background[:], positions_of_keys, "K")
        board = insert_player(background[:], x, y, hero_customization[0], hero_customization[1])
        print_board(board)
        if extend_inv:
            print_status_bar_extended(hero_status, WEAPONS)
        else:
            print_status_bar_basic(hero_status)
        
        x, y, positions_of_enemies, extend_inv = move_hero(board, x, y, OBSTACLES, background,
                                                           positions_of_enemies, positions_of_chests,
                                                           extend_inv, weapon_range)


if __name__ == '__main__':
    main()
