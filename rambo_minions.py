import sys
import random


def create_enemies(board, amount_of_enemies, OBSTACLES):
    '''
    '''
    positions_of_enemies = []
    while amount_of_enemies:
        x = random.randint(2, len(board[0])-1)
        y = random.randint(2, len(board)-1)
        if board[y-1][x-1] not in OBSTACLES:
            positions_of_enemies.append((x, y))
            amount_of_enemies -= 1
    return positions_of_enemies


def insert_enemies(board, positions):
    for x, y in positions:
        board[y-1][x-1] = "\bE"
    return board


def move_enemies(board, positions, OBSTACLES):
    new_positions = []
    for x, y in positions:
        direction = random.randint(1,4)
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


def kill_enemies(enemy_positions, player_x, player_y):
    i = 0
    while i < len(enemy_positions):
        if abs(player_x-enemy_positions[i][0]) <= 5 and abs(player_y-enemy_positions[i][1]) <= 5 :
            # print(enemy_positions[i])
            del enemy_positions[i]
            break
        i += 1



def main():
    amount_of_enemies = 5
    background = rambo.create_board(sys.argv[1])
    positions_of_enemies = create_enemies(background, amount_of_enemies)
    move_enemies(background, positions_of_enemies)


if __name__ == "__main__":
    main()
