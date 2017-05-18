import sys
import random
import rambo_colors
from rambo_hero_status import *

ADDITIONAL_OBSTACLES = [colors['violet'] + "\bK" + colors['reset'],  # Keys
                        colors['violet'] + "\bC" + colors['reset'],  # Chests
                        colors['red'] + "\bS" + colors['reset'],  # Soviets
                        colors['yellow'] + "\bV" + colors['reset']]  # Vietnamees


def create_objects(board, amount_of_objects, OBSTACLES):
    positions_of_objects = []
    while amount_of_objects:
        x = random.randint(2, len(board[0])-1)
        y = random.randint(2, len(board)-1)
        if board[y-1][x-1] not in OBSTACLES + ADDITIONAL_OBSTACLES:
            positions_of_objects.append((x, y))
            amount_of_objects -= 1
    return positions_of_objects


def insert_objects(board, positions, type_of_object):
    if type_of_object == "S":
        colored_output = colors['red'] + "\bS" + colors['reset']
    elif type_of_object == "V":
        colored_output = colors['yellow'] + "\bC" + colors['reset']
    elif type_of_object == "C":
        colored_output = colors['violet'] + "\bC" + colors['reset']
    elif type_of_object == "K":
        colored_output = colors['violet'] + "\bK" + colors['reset']
    for x, y in positions:
        board[y-1][x-1] = colored_output
    return board


def move_enemies(board, positions, OBSTACLES):
    new_positions = []
    for x, y in positions:
        direction = random.randint(1, 4)
        if direction == 1 and board[y-2][x-1] not in OBSTACLES+ADDITIONAL_OBSTACLES:
            new_positions.append((x, y-1))
        elif direction == 2 and board[y][x-1] not in OBSTACLES+ADDITIONAL_OBSTACLES:
            new_positions.append((x, y+1))
        elif direction == 3 and board[y-1][x-2] not in OBSTACLES+ADDITIONAL_OBSTACLES:
            new_positions.append((x-1, y))
        elif direction == 4 and board[y-1][x] not in OBSTACLES+ADDITIONAL_OBSTACLES:
            new_positions.append((x+1, y))
        else:
            new_positions.append((x, y))
    return new_positions


def kill_enemies(enemy_positions, player_x, player_y, range_of_weapon, hero_status):
    i = 0
    while i < len(enemy_positions):
        if abs(player_x-enemy_positions[i][0]) <= range_of_weapon and \
           abs(player_y-enemy_positions[i][1]) <= range_of_weapon:
            # print(enemy_positions[i])
            del enemy_positions[i]
            manage_events(status=hero_status, event="enemy_killed")
            return
        i += 1
    manage_events(status=hero_status, event="shot_fired")


def enemy_shooting(enemy_positions, player_x, player_y, hero_status):
    i = 0
    while i < len(enemy_positions):
        if abs(player_x-enemy_positions[i][0]) <= 2 and \
           abs(player_y-enemy_positions[i][1]) <= 2:
           manage_events(status=hero_status, event="enemy_shot")
        i += 1


def pick_up_item(item_positions, player_x, player_y, hero_status):
    i = 0
    while i < len(item_positions):
        if abs(player_x - item_positions[i][0]) <= 1 and abs(player_y-item_positions[i][1]) <= 1:
            del item_positions[i]
            manage_events(status=hero_status, event="chest_opened")
            break
        i += 1
