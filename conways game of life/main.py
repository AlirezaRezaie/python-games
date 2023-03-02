import argparse
import numpy
import pygame
from utils import PIXEL_SIZE

# initializing the parser
parser = argparse.ArgumentParser(description='conways game of life implementation in python!!')

parser.add_argument('-t','--type',choices=["gui","cli"],
                    help='game run type',required=True)

parser.add_argument('-s','--size',type=int,default=100,
                    help='grid size (x,x)',required=False)


def Init_State(w,h):
    """
        creates a random grid
    """

    state = numpy.random.choice([0,0,0,0,0,0,0,0,0],(w ,h))
    shape = numpy.shape(state)
    return state,shape


args = parser.parse_args()
args.size = tuple([args.size]*2)
match args.type:
    case 'gui':
        import gui
        pygame.init()
    
        window = pygame.display.set_mode((args.size[0]* PIXEL_SIZE, args.size[1]* PIXEL_SIZE))
        gui.gui(window,*Init_State(*args.size))

    case 'cli':
        import cli
        cli.cli(*Init_State(*args.size))
    case _:
        print("error")
    