import pygame
import random
import time,math
from slime import Slime


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Slime Jump")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


s = Slime((SCREEN_WIDTH/2,SCREEN_HEIGHT-80))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
game_over = False

start_time = time.time()

tick=0
seconds = 0
index=1
is_jumping=False
on_ground =True
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while run:
    clock.tick(60)

    dt = clock.tick(60)/1000
    #print(dt)

    screen.fill((0,255,100))
    screen.blit(s.image,s.rect)

    #MAIN EVENT LOOP
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        #if event.type == pygame.K_SPACE and is_jumping == False:



    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        s.move('left',dt)
    if keys[pygame.K_RIGHT]:
        s.move('right',dt)
    if keys[pygame.K_SPACE]:
        if is_jumping == False:
            is_jumping = True
            on_ground = False
    else:
        if is_jumping==True:
           is_jumping = s.jump()




    #animation
    if is_jumping==False:
        index += 1 * dt
        index = math.ceil(index)
        if index==11:
            index = 1
        s.animate('idle',index)
    else:
        index+=1*(dt)
        index=math.ceil(index)
        if index==11:
            index=1
            is_jumping=False
        s.animate('jump',index)




    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




