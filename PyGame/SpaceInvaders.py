import pygame
from Ship import Ship
from Enemy import Enemy

pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

SCREENWIDTH=400
SCREENHEIGHT=500

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Spaca Invaders")

carryOn = True
clock = pygame.time.Clock()

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

ship = Ship(screen)

ship.rect.x = 200
ship.rect.y = 300

all_sprites_list.add(ship) # Add the car to the list of objects


while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Pressing the x Key will quit the game
                 carryOn=False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        ship.moveRight(5)



    all_sprites_list.update()

    # lógica del juego aquí



    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    pygame.display.flip() #Refresh Screen

     # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()






# https://www.101computing.net/creating-sprites-using-pygame/
