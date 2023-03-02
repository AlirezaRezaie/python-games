import pygame
from snake import Snake
from food import Food
from consts import *
import numpy as np

pygame.init()

window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

foods = []
for _ in range(20):
    foods.append(Food(window))
snakes = []
for _ in range(50):
    snakes.append(Snake(window,foods))

run = True
gen = 0
highest_score = -1
best_snake = None
best_survival = 0
while run:
    clock.tick(120)
    gen +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        #elif event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_UP and not snake.direction == [0,1,0,0]:
        #        snake.direction = [1,0,0,0]
        #    elif event.key == pygame.K_DOWN and not snake.direction == [1,0,0,0]:
        #        snake.direction = [0,1,0,0]
        #    elif event.key == pygame.K_RIGHT and not snake.direction == [0,0,0,1]:
        #        snake.direction = [0,0,1,0]
        #    elif event.key == pygame.K_LEFT and not snake.direction == [0,0,1,0]:
        #        snake.direction = [0,0,0,1] 

    for snake in snakes:
        pred = snake.think()
        if not np.argmax(pred) == 4:
            arr= [0,0,0,0]
            arr[np.argmax(pred)] = 1
            if arr == [1,0,0,0] and not snake.direction == [0,1,0,0]:
                snake.direction = [1,0,0,0]
            elif arr == [0,1,0,0] and not snake.direction == [1,0,0,0]:
                snake.direction = [0,1,0,0]
            elif arr == [0,0,1,0] and not snake.direction == [0,0,0,1]:
                snake.direction = [0,0,1,0]
            elif arr == [0,0,0,1] and not snake.direction == [0,0,1,0]:
                snake.direction = [0,0,0,1] 

        # check if self bitten
        if snake.collided(snake.cells) and not len(snake.cells) == 2:
            snakes.remove(snake)

        # check and manage field barrier
        if snake.head.x > width - PIXEL_SIZE or snake.head.x < 0 or snake.head.y < 0 or snake.head.y > height - PIXEL_SIZE:
            snakes.remove(snake)

        snake.draw()
        snake.collid = False

    for food in foods:
        for snake in snakes:
            # check if food eaten
            if snake.collided([(food.x,food.y)]) and food in foods:
                foods.remove(food)
                print("food removed")
                snake.score += 1
                snake.collid = True

    # Draw all remaining food items
    for food in foods:
        food.draw()
        
    pygame.display.flip()
    window.fill((100,100,100))

    for snake in snakes:
        if snake.score > highest_score:
            print("new snake stronger")
            highest_score = snake.score
            best_snake = snake

                     
    if gen == 50:
        
        gen = 0
        print("last snake reached")

                
        foods = []
        for _ in range(10):
            foods.append(Food(window))
        snakes = []    
        for _ in range(50):
            brain = best_snake.brain
            brain.w1 += np.random.normal(scale=0.2, size=best_snake.brain.w1.shape)
            brain.w2 += np.random.normal(scale=0.3, size=best_snake.brain.w2.shape)
            brain.w3 += np.random.normal(scale=0.7, size=best_snake.brain.w3.shape)
            snakes.append(Snake(window,foods,brain=brain))
        snakes.append(best_snake)
    

pygame.quit()

exit()