import os
import sys
from colored import fg, bg, attr

color = bg('dark_khaki') + fg('white')
green = bg('green') + fg('green')
blue = bg('blue') + fg('blue')
black = bg('black') + fg('black')
reset = attr('reset')
FORBIDDEN_MOVES = ["\bX", "\bW", green+"\bT"+reset]

def getch():
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def create_board(file_name):
    playboard = []
    with open(file_name, "r") as board:
        playboard_temp = board.readlines()
    for line in playboard_temp:
        playboard_line = []
        for element in line[:-1]:
            if element == "T":
                element = green + "\b" + element + reset
            elif element == "X":
                element = black + "\b" + element + reset
            elif element == "R":
                element = blue + "\b" + element + reset
            else:
                element = color + "\b" + element + reset
            playboard_line.append(element)
        playboard.append(playboard_line)
    return playboard


def print_board(board):
    os.system("clear")
    for line in board:
        print(*line)


def insert_player(board, x, y):
    board[y-1][x-1] = "\b@"
    return board


def main():
    x = 2
    y = 2
    while True:
        size = create_board("vietnam_jungle.txt")
        board = insert_player(size[:], x, y)
        print_board(board)
        # print("lives = 10", y, x)
        # print("up {} down {} left {} right {}".format(board[y-2][x-1], board[y][x-1], board[y-1][x-2], board[y-1][x]))
        movement = getch()
        # When any 'WSAD' key press and coresponding position is not "\bX" player moves
        if movement == "w" and board[y-2][x-1] not in FORBIDDEN_MOVES:
            y -= 1
        if movement == "s" and board[y][x-1] not in FORBIDDEN_MOVES:
            y += 1
        if movement == "a" and board[y-1][x-2] not in FORBIDDEN_MOVES:
            x -= 1
        if movement == "d" and board[y-1][x] not in FORBIDDEN_MOVES:
            x += 1
        if movement == "q":
            exit()


if __name__ == '__main__':
    main()
