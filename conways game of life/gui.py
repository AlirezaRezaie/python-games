import pygame
from utils import next_gen,quadtree,PIXEL_SIZE

BLACK = (0,0,0)
WHITE = (255,255,255)

def gui(window,state,shape):

    clock = pygame.time.Clock()
    stop = True
    drawquad = True
    mouse = "up"
    run = True
    while run:
        clock.tick(20)
        for event in pygame.event.get(): 
            # mouse events
            if event.type == pygame.MOUSEBUTTONUP:
                print("up")
                mouse = "up"

            if event.type == pygame.MOUSEBUTTONDOWN:
                print('down')
                mouse = "down"
                
            # keyboard events
            if event.type == pygame.KEYDOWN:
                # toggle pause game
                if event.key == pygame.K_d:
                    if stop : stop = False
                    else :stop = True
                # toggle draw quad
                if event.key == pygame.K_p:
                    if drawquad : drawquad = False
                    else :drawquad = True

            if event.type == pygame.QUIT:
                run = False

        if mouse == "down":
                x,y = pygame.mouse.get_pos()
                state[int(y/PIXEL_SIZE)][int(x/PIXEL_SIZE)] = 1
        window.fill((0,0,0))
        points = []
        # draw each cell represented by the state matrix to the screen
        for i in range(shape[0]):
            for j in range(shape[1]):
                rect = pygame.Rect(j*PIXEL_SIZE,i*PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE)

                if state[i][j] == 0:
                    pygame.draw.rect(window,BLACK,rect)

                if state[i][j] == 1:
                    pygame.draw.rect(window,WHITE,rect)
                    points.append((j*PIXEL_SIZE,i*PIXEL_SIZE))


        if stop : 
            pygame.display.flip()
            continue
        if drawquad:
            quadtree([[0,0],[shape[0]*PIXEL_SIZE,shape[1]*PIXEL_SIZE]],points,window=window)
         
        state = next_gen(state.copy(),shape)
        pygame.display.flip()
    pygame.quit()
    exit()

