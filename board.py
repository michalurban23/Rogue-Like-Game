from os import system
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
    vertical = ["X" * width]
    middle = []
    for i in range(height-2):
        middle.append("X" + " " * (width-2) + "X")
    playboard = vertical + middle + vertical
    return playboard


def print_board(board):
    system("clear")
    for line in board:
        print(line)


def insert_player(board, x, y):
    board.insert(y-1, board[y-1][:x-1] + "@" + board[y-1][x:])
    board.pop(y)
    return board


def proper_input_size(message):
    while True:
        number = input(message)
        if number.isdecimal:
            try:
                if int(number) > 2:
                    return int(number)
                else:
                    print("Must be greater than 2")
            except ValueError:
                print("Must be integer")


def proper_input_player(size, message):
    while True:
        number = input(message)
        if number.isdecimal:
            try:
                if int(number) > 1 and int(number) < size:
                    return int(number)
                else:
                    print("Must be inside")
            except ValueError:
                print("Must be integer")


def main():
    try:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        x = int(sys.argv[3])
        y = int(sys.argv[4])
    except:
        width = proper_input_size("Enter width of board: ")
        height = proper_input_size("Enter height of board: ")
        x = proper_input_player(width, "Enter player x position: ")
        y = proper_input_player(height, "Enter player y position: ")
    while True:
        size = create_board(width, height)
        board = insert_player(size, x, y)
        print_board(board)
        movement = getch()
        if movement == "w" and y > 2:
            y -= 1
        if movement == "s" and y < height-1:
            y += 1
        if movement == "a" and x > 2:
            x -= 1
        if movement == "d" and x < width-1:
            x += 1
        if movement == "q":
            exit()


if __name__ == '__main__':
    main()
