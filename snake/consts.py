import random
from pygame import display


width, height = 800, 800
PIXEL_SIZE = 20
window = display.set_mode((width, height))


def print_colored_char(char, rgb):
    r, g, b = rgb
    color_code = f"\033[48;2;{r};{g};{b}m"
    reset_code = "\033[0m"
    print(f"{color_code}{char}{reset_code}", end="")


def gen_rand_color():
    return (random.randrange(255), random.randrange(255), random.randrange(255))
