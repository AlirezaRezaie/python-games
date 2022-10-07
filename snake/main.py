from typing import Literal
import pygame
import random

pygame.init()
width,height = 800,800
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

PIXEL_SIZE = 20

def gen_rand_color():
    return (random.randrange(255) , random.randrange(255) , random.randrange(255))	

class axis:
    def __init__(self,x_axis,y_axis):
        self.x = x_axis
        self.y = y_axis

class Snake:
    def __init__(self):
        self.vel = 20
        self.size = PIXEL_SIZE
        self.direction : Literal['up', 'down', 'right', 'left'] = 'right'
        self.cells = [(0,20),(20,20)]
        self.colors = [(0,255,255),(255,0,0)]
        self.head = axis(*self.cells[-1])


    def draw(self):
        # append new head to cells if not exists
        if (self.head.x,self.head.y) not in self.cells: 
            self.cells.append((self.head.x,self.head.y))
        # apply direction value to the corresponding axis
        match self.direction:
            case "up":
                self.head.y += -self.vel

            case "down":
                self.head.y += self.vel
                
            case "right":
                self.head.x += self.vel
                
            case "left":
                self.head.x += -self.vel
        
        # check and manage field barrier

        # colid right
        if self.head.x > width - PIXEL_SIZE: self.head.x = 0
        # colid left
        elif self.head.x < 0: self.head.x = width - PIXEL_SIZE
        # colid up
        elif self.head.y < 0: self.head.y = width - PIXEL_SIZE
        # colid down
        elif self.head.y > height - PIXEL_SIZE: self.head.y = 0


        if not collid and not len(self.cells) == 2:
            self.cells.remove(self.cells[0])
        else:
            print("snake grow")
            self.colors.append(gen_rand_color())

        self.colors.reverse()
        for cell,color in zip(self.cells,self.colors):
            rect = pygame.Rect(cell[0],cell[1],self.size,self.size)
            pygame.draw.rect(window, color, rect)
        self.colors.reverse()

class Food:
    x = 80
    y = 80
    transparency = 150
    inc = 5
    def draw(self,x ,y):
        self.x = x
        self.y = y
        if self.transparency >= 255:
           self.inc *= -1 
        elif self.transparency < 150:
           self.inc *= -1
        self.transparency += self.inc
        rect = pygame.Rect(self.x,self.y,PIXEL_SIZE,PIXEL_SIZE)
        pygame.draw.rect(window,(0,self.transparency,0),rect)
        
    def respawn(self):
        x,y = self.gen_random_pos()
        self.draw(x,y)

    def gen_random_pos(self):
        posx = round(random.randrange(0,width-PIXEL_SIZE)/PIXEL_SIZE)* PIXEL_SIZE 
        posy = round(random.randrange(0,height-PIXEL_SIZE)/PIXEL_SIZE)* PIXEL_SIZE
        return posx,posy

def collided(objs:list[tuple[()]]) -> bool:
    for obj in objs:
        if snake.head.x == obj[0] and snake.head.y == obj[1]:
            return True


snake = Snake()
food = Food()

score = 0
run = True
while run:
    collid = False
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake.direction == "down":
                snake.direction = "up"
            elif event.key == pygame.K_DOWN and not snake.direction == "up":
                snake.direction = "down"
            elif event.key == pygame.K_RIGHT and not snake.direction == "left":
                snake.direction = "right"
            elif event.key == pygame.K_LEFT and not snake.direction == "right":
                snake.direction = "left"

    # check if food eaten
    if collided([(food.x,food.y)]):
        food.respawn() 
        score += 1
        collid = True
    
    # check if self bitten
    if collided(snake.cells) and not len(snake.cells) == 2:
        run = False

    window.fill((100,100,100))
    food.draw(food.x,food.y) 
    snake.draw()
    pygame.display.flip()
    

pygame.quit()

print("your score:",score)

exit()