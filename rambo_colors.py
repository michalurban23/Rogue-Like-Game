from colored import fg, bg, attr

BLACK = "\033[0;30m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"
LPURPLE = "\033[1;35m"
GRAY = "\033[0;37m"

RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
UNDERLINE = "\033[4;31m"

colors = {'green': bg('green') + fg('green'), 'blue': bg('blue') + fg('blue'), 'black': bg('black') + fg('black'),
          'dorange': bg('dark_orange_3a') + fg('dark_orange_3a'), 'yellow4b': bg('yellow_4b') + fg('yellow_4b'),
          'dred': bg('red_3a') + fg('red_3a'), 'violet': bg('deep_pink_4c') + fg('deep_pink_4c'),
          'yellow': bg('light_yellow') + fg('light_yellow'), 'red': bg('red') + fg('red'),
          'sblue': bg('sky_blue_1') + fg('sky_blue_1'), 'gray': bg('grey_54') + fg('grey_54'),
          'reset': attr('reset')}

# Blue             \e[0;34m
# Cyan             \e[0;36m
# Red              \e[0;31m
# Purple           \e[0;35m
# Dark Gray        \e[1;30m
# Light Blue       \e[1;34m
# Light Green      \e[1;32m
# Light Cyan       \e[1;36m
# Light Red        \e[1;31m
