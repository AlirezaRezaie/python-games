import random

width,height = 800,800
PIXEL_SIZE = 20

def gen_rand_color():
    return (random.randrange(255) , random.randrange(255) , random.randrange(255))
