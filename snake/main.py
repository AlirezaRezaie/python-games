import pygame
from snake import Snake, snakes
from food import Food, foods
from consts import *
import numpy as np
import time

pygame.init()

clock = pygame.time.Clock()

run = True
gen = 0
end_gen = False
while run:
    clock.tick(30)
    gen += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for snake in snakes:
        snake.step()

    # Draw all remaining food items
    for food in foods:
        food.draw()

    pygame.display.flip()
    window.fill((100, 100, 100))

    for snake in snakes:
        if snake.score > 5:
            end_gen = True

    if gen > 100:
        end_gen = True

    if end_gen:
        end_gen = False
        gen = 0
        snakes.clear()
        foods.clear()
        print("last snake reached it was")
        print_colored_char("    ", Snake.best_snake.color)
        print()
        time.sleep(1)

        for _ in range(20):
            foods.append(Food())

        for _ in range(10):
            brain = Snake.best_snake.brain
            brain.w1 += np.random.uniform(
                low=-0.1, high=0.1, size=Snake.best_snake.brain.w1.shape
            )
            brain.w2 += np.random.uniform(
                low=-0.1, high=0.1, size=Snake.best_snake.brain.w2.shape
            )
            brain.w3 += np.random.uniform(
                low=-0.1, high=0.1, size=Snake.best_snake.brain.w3.shape
            )
            snakes.append(Snake(brain=brain))

        Snake.best_snake = None
        # snakes.append(Snake.best_snake)

pygame.quit()
