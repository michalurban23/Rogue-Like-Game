from rambo_colors import *

STARTING_STATUS = {"Lifes": 3,
                   "Energy": 100,
                   "Experience": 0,
                   "Ammo": 20,
                   "Weapon": "Beretta",
                   "Hero Level": 1,
                   "Keys": 0}
BORDER = colors['black'] + "-" + colors['reset']


def print_status_bar_basic(status):
    print(BORDER * 17 +
          BORDER*3, BLUE + "Lifes:" + RED + "{:>10}".format(status["Lifes"]),
          BORDER*3, BLUE + "Level:" + RED + " {:>10}".format(status["Hero Level"]),
          BORDER*3, BLUE + "Weapon:" + RED + " {:>10}".format(status["Weapon"]),
          BORDER*3, BLUE + "Ammo:" + RED + " {:>10}".format(status["Ammo"]),
          BORDER*3, BLUE + "Energy:" + RED + " {:>10}".format(status["Energy"]),
          BORDER * 17)
    print(BORDER*144 + colors['reset'])


def print_status_bar_extended(status):
    ext_inv = ["Current hero level: {}Your current exp: {}"]
    for element in ext_inv:
        print(BORDER + element + BORDER)
    print(BORDER*144 + colors['reset'])
