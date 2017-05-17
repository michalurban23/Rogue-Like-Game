import sys
import random
import rambo_colors


def create_objects(board, amount_of_objects, OBSTACLES):
    positions_of_objects = []
    while amount_of_objects:
        x = random.randint(2, len(board[0])-1)
        y = random.randint(2, len(board)-1)
        if board[y-1][x-1] not in OBSTACLES: # +rambo.ITEM_OBSTACLES:
            positions_of_objects.append((x, y))
            amount_of_objects -= 1
    return positions_of_objects



def insert_objects(board, positions, type_of_object):
    colored_output = ""
    if type_of_object == "E":
        colored_output = "\bE"
    elif type_of_object == "C":
        colored_output = "\bC"
    elif type_of_object == "K":
        colored_output = "\bK"
    for x, y in positions:
        board[y-1][x-1] = colored_output
    return board



def move_enemies(board, positions, OBSTACLES):
    new_positions = []
    for x, y in positions:
        direction = random.randint(1, 4)
#        print(x, y)
        if direction == 1 and board[y-2][x-1] not in OBSTACLES:
            new_positions.append((x, y-1))
        elif direction == 2 and board[y][x-1] not in OBSTACLES:
            new_positions.append((x, y+1))
        elif direction == 3 and board[y-1][x-2] not in OBSTACLES:
            new_positions.append((x-1, y))
        elif direction == 4 and board[y-1][x] not in OBSTACLES:
            new_positions.append((x+1, y))
        else:
            new_positions.append((x, y))
    return new_positions


def kill_enemies(enemy_positions, player_x, player_y, range_of_weapon):
    i = 0
    while i < len(enemy_positions):
        if abs(player_x-enemy_positions[i][0]) <= range_of_weapon and abs(player_y-enemy_positions[i][1]) <= range_of_weapon:
            # print(enemy_positions[i])
            del enemy_positions[i]
            break
        i += 1


def enemy_shooting(enemy_positons, player_x, player_y):
    pass


def pick_up_item(item_positions, player_x, player_y):
    i = 0
    while i < len(item_positions):
        if abs(player_x - item_positions[i][0]) <= 1 and abs(player_y-item_positions[i][1]) <= 1:
            del item_positions[i]
            break
        i += 1


def main():
    amount_of_enemies = 5
    background = rambo.create_board(sys.argv[1])
    positions_of_enemies = create_enemies(background, amount_of_enemies)
    move_enemies(background, positions_of_enemies)


if __name__ == "__main__":
    main()
