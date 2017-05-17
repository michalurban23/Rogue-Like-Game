from rambo_colors import *

STARTING_STATUS = {"Lives": 3,
                   "Energy": 100,
                   "Experience": 0,
                   "Ammo": 20,
                   "Weapon": "Beretta",
                   "Hero Level": 1,
                   "Keys": 0}


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
