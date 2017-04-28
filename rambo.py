import os
import sys


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


def create_board(width, height):
    vertical = [["\bX"] * width]
    middle = []
    for i in range(height-2):
        middle.append(list(["\bX"] + ["\b "] * (width-2) + ["\bX"]))
    middle[2][2] = "\bX"
    playboard = vertical + middle + vertical
    return playboard


def print_board(board):
    os.system("clear")
    for line in board:
        print(*line)


def insert_player(board, x, y):
    board[y-1][x-1] = "\b@"
    return board


def print_status_bar(width_of_bar, status):
    print("-"*width_of_bar)
    for line in status:
        if line[0] == "Inventory":
            # First count amount of signs of elements in inventory
            amount_of_signs = 0
            for item in line[1]:
                amount_of_signs += len(item)
            # width_of_spacing is equal
            witdh_of_spacing = width_of_bar-21-amount_of_signs-len(line[1])
            print("| {:>15}: ".format(line[0]), *line[1], 
                  "{:{align}{width}}".format(" ", align="<", width=witdh_of_spacing)
                  + "|" )
        else:
            print("| {:>15}:  {}".format(line[0], line[1]) + 
                                       " "*(width_of_bar-21-len(str(line[1]))) +
                                       "|" )
    print("-"*width_of_bar)


def main():
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    x = int(sys.argv[3])
    y = int(sys.argv[4])
    status = [["Lives", 5], ["Energy", 100], ["Experience", 0] ,["Inventory",["Dict","Key","Fuel","Joar"]]]
    while True:
        size = create_board(width, height)
        board = insert_player(size[:], x, y)
        print_board(board)
        print_status_bar(width, status)
        # print("lives = 10", y, x)
        # print("up {} down {} left {} right {}".format(board[y-2][x-1], board[y][x-1], board[y-1][x-2], board[y-1][x]))
        movement = getch()
        # When any 'WSAD' key press and coresponding position is not "\bX" player moves
        if movement == "w" and board[y-2][x-1] != "\bX":
            y -= 1
        if movement == "s" and board[y][x-1] != "\bX":
            y += 1
        if movement == "a" and board[y-1][x-2] != "\bX":
            x -= 1
        if movement == "d" and board[y-1][x] != "\bX":
            x += 1
        if movement == "q":
            exit()


if __name__ == '__main__':
    main()

