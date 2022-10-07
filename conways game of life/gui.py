import pygame
from utils import next_gen,PIXEL_SIZE

BLACK = (0,0,0)
WHITE = (255,255,255)

def gui(window,state,shape):

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        window.fill((0,0,0))
        for i in range(shape[0]):
            for j in range(shape[1]):
                rect = pygame.Rect(j*PIXEL_SIZE,i*PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE)
                

                if state[i][j] == 0:
                    pygame.draw.rect(window,BLACK,rect)

                if state[i][j] == 1:
                    pygame.draw.rect(window,WHITE,rect)


        state = next_gen(state.copy(),shape)
        pygame.display.flip()
        
    pygame.quit()
    exit()

