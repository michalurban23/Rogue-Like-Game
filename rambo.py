from rambo_screens import *
from rambo_hero_status import *
from rambo_hero_movement import *


OBSTACLES = [colors['black']+"\bX"+colors['reset'],  # Edges
             colors['dorange']+"\bW"+colors['reset'],  # Walls
             colors['green']+"\bT"+colors['reset'],  # Trees
             colors['red']+"\b|"+colors['reset'],  # Boss
             colors['sblue']+"\bN"+colors['reset']]  # Portals
STARTING_MAP = "vietnam_jungle.txt"
STARTING_STATUS = {"Lifes": 2,
                   "Energy": 100,
                   "Experience": 0,
                   "Ammo": 20,
                   "Weapon": "Beretta",
                   "Hero Level": 1,
                   "Keys": 0,
                   "Sight": 10,
                   "Max Load": 15,
                   "Energy Regen": 0.2,
                   "Inteligence": 5}
WEAPONS_ATTRIBUTES = {"Beretta": (1, 3),
                      "Uzi": (2, 6),
                      "M4": (3, 10),
                      "M16": (4, 15)}
MAP_SPECIFIC = {"vietnam_jungle.txt": {"Enemy_number": 50, "Enemy_type": "V", "Keys": 3, "Chests": 13},
                "pow_camp.txt": {"Enemy_number": 5, "Enemy_type": "S", "Keys": 3, "Chests": 13},
                "soviet_camp.txt": {"Enemy_number": 15, "Enemy_type": "S", "Keys": 3, "Chests": 13},
                "final_boss.txt": {"Enemy_number": 0, "Enemy_type": "S", "Keys": 0, "Chests": 0}}


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
            elif element == "-":
                element = colors['gray'] + "\b" + element + colors['reset']
            elif element == "N":
                element = colors['sblue'] + "\b" + element + colors['reset']
            elif element == "S" or element == '|':
                element = colors['red'] + "\b" + element + colors['reset']
            # elif element == "*":
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
    hero_status = STARTING_STATUS
    weapon_range = WEAPONS_ATTRIBUTES[hero_status["Weapon"]][0]
    current_map = STARTING_MAP
    # show_ascii_intro()
    # input()
    # show_main_menu()
    # hero_customization = create_character()
    hero_customization = ['white', "\b"+chr(920), "Spotter", "Camper", "Survivor"]
    # start_game()
    while True:
        next_map = current_map
        #x = 110
        #y = 20
        x = 2
        y = 2
        extend_inv = False
        amount_of_enemies = MAP_SPECIFIC[current_map]['Enemy_number']
        amount_of_chests = MAP_SPECIFIC[current_map]['Chests']
        amount_of_keys = MAP_SPECIFIC[current_map]['Keys']
        background = create_board(current_map)
        positions_of_enemies = create_objects(background, amount_of_enemies, OBSTACLES)
        positions_of_chests = create_objects(background, amount_of_chests, OBSTACLES)
        positions_of_keys = create_objects(background, amount_of_keys, OBSTACLES)
        while next_map == current_map:
            background = create_board(current_map)
            board = insert_objects(background[:], positions_of_enemies, MAP_SPECIFIC[current_map]['Enemy_type'])
            board = insert_objects(background[:], positions_of_chests, "C")
            board = insert_objects(background[:], positions_of_keys, "K")
            board = insert_player(background[:], x, y, hero_customization[0], hero_customization[1])
            print_board(board)
            hero_status, message = manage_events(status=hero_status)
            print_status_bar(message)
            message = None
            if extend_inv:
                print_inventory_extended(hero_status, WEAPONS_ATTRIBUTES)
            else:
                print_inventory_basic(hero_status)
            x, y, positions_of_enemies, extend_inv, current_map = move_hero(board, x, y, OBSTACLES, background, positions_of_enemies,
                                                               positions_of_chests, extend_inv, weapon_range,
                                                               hero_status, current_map)

if __name__ == '__main__':
    main()
