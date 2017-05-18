from random import randint
import time
from rambo_hero_status import *
from rambo_screens import *

def user_input(n):
    while True:
        try:
            number = int(input("Its your {} attempt,type a three-digit number: ".format(n)))
            if number > 999 or number < 100:
                raise ValueError
        except ValueError:
            print("This is no number or it don't have 3 digits")
        else:
            return list(str(number))


def create_number():
    while True:
        random_number = list(str(randint(100, 999)))
        if random_number[0] == random_number[1] \
                or random_number[1] == random_number[2] \
                or random_number[2] == random_number[0]:
            pass
        else:
            break
    return random_number


hot_cold_message = ("""I am thinking of a 3-digit number. Try to guess what it is.

Here are some clues:

When I say:    That means:

  Cold       No digit is correct.

  Warm       One digit is correct but in the wrong position.

  Hot        One digit is correct and in the right position.

I have thought up a number. You have 10 guesses to get it.) """)


def main(status):
    number_to_guess_original = create_number()
    n = 1
    print(number_to_guess_original)
    start = time.time()
    diff = status["Inteligence"]
    print(hot_cold_message)
    while n <= diff:
        cold_check = 0
        number_to_guess = number_to_guess_original[:]
        user_guess = user_input(n)
        if user_guess == number_to_guess:
            end = time.time()
            print("Your time was {:.3}s and you needed {} guess(es)".format(end-start, n))
            input()
            show_victory_screen()
            break
        else:
            i = 0
            while i < len(number_to_guess):
                if number_to_guess[i] == user_guess[i]:
                    print("Hot")
                    number_to_guess.pop(i)
                    user_guess.pop(i)
                else:
                    i += 1
        for digit in user_guess:
            if digit in number_to_guess:
                print("warm")
            else:
                cold_check += 1
        if cold_check == 3:
            print("Cold")
        n += 1
    if n > diff:
        print("You ran out of tries. It was {:s}".format("".join(number_to_guess_original)))
        input()
        show_death_screen()


if __name__ == "__main__":
    main()
