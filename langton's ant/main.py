# yet to be completed

import pygame
import numpy

width,height = 200,200

pygame.init()
PIXEL_SIZE = 10
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class Screen:
    def __init__(self) -> None:
        self.width = (width,width)
        self.grid = list(numpy.zeros((100,100)))
        self._shape = numpy.shape(self.grid) 

    def draw(self):
        for i in range(self._shape[0]):
            for j in range(self._shape[1]):
                rect = pygame.Rect(i * PIXEL_SIZE,j * PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE)
                if self.grid[i][j] == 0:
                    pygame.draw.rect(window,(0,0,0),rect)
                else:
                    pygame.draw.rect(window,(255,255,255),rect)

class Ant:
    def __init__(self) -> None:
        self.pointer = (10,10)
        self.arrow = (0,1)

    def turn(self,direction):
        match direction:
            case "right":
                self.pointer = (self.pointer[0] + self.arrow[0],self.pointer[1]  + self.arrow[0])
            case "left":
                self.pointer = (self.pointer[0] - self.arrow[0],self.pointer[1]  - self.arrow[0])

screen = Screen()
ant = Ant()

screen.grid[10][10] = 1
run = True
while run:
    collid = False
    clock.tick(60)

    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    screen.draw()
    ant.draw()
    pygame.display.flip()
    

pygame.quit()
exit()
