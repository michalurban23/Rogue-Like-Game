from rambo_screens import *
from rambo_hero_status import *
from rambo_hero_movement import *
import hot_cold

OBSTACLES = [colors['black']+"\bX"+colors['reset'],  # Edges
             colors['dorange']+"\bW"+colors['reset'],  # Walls
             colors['green']+"\bT"+colors['reset'],  # Trees
             colors['sblue']+"\bN"+colors['reset']]  # Portals
STARTING_MAP = "vietnam_jungle.txt"
STARTING_STATUS = {"Lifes": 2,
                   "Max Energy": 100,
                   "Energy": 100,
                   "Experience": 0,
                   "Ammo": 20,
                   "Weapon": "Beretta",
                   "Medpacks": 1,
                   "Hero Level": 1,
                   "Keys": 0,
                   "Sight": 10,
                   "Max Load": 15,
                   "Energy Regen": 0.2,
                   "Inteligence": 2,
                   "Bonus Range": 0,
                   "Start Time": time.time(),
                   "Overweight": False,
                   "Swimming": 1,
                   "Experience Ratio": 1}
WEAPONS_ATTRIBUTES = {"Beretta": (2, 3),
                      "Uzi": (3, 6),
                      "M4": (4, 9),
                      "M16": (5, 12)}
MAP_SPECIFIC = {"vietnam_jungle.txt": {"Enemy_number": 50, "Enemy_type": "V", "Keys": 2, "Chests": 15},
                "pow_camp.txt": {"Enemy_number": 40, "Enemy_type": "S", "Keys": 2, "Chests": 15},
                "soviet_camp.txt": {"Enemy_number": 60, "Enemy_type": "S", "Keys": 1, "Chests": 15},
                "final_boss.txt": {"Enemy_number": 0, "Enemy_type": "S", "Keys": 0, "Chests": 0}}


def create_board(file_name):
    '''Imports background from "file_name" and colored it.
    Returns colored background.
    '''
    playboard = []
    with open(file_name, "r") as board:
        playboard_temp = board.readlines()
    for line in playboard_temp:
        playboard_line = []
        for element in line[:-1]:
            if element == "T":
                element = colors['green'] + "\b" + element + colors['reset']
            elif element == "X" or element in ["1", "2", "3", "4"]:
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
            else:
                element = colors['yellow4b'] + "\b" + element + colors['reset']
            playboard_line.append(element)
        playboard.append(playboard_line)
    return playboard


def print_board(hero_status, board, x, y, current_map):
    '''
    Takes in board, player position, his status and current map. Based on player sight range,
    displays board around him, while everything rest is printed black. On the last map its turned off
    '''
    outside = colors['black'] + "X" + colors['reset']  # Black elements of vision outside range
    # Calculate boundaries of player vision, so he sees no further than his sight range or map borders
    boundaries = {"left": max(0, x - hero_status["Sight"] - 3),
                  "right": min(144, x + hero_status["Sight"] + 3),
                  "top": max(1, y - hero_status["Sight"] + 3),
                  "bottom": min(39, y + hero_status["Sight"] - 3)}
    system("clear")
    if current_map == "final_boss.txt":
        for line in board:
            print(*line)
    else:
        # prints black blocks everywhere outside boundaries, and actual board inside
        for i in range(boundaries["top"]):
            print(outside * 144)
        for line in board[boundaries["top"]:boundaries["bottom"]]:
            print(outside * boundaries["left"],
                  *line[boundaries["left"]:boundaries["right"]],
                  "\b" + outside * (144-boundaries["right"]))
        for i in range(40 - boundaries["bottom"]):
            print(outside * 144)


def insert_player(board, x, y, hero_skin, hero_face):
    '''Inserts player sign on "board" on proper position given by "x" and "y".
    "hero_skin" changes color of background of player sign
    "hero_face" changes the sign of player
    '''
    board[y-1][x-1] = bg(hero_skin) + fg('red') + hero_face
    return board


def main():
    current_map = STARTING_MAP
    show_ascii_intro()
    input()
    show_main_menu()
    hero_customization = create_character()
    hero_status = change_initial_stats(STARTING_STATUS, hero_customization[2:])
    start_game()
    while True:
        next_map = current_map
        # Hero starting position (top left)
        x = 2
        y = 2
        extend_inv = False
        enemy_type = MAP_SPECIFIC[current_map]['Enemy_type']
        amount_of_enemies = MAP_SPECIFIC[current_map]['Enemy_number']
        amount_of_chests = MAP_SPECIFIC[current_map]['Chests']
        amount_of_keys = MAP_SPECIFIC[current_map]['Keys']
        background = create_board(current_map)
        positions_of_enemies = create_objects(background, amount_of_enemies, OBSTACLES)
        positions_of_chests = create_objects(background, amount_of_chests, OBSTACLES)
        positions_of_keys = create_objects(background, amount_of_keys, OBSTACLES)
        items_position = [positions_of_chests, positions_of_keys]
        while next_map == current_map:
            background = create_board(current_map)
            board = insert_objects(background[:], positions_of_enemies, MAP_SPECIFIC[current_map]['Enemy_type'])
            board = insert_objects(background[:], positions_of_chests, "C")
            board = insert_objects(background[:], positions_of_keys, "K")
            board = insert_player(background[:], x, y, hero_customization[0], hero_customization[1])
            # print_board(board)
            print_board(hero_status, board, x, y, current_map)
            hero_status, message = manage_events(status=hero_status)
            if current_map == "final_boss.txt":
                hot_cold.main(hero_status)
            else:
                print_status_bar(message)
                if extend_inv:
                    print_inventory_extended(hero_status, WEAPONS_ATTRIBUTES)
                else:
                    print_inventory_basic(hero_status)
                x, y, positions_of_enemies, extend_inv, current_map = move_hero(
                                        board, x, y, OBSTACLES, background, positions_of_enemies, items_position,
                                        extend_inv, WEAPONS_ATTRIBUTES, hero_status, current_map, enemy_type
                                        )


if __name__ == '__main__':
    main()
