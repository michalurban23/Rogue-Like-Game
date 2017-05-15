from os import system
from cc_colors import *


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
    system("clear")
    print("Welcome to:\n")
    print(RED + arts[0], RESET)
    print("Type:\n")
    print("start - to start a new game")
    print("howto - to learn how to play the game")
    print("highscores - to display a highscore list")
    print("about - to learn more about the authors")
    print("exit - to leave the game (although you might regret it!)")
    choice = proper_input_choice()


def proper_input_choice():
    while True:
        choice = input()
        if choice.lower() == "start":
            return
        elif choice.lower() == "howto":
            show_rules()
        elif choice.lower() == "highscores":
            show_highscores()
        elif choice.lower() == "about":
            show_credits()
        elif choice.lower() == "exit":
            exit()
        else:
            print("\nPlease enter a valid command :)\n")


def start_game():
    system("clear")


def show_highscores():
    system("clear")
    print("Highscores")
    input("Press enter to go back to menu ")


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


with open("ascii_arts.txt", "r") as file:
    ascii_arts = file.read().split(',')
    arts = []
    for element in ascii_arts:
        arts.append(element)
