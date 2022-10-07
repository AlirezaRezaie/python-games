import sys
import os
from utils import next_gen
# import time

def cli(state,shape):
    os.system("clear")
    while True:
        for i in state:
            for j in i:
                if j == 0:
                    sys.stdout.write(".")
                if j == 1:
                    sys.stdout.write("@")
            sys.stdout.write("\n")
        state = next_gen(state.copy(),shape)
        #time.sleep(0.001)