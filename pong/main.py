# yet to be completed

import pygame

pygame.init()
width,height = 800,800
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


class Bar:
    def __init__(self) -> None:
        self.x = 50
        self.y = 50
        self.direction = 20
    def draw(self):

        if bar.y < 0:
           self.direction = +20
        elif bar.y + 100 > height:
           self.direction = -20
        bar.y += self.direction
        rect = pygame.Rect(self.x,self.y,20,100)
        pygame.draw.rect(window, (255,0,0), rect)


class Ball:
   def __init__(self) -> None:
        self.x = 500
        self.y = 150
        self.x_inc = 20
        self.y_inc = 20
   def draw(self):
        global run
               # colid right

        if self.x > width - 20: self.x_inc *= -1 
        # colid left
        elif self.x < 0: run = False
        # colid up
        elif self.y < 0: self.y_inc *= -1 
        # colid down
        elif self.y > height - 20: self.y_inc *= -1

        self.x += self.x_inc
        self.y += self.y_inc
        rect = pygame.Rect(self.x,self.y,20,20)
        pygame.draw.rect(window, (0,0,255), rect)

   
bar = Bar()
ball = Ball()
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bar.direction =  -20
            elif event.key == pygame.K_DOWN:
                bar.direction = +20
        
    if ball.x < bar.x + 20 and bar.y < ball.y < bar.y +100:
        ball.x_inc *= -1
         
        print("colloid")
    window.fill((0,0,0))
    bar.draw()
    ball.draw()
    pygame.display.flip()
    

pygame.quit()
