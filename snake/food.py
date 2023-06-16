import pygame
from consts import *
from consts import window


class Food:
    def __init__(self, transparency=150, inc=5):
        self.x, self.y = self.gen_random_pos()
        self.transparency = transparency
        self.inc = inc

    def draw(self):
        if self.transparency >= 255:
            self.inc *= -1
        elif self.transparency < 150:
            self.inc *= -1
        self.transparency += self.inc
        rect = pygame.Rect(self.x, self.y, PIXEL_SIZE, PIXEL_SIZE)
        pygame.draw.rect(window, (0, self.transparency, 0), rect)

    def respawn(self):
        x, y = self.gen_random_pos()
        self.draw(x, y)

    def gen_random_pos(self):
        posx = round(random.randrange(0, width - PIXEL_SIZE) / PIXEL_SIZE) * PIXEL_SIZE
        posy = round(random.randrange(0, height - PIXEL_SIZE) / PIXEL_SIZE) * PIXEL_SIZE
        return posx, posy


foods = [Food() for food in range(30)]
