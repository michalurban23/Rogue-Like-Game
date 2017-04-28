import os
import sys
from colored import fg, bg, attr

colors = {'green': bg('green') + fg('green'), 'blue': bg('blue') + fg('blue'), 'black': bg('black') + fg('black'),
          'dark_orange': bg('dark_orange_3a') + fg('dark_orange_3a'), 'yellow4b': bg('yellow_4b') + fg('yellow_4b'),
          'reset': attr('reset')}
OBSTACLES = [colors['black']+"\bX"+colors['reset'], "\bW", colors['green']+"\bT"+colors['reset']]


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
                element = colors['green'] + "\b" + element + colors['reset']
            elif element == "X":
                element = colors['black'] + "\b" + element + colors['reset']
            elif element == "R":
                element = colors['blue'] + "\b" + element + colors['reset']
            elif element == "B" or element == "W":
                element = colors['dark_orange'] + "\b" + element + colors['reset']
            else:
                element = colors['yellow4b'] + "\b" + element + colors['reset']
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
        size = create_board(sys.argv[1])
        #size = create_board("pow_camp.txt")
        board = insert_player(size[:], x, y)
        print_board(board)
        movement = getch()
        # When any 'WSAD' key press and coresponding position is not "\bX" player moves
        if movement == "w" and board[y-2][x-1] not in OBSTACLES:
            y -= 1
        if movement == "s" and board[y][x-1] not in OBSTACLES:
            y += 1
        if movement == "a" and board[y-1][x-2] not in OBSTACLES:
            x -= 1
        if movement == "d" and board[y-1][x] not in OBSTACLES:
            x += 1
        if movement == "q":
            exit()


if __name__ == '__main__':
    main()
