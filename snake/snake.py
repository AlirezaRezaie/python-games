import pygame
from consts import *
from nn import NueralNetwork
import numpy as np
from math import sqrt

moves = ["up","down","right","left"]
class axis:
    def __init__(self,x_axis,y_axis):
        self.x = x_axis
        self.y = y_axis

class Snake:
    collid = False
    def __init__(self,window,foods,brain = None):
        self.window = window
        self.foods = foods
        self.vel = 20
        self.score = 0
        self.size = PIXEL_SIZE
        self.direction = [0,0,1,0]
        self.start = (round(random.randrange(0,width-PIXEL_SIZE)/PIXEL_SIZE)* PIXEL_SIZE,
             (round(random.randrange(0,width-PIXEL_SIZE)/PIXEL_SIZE)* PIXEL_SIZE ))
        self.cells = [
            self.start,(self.start[0]+self.size,self.start[1])
        ]
        self.survival = 0
        self.color = tuple(np.random.randint(0, 256, size=3))
        self.head = axis(*self.cells[-1])
        if brain:
            self.brain = brain
        else:
            self.brain = NueralNetwork(9,20,15,5)

    def collided(self,objs):
            for obj in objs:
                if self.head.x == obj[0] and self.head.y == obj[1]:
                    return True
            return False
        
    def think(self):
        smallest = 1000
        for food in self.foods:
            
            distance_from_food = sqrt((self.head.x - food.x)**2+(self.head.y-food.y)**2)
            if distance_from_food < smallest:
                smallest = distance_from_food
        distances = [
        self.head.y,  # distance to top wall
        height - self.head.y,  # distance to bottom wall
        self.head.x,  # distance to left wall
        width - self.head.x,  # distance to right wall
        ]   

        # take minimum distance as the distance to the nearest wall
        distance_to_wall = min(distances)
            
        prediction = self.brain.predict([distance_from_food,*distances,*self.direction])
        return prediction
    
    def draw(self):
        
        # append new head to cells if not exists
        if (self.head.x,self.head.y) not in self.cells: 
            self.survival += 1
            self.cells.append((self.head.x,self.head.y))

        # remove cells that are no longer part of the snake's body
        if not self.collid and not len(self.cells) == 2:
            self.cells.remove(self.cells[0])
        # apply direction value to the corresponding axis        
        match moves[np.argmax(self.direction)]:
            case "up":
                self.head.y += -self.vel
            case "down":
                self.head.y += self.vel
            case "right":
                self.head.x += self.vel
            case "left":
                self.head.x += -self.vel

        for cell in self.cells:
            rect = pygame.Rect(cell[0],cell[1],self.size,self.size)
            pygame.draw.rect(self.window, self.color, rect)
        

