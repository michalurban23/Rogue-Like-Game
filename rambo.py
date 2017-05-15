import os
import sys
from colored import fg, bg, attr

colors = {'green': bg('green') + fg('green'), 'blue': bg('blue') + fg('blue'), 'black': bg('black') + fg('black'),
          'dorange': bg('dark_orange_3a') + fg('dark_orange_3a'), 'yellow4b': bg('yellow_4b') + fg('yellow_4b'),
          'dred': bg('red_3a') + fg('red_3a'), 'reset': attr('reset')}
OBSTACLES = [colors['black']+"\bX"+colors['reset'],  # Edges
             colors['dorange']+"\bW"+colors['reset'],  # Walls
             colors['green']+"\bT"+colors['reset']]  # Trees


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


def show_ascii_intro():
    os.system("clear")
    with open("intro.txt", "r") as file:
        rambo_ascii = file.readlines()
        i = 0
        for line in rambo_ascii:
            i += 1
            if i % 2 != 1:
                print(fg('wheat_1'), line[:-1])


def show_main_menu():
    pass


def start_game():
    pass


def show_highscores():
    pass


def show_credits():
    pass


def show_rules():
    pass


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
                # element = "\b" + element
            playboard_line.append(element)
        playboard.append(playboard_line)
    return playboard


def print_board(board):
    os.system("clear")
    for line in board:
        print(*line)


def insert_player(board, x, y):
    board[y-1][x-1] = bg('white')+fg('red')+"\b"+chr(920)
    return board


def print_status_bar(width_of_bar, status):
    print(colors['black']+"-"*width_of_bar+colors['reset'])
    for line in status:
        if line[0] == "Inventory":
            # First count amount of signs of elements in inventory
            amount_of_signs = 0
            for item in line[1]:
                amount_of_signs += len(item)
            # width_of_spacing is equal
            witdh_of_spacing = width_of_bar-21-amount_of_signs-len(line[1])
            print(colors['black']+"|"+colors['reset']+" {:>15}: ".format(line[0]), *line[1],
                  "{:{align}{width}}".format(" ", align="<", width=witdh_of_spacing)
                  + colors['black']+"|"+colors['reset'])
        else:
            print(colors['black']+"|"+colors['reset']+" {:>15}:  {}".format(line[0], line[1]) +
                  " "*(width_of_bar-21-len(str(line[1]))) + colors['black']+"|"+colors['reset'])
    print(colors['black']+"-"*width_of_bar+colors['reset'])


def main():
    x = 2
    y = 2
    status = [["Lives", 5], ["Energy", 100], ["Experience", 0], ["Inventory", ["Dict", "Key", "Fuel", "Joar"]]]
    show_ascii_intro()
    input("Press enter to continue")
    show_main_menu()
    while True:
        background = create_board(sys.argv[1])
        board = insert_player(background[:], x, y)
        print_board(board)
        print_status_bar(len(board[0]), status)
        movement = getch()
        # When any 'WSAD' key press and coresponding position is not illegal player moves
        if movement == "w" and board[y-2][x-1] not in OBSTACLES:
            y -= 1
        if movement == "s" and board[y][x-1] not in OBSTACLES:
            y += 1
        if movement == "a" and board[y-1][x-2] not in OBSTACLES:
            x -= 1
        if movement == "d" and board[y-1][x] not in OBSTACLES:
            x += 1
        if movement == "q":
            if input("Type 'quit' to exit ") == "quit":
                exit()


if __name__ == '__main__':
    main()
