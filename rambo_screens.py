from os import system
from rambo_colors import *


def show_ascii_intro():
    system("clear")
    with open("intro.txt", "r") as file:
        rambo_ascii = file.readlines()
        i = 0
        for line in rambo_ascii:
            i += 1
            if i % 2 != 1:
                print(CYAN, line[:-1])


def show_main_menu():
    while True:
        system("clear")
        print("Welcome to:\n")
        print(RED + ascii_arts(0), RESET)
        print("Type:\n")
        print("start - to start a new game")
        print("howto - to learn how to play the game")
        print("highscores - to display a highscore list")
        print("about - to learn more about the authors")
        print("exit - to leave the game (although you might regret it!)")
        choice = proper_input_choice()
        if choice == "start":
            return


def proper_input_choice():
    choice = input()
    if choice.lower() == "start":
        return choice
    elif choice.lower() == "howto":
        show_rules()
    elif choice.lower() == "highscores":
        show_highscores()
    elif choice.lower() == "about":
        show_credits()
    elif choice.lower() == "exit":
        exit()


def start_game():
    system("clear")
    print("game starting")
    input()


def show_highscores():
    system("clear")
    print("Highscores\n")
    try:
        open("highscores.txt")
    except FileNotFoundError:
        print("Couldn't find a hiscores.txt file in game directory")
    input("\nPress enter to go back to menu ")


def show_credits():
    system("clear")
    print("Credits")
    input("Press enter to go back to menu ")


def show_rules():
    system("clear")
    print("In rambo adventures game you are able of moving, fighting and interacting with enviroment")
    print("\nMovement:")
    print("W - move up")
    print("S - move down")
    print("A - move left:")
    print("D - move right:")
    print("\nFighting:")
    print("Space - ....")
    print("\nOther:")
    print("Q - quits the game")
    print("I - shows extended inventory")
    print("E - interact with doors and other objects\n\n")
    input("Press enter to go back to menu ")


def ascii_arts(n):
    with open("ascii_arts.txt", "r") as file:
        ascii_arts = file.read().split(',')
        arts = []
        for element in ascii_arts:
            arts.append(element)
    return arts[n]
